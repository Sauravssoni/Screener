import re

def normalize_text(text):
    if not text:
        return ""
    return str(text).lower()

def extract_tokens(text):
    if not text:
        return set()
    text = normalize_text(text)
    words = re.split(r'\W+', text)
    return set(words)

def count_terms(text, terms):
    if not text:
        return 0
    text_lower = " " + normalize_text(text) + " "
    count = 0
    for term in terms:
        # Fast string search instead of regex
        if f" {term} " in text_lower or f" {term}" in text_lower or f"{term} " in text_lower:
            count += 1
    return count

def has_exact_match(text, term):
    if not text:
        return False
    text_lower = " " + normalize_text(text) + " "
    return f" {term} " in text_lower
