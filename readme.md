
# Sustainability PDF Analysis

This project is designed to analyze sustainability-related content in PDF documents by searching for specific frameworks and standards such as ISSB, GRI, TCFD, OECD, and UN Principles. It uses a combination of basic keyword matching and advanced contextual analysis based on sentence embeddings to identify relevant sections of the PDFs and provide detailed results.

## Features

- Extracts text from PDF documents using two methods: `pdfplumber` and `PyPDF2`.
- Searches for sustainability-related frameworks and standards within the text.
- Performs basic keyword matching to find relevant sentences.
- Uses advanced contextual matching with sentence embeddings to measure similarity between sentences and keywords.
- Extracts entities related to sustainability or business (e.g., organizations, geographical locations) from the text using spaCy.
- Outputs results in a detailed and structured format, including a CSV file for easy analysis.

## Requirements

To run this project, you'll need the following Python packages:

- `pdfplumber` for extracting text from PDFs.
- `spacy` for natural language processing and entity extraction.
- `PyPDF2` for PDF text extraction.
- `sentence-transformers` for advanced contextual matching with sentence embeddings.
- `pandas` for organizing and displaying the results in a structured format.

You can install the required dependencies using `pip`:

```bash
pip install pdfplumber spacy PyPDF2 sentence-transformers pandas
```

Additionally, you will need to download the spaCy model for natural language processing:

```bash
python -m spacy download en_core_web_sm
```

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/sustainability-pdf-analysis.git
   cd sustainability-pdf-analysis
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Download the spaCy model:

   ```bash
   python -m spacy download en_core_web_sm
   ```

## Usage

1. Place the PDFs you want to analyze in the project directory.
   
2. Update the `pdf_paths` list in the script to include the paths to the PDF files you want to analyze.

3. Run the script:

   ```bash
   python analyze_pdfs.py
   ```

   The script will process the PDFs and display the results in a tabular format in the console.

4. A CSV file (`sustainability_analysis.csv`) will be generated containing the detailed results of the analysis, including:

   - The PDF file name and page number.
   - The framework or standard (e.g., ISSB, GRI, TCFD, OECD, UN Principles).
   - Whether any mentions of the standard were found.
   - The sentence containing the keyword or framework.
   - Contextual matching details with sentence similarity.
   - Basic keyword matching results.

## Example Output

Here is an example of how the output might look in the CSV file:

| File           | Page Number | Standard  | Description                           | Evidence              | Sentence                                           | Contextual Matches                                              | Basic Matches                           |
|----------------|-------------|-----------|---------------------------------------|-----------------------|---------------------------------------------------|----------------------------------------------------------------|----------------------------------------|
| Report1.pdf    | 1           | ISSB      | Mentions ISSB                         | ISSB Standards        | "The ISSB Standards provide guidelines..."      | {'Framework': 'ISSB', 'Sentence': 'The ISSB Standards provide...', 'Context': 'Entities: [ISSB, Finance]', 'Similarity': 0.75} | [{'Framework': 'ISSB', 'Sentence': 'The ISSB Standards provide...', 'Context': 'No additional context', 'Similarity': 'N/A'}] |
| Report2.pdf    | 2           | GRI       | Mentions GRI                          | GRI Standards         | "According to the GRI Standards, businesses..." | {'Framework': 'GRI', 'Sentence': 'According to the GRI Standards...', 'Context': 'Entities: [GRI, Stakeholders]', 'Similarity': 0.80} | [{'Framework': 'GRI', 'Sentence': 'According to the GRI Standards...', 'Context': 'No additional context', 'Similarity': 'N/A'}] |
| Report3.pdf    | 3           | OECD      | No mentions found for OECD            |                       | "No relevant content found"                    |                                                                |                                        |

## Contributing

If you would like to contribute to this project, feel free to fork the repository and submit a pull request. Here are a few ways you can contribute:

- Improve the accuracy of the keyword matching and contextual analysis.
- Add support for additional sustainability standards and frameworks.
- Improve performance when processing large PDFs.
- Provide better handling for edge cases or errors during PDF extraction.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [pdfplumber](https://github.com/jsvine/pdfplumber) for PDF text extraction.
- [spaCy](https://spacy.io/) for natural language processing.
- [sentence-transformers](https://www.sbert.net/) for advanced contextual sentence matching.
- [PyPDF2](https://pythonhosted.org/PyPDF2/) for PDF text extraction.
- [pandas](https://pandas.pydata.org/) for data manipulation and analysis.
```

### Key Sections Explained:

1. **Introduction**: Briefly explains the purpose of the project, which is to analyze sustainability-related content in PDFs using keyword and contextual matching.
  
2. **Requirements**: Lists the necessary Python packages and provides installation commands.

3. **Setup**: Instructions on cloning the repository, installing dependencies, and setting up the spaCy model.

4. **Usage**: Details on how to use the script, including how to run the analysis and where to find the output.

5. **Example Output**: Provides an example of how the results will appear, including both basic keyword matches and contextual sentence matching.

6. **Contributing**: Encourages others to contribute to the project by improving features or fixing bugs.

7. **License**: Specifies that the project is licensed under the MIT License.

8. **Acknowledgments**: Credits the libraries and tools used in the project. 
