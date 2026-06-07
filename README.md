# AI Data Extraction Agent

An AI-powered agent that scrapes web pages or processes raw text and extracts structured data using LLM. Results are saved as CSV and JSON.

## How It Works

1. Provide URLs or raw text
2. Specify the fields you want to extract
3. Agent scrapes and processes the content
4. Structured data is saved to output files

## Tech Stack

- Python
- BeautifulSoup4 (web scraping)
- Groq API (llama-3.1-8b-instant)
- Pandas (CSV export)

## Setup

1. Clone the repository
2. Install dependencies:
pip install -r requirements.txt
3. Create `.env` file:
GROQ_API_KEY=your_groq_api_key

## Usage

Extract data from URLs:
python main.py --urls "https://example.com" --fields "title" "price" "date" --format json

Extract data from raw text:
python main.py --text "Your text here" --fields "name" "email" "phone" --format csv

## Output formats

- `--format json` — saves to output/output.json
- `--format csv` — saves to output/output.csv
- `--format both` — saves both formats