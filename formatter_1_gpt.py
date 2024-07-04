import re

# List of scriptures for matching
scripture_list = [...]  # Same list as provided before

def clean_text(text):
    """Clean and prepare the text for processing."""
    return text.replace("-", "").replace("–", "").replace("—", "").replace("\n", ",").strip()

def extract_scriptures(text):
    """Extract scriptures using regular expressions."""
    patterns = [
        r'([1-3]?\s?[a-zA-Z]+&?[a-zA-Z]+\.?\s*\d+),?',
        r'\b([1-3]?\s*[A-Za-z]+\.\s*\d+)\b',
        r'(JST\s+[1-3]?\s?[a-zA-Z]+\.?\s*(?:\d+)?)',
        r'(Section \d+ of \s?Doctrine and Covenants)'
    ]
    all_matches = []
    for pattern in patterns:
        matches = re.findall(pattern, text)
        all_matches.extend(matches)
    return all_matches

def remove_duplicates(items):
    """Remove duplicate items from a list."""
    seen = set()
    unique_items = []
    for item in items:
        if item not in seen:
            unique_items.append(item)
            seen.add(item)
    return unique_items

def process_scriptures(text):
    """Main processing function to clean text and extract scriptures."""
    cleaned_text = clean_text(text)
    scriptures = extract_scriptures(cleaned_text)
    unique_scriptures = remove_duplicates(scriptures)
    return unique_scriptures

# Example usage:
text = """ s 

 3 Nephi,  3 Ne. 8:9, 14; 9:4, 7; 10:13
 3 Nephi 9:6
 3 Nephi 8:19"""

scriptures = process_scriptures(text)
for scripture in scriptures:
    print(scripture)
#print(scriptures)
