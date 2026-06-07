import argparse
from scraper import scrape_url, scrape_text
from extractor import extract_data
from exporter import export_to_csv, export_to_json

def process_urls(urls: list[str], fields: list[str]) -> list[dict]:
    results = []
    for url in urls:
        print(f"Scraping: {url}")
        try:
            text = scrape_url(url)
            data = extract_data(text, fields)
            data["source"] = url
            results.append(data)
            print(f"Extracted: {data}")
        except Exception as e:
            print(f"Error scraping {url}: {e}")
            results.append({"source": url, "error": str(e)})
    return results

def process_text(text: str, fields: list[str]) -> dict:
    cleaned = scrape_text(text)
    return extract_data(cleaned, fields)

def main():
    parser = argparse.ArgumentParser(description="AI Data Extraction Agent")
    parser.add_argument("--urls", nargs="+", help="URLs to scrape")
    parser.add_argument("--text", type=str, help="Raw text to extract from")
    parser.add_argument("--fields", nargs="+", required=True, help="Fields to extract")
    parser.add_argument("--format", choices=["csv", "json", "both"], default="both")
    args = parser.parse_args()

    if args.urls:
        results = process_urls(args.urls, args.fields)
    elif args.text:
        result = process_text(args.text, args.fields)
        results = [result]
    else:
        print("Error: provide --urls or --text")
        return

    if args.format in ("csv", "both"):
        export_to_csv(results)
    if args.format in ("json", "both"):
        export_to_json(results)

if __name__ == "__main__":
    main()
