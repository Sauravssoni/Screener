import re

def normalize_text(text):
    if not text:
        return ""
    return str(text).lower()

def extract_tokens(text):
    if not text:
        return set()
    text = normalize_text(text)
    words = re.findall(r'\b\w+\b', text)
    return set(words)

def count_terms(text, terms):
    text = normalize_text(text)
    count = 0
    for term in terms:
        if re.search(r'\b' + re.escape(term) + r'\b', text):
            count += 1
    return count

def has_exact_match(text, term):
    text = normalize_text(text)
    return bool(re.search(r'\b' + re.escape(term) + r'\b', text))
