import pdfplumber
import spacy
import re
import pandas as pd
import PyPDF2
from sentence_transformers import SentenceTransformer, util

# Load the spaCy model for NLP processing
nlp = spacy.load("en_core_web_sm")

# Load sentence transformer model for advanced contextual matching
sentence_model = SentenceTransformer('all-MiniLM-L6-v2')

# Define keywords and standards to search for
keywords = {
    'ISSB': ['ISSB Standards', 'IFRS S1', 'IFRS S2', 'ISSB Framework', 'International Sustainability Standards Board'],
    'GRI': ['GRI Standards', 'Global Reporting Initiative'],
    'TCFD': ['TCFD', 'Task Force on Climate-related Financial Disclosures'],
    'OECD': ['OECD Guidelines'],
    'UN': ['UN Principles']
}

# Define standards and frameworks with relevant keywords and patterns for contextual matching
framework_keywords = {
    'ISSB': ['sustainability risks', 'climate change', 'carbon emissions', 'financial materiality'],
    'GRI': ['stakeholder', 'community impact', 'social responsibility', 'human rights', 'sustainable development'],
    'TCFD': ['climate-related risks', 'financial impact of climate', 'governance of climate risks', 'metrics'],
    'OECD': ['due diligence', 'responsible business', 'human rights', 'anti-corruption'],
    'UN Principles': ['sustainable development goals', 'human rights', 'labor practices', 'environmental protection']
}

# Function to extract text from a PDF using pdfplumber
def extract_text_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        full_text = []
        for page in pdf.pages:
            full_text.append(page.extract_text())
        return full_text

# Function to extract text from a PDF using PyPDF2
def extract_text_from_pdf_py(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text += page.extract_text()
        return text

# Function to find sentences matching a keyword in the first approach (basic keyword matching)
def find_matching_sentences(text, keyword):
    sentences = re.split(r'(?<=\.)\s+', text)  # Split text into sentences
    matching_sentences = []
    for sentence in sentences:
        if any(k in sentence for k in keywords[keyword]):
            matching_sentences.append(sentence.strip())
    return matching_sentences

# Function for basic keyword matching to find relevant sentences
def find_matching_sentences_basic(text, frameworks):
    doc = nlp(text)
    sentences = [sent.text for sent in doc.sents]
    
    results = []
    for framework, keywords in frameworks.items():
        for sentence in sentences:
            if any(keyword.lower() in sentence.lower() for keyword in keywords):
                results.append({
                    'Framework': framework,
                    'Sentence': sentence,
                    'Context': "No additional context (basic keyword matching)",
                    'Similarity': "N/A"
                })
    return results

# Function for advanced contextual matching using sentence embeddings
def find_matching_sentences_with_context(text, frameworks):
    doc = nlp(text)
    sentences = [sent.text for sent in doc.sents]
    
    results = []
    for framework, keywords in frameworks.items():
        for sentence in sentences:
            # Check for keyword matches
            if any(keyword.lower() in sentence.lower() for keyword in keywords):
                # Check for entities related to sustainability or business in context
                entities = [ent.text for ent in doc.ents if ent.label_ in ["ORG", "GPE", "TIME", "MONEY"]]
                sentence_embedding = sentence_model.encode(sentence)
                
                # Check for contextual match using sentence embeddings (similarity)
                for keyword in keywords:
                    keyword_embedding = sentence_model.encode(keyword)
                    similarity = util.pytorch_cos_sim(sentence_embedding, keyword_embedding)[0][0].item()
                    
                    # If similarity is above a certain threshold, consider it a contextual match
                    if similarity > 0.6:
                        results.append({
                            'Framework': framework,
                            'Sentence': sentence,
                            'Context': f"Entities: {entities}",
                            'Similarity': similarity
                        })
    return results

# Function to extract content from a PDF with page numbers and run both matching approaches
def extract_content_with_page(pdf_path):
    # Initialize a list to store the results
    results = []

    # Extract the text from the PDF using pdfplumber
    pages = extract_text_from_pdf(pdf_path)

    # Loop through each page in the PDF
    for page_number, page_text in enumerate(pages, start=1):
        # Loop through each standard and its keywords for basic keyword matching
        for standard, standard_keywords in keywords.items():
            for keyword in standard_keywords:
                matches = find_matching_sentences(page_text, standard)
                if matches:
                    for match in matches:
                        # First, run basic matching and then advanced matching (embedding-based)
                        basic_matches = find_matching_sentences_basic(page_text, framework_keywords)
                        context_matches = find_matching_sentences_with_context(page_text, framework_keywords)
                        
                        # Combine the results
                        results.append({
                            'File': pdf_path,
                            'Page Number': page_number,
                            'Standard': standard,
                            'Description': f'Mentions {standard}',
                            'Evidence': keyword,
                            'Sentence': match,
                            'Contextual Matches': context_matches,
                            'Basic Matches': basic_matches
                        })
                else:
                    results.append({
                        'File': pdf_path,
                        'Page Number': page_number,
                        'Standard': standard,
                        'Description': f'No mentions found for {standard}',
                        'Evidence': '',
                        'Sentence': 'No relevant content found',
                        'Contextual Matches': '',
                        'Basic Matches': ''
                    })
    
    return results

# Function to analyze PDFs and combine results
def analyze_pdfs(pdf_paths):
    all_results = []

    # Process each PDF
    for pdf_path in pdf_paths:
        pdf_results = extract_content_with_page(pdf_path)
        all_results.extend(pdf_results)

    return all_results

# Example Usage
pdf_paths = ['Report1.pdf', 'Report2.pdf', 'Report3.pdf']  # Replace with actual PDF paths

# Analyze the PDFs
results = analyze_pdfs(pdf_paths)

# Create a DataFrame for easy viewing
df = pd.DataFrame(results)

# Display the results
print(df)

# Save the results to a CSV file
df.to_csv('sustainability_analysis.csv', index=False)
