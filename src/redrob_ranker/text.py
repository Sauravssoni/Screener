import re


def normalize_text(text):
    if not text:
        return ""
    return str(text).lower()


def extract_tokens(text):
    if not text:
        return set()
    text = normalize_text(text)
    words = re.findall(r"\b\w+\b", text)
    return set(words)


def count_terms(text, terms):
    if not text:
        return 0
    text = normalize_text(text)
    count = 0
    for term in terms:
        # Precompile would be better, but we can do a simple string find if terms are distinct words
        # but boundaries matter. re.search is slow inside a loop for 100k times.
        if term in text:  # Fast pre-filter
            if re.search(r"\b" + re.escape(term) + r"\b", text):
                count += 1
    return count


def has_exact_match(text, term):
    text = normalize_text(text)
    if term not in text:
        return False
    return bool(re.search(r"\b" + re.escape(term) + r"\b", text))
