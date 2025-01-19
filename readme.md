# PDF Sustainability Report Analysis

This project analyzes PDF sustainability reports and identifies mentions of various sustainability frameworks and standards. It utilizes Natural Language Processing (NLP) techniques to extract relevant content, match it with predefined keywords, and provide insights into the context of those mentions. The result is a detailed report, showing which sustainability standards (e.g., ISSB, GRI, TCFD) are mentioned in each report, along with the specific sentences and context where they appear.

## Features

- **PDF Text Extraction**: Extracts text from PDF reports.
- **Keyword Matching**: Identifies relevant mentions of sustainability standards (e.g., ISSB, GRI, TCFD, etc.) using keyword-based matching.
- **Contextual Matching**: Utilizes spaCy's NLP capabilities and sentence embeddings from Sentence-Transformers for more advanced contextual understanding.
- **Page-Level Reporting**: Provides the page number where each relevant sentence is found in the PDF.
- **Similarity Scoring**: For contextual matches, provides a similarity score to indicate how closely the sentence matches the relevant keyword or framework.
- **Output CSV**: Outputs the results in a CSV file for easy reporting and further analysis.

## Requirements

- **Python 3.7+**
- **Libraries**:
  - `pdfplumber`: For extracting text from PDF documents.
  - `spacy`: For basic NLP processing.
  - `sentence-transformers`: For advanced contextual analysis using sentence embeddings.
  - `PyPDF2`: For reading and extracting text from PDFs.
  - `pandas`: For organizing and outputting the results in a tabular format.

To install the required dependencies, run:

```bash
pip install pdfplumber spacy sentence-transformers PyPDF2 pandas
python -m spacy download en_core_web_sm
```

## Setup

1. **Clone this repository**:
   ```bash
   git clone https://github.com/yourusername/sustainability-report-analysis.git
   cd sustainability-report-analysis
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Download spaCy model**:
   ```bash
   python -m spacy download en_core_web_sm
   ```

## Usage

1. **Prepare your PDFs**:
   Place the PDF files you want to analyze in the same directory or specify the path in the `pdf_paths` list in the script.

2. **Run the analysis**:
   Execute the script to process the PDFs and generate the analysis:

   ```python
   from analysis import analyze_pdfs

   # List of PDF file paths to analyze
   pdf_paths = ['Report1.pdf', 'Report2.pdf', 'Report3.pdf']

   # Run the analysis
   results = analyze_pdfs(pdf_paths)

   # View the results in a DataFrame
   import pandas as pd
   df = pd.DataFrame(results)
   print(df)

   # Save the results to a CSV file
   df.to_csv('sustainability_analysis.csv', index=False)
   ```

   The script will process each PDF in the `pdf_paths` list, extracting relevant content, matching it with the predefined sustainability frameworks, and saving the results in a CSV file (`sustainability_analysis.csv`).

## Output

The output will be a CSV file containing detailed analysis for each PDF report. The CSV will contain the following columns:

| Column         | Description                                                               |
|----------------|---------------------------------------------------------------------------|
| **File**       | The name of the PDF file being analyzed.                                  |
| **Page Number**| The page number where the relevant sentence was found.                    |
| **Standard**   | The sustainability standard or framework (e.g., ISSB, GRI, TCFD).         |
| **Description**| A brief description indicating whether the standard is mentioned or not.  |
| **Evidence**   | The keyword found in the sentence that matched the framework.             |
| **Sentence**   | The full sentence from the PDF where the framework or standard is mentioned. |
| **Context**    | The context of the mention, including entities identified in the sentence (e.g., organization names, locations). |
| **Similarity** | For contextual matches, the similarity score between the sentence and the keyword. |

### Example Output

| File          | Page Number | Standard | Description                   | Evidence                | Sentence                                                                                     | Context                             | Similarity |
|---------------|-------------|----------|-------------------------------|-------------------------|----------------------------------------------------------------------------------------------|-------------------------------------|------------|
| Report1.pdf   | 1           | ISSB     | Mentions ISSB                 | IFRS S1                 | "The IFRS S1 standard outlines the approach for reporting sustainability risks."             | Entities: ["IFRS", "Financial"]    | 0.75       |
| Report1.pdf   | 2           | GRI      | Mentions GRI                  | sustainable development | "The company follows GRI guidelines to ensure sustainable development in its operations."     | Entities: ["GRI", "company"]       | 0.80       |
| Report2.pdf   | 3           | TCFD     | No mentions found for TCFD    |                         | "The company has no specific policy regarding climate-related financial disclosures."        | No entities found                  | N/A        |
| Report2.pdf   | 4           | OECD     | Mentions OECD                 | human rights            | "The organization adheres to OECD guidelines on human rights and responsible business."      | Entities: ["OECD", "organization"] | 0.85       |
| Report3.pdf   | 1           | UN Principles | No mentions found for UN Principles |                | "This report does not reference any UN sustainability principles."                           | No entities found                  | N/A        |

## Customizing the Standards and Keywords

To customize the sustainability standards and the related keywords, modify the `keywords` and `framework_keywords` dictionaries in the script. Each dictionary contains a set of frameworks and their respective keywords or phrases that will be searched in the PDF text.

```python
keywords = {
    'ISSB': ['ISSB Standards', 'IFRS S1', 'IFRS S2', 'ISSB Framework', 'International Sustainability Standards Board'],
    'GRI': ['GRI Standards', 'Global Reporting Initiative'],
    'TCFD': ['TCFD', 'Task Force on Climate-related Financial Disclosures'],
    'OECD': ['OECD Guidelines'],
    'UN': ['UN Principles']
}
```

For more complex frameworks, you can expand the `framework_keywords` dictionary to include additional terms or patterns relevant to the framework.

## Contributing

Contributions are welcome! If you find a bug or want to suggest an enhancement, please fork the repository, make your changes, and submit a pull request.

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Added new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.