# compare/utils.py
import re
from difflib import SequenceMatcher

def count_special_characters(code):
    special_characters = {
        '<': 0,
        '>': 0,
        '/': 0,
        ';': 0,
    }
    
    for char in code:
        if char in special_characters:
            special_characters[char] += 1
            
    return special_characters

def count_keywords(code):
    keywords = ['const', 'int', 'char']
    keyword_count = {keyword: len(re.findall(r'\b' + re.escape(keyword) + r'\b', code)) for keyword in keywords}
    return keyword_count

def count_whitespace_patterns(code):
    # Count spaces between words
    words = re.findall(r'\S+', code)  # Find all non-whitespace sequences
    if len(words) < 2:
        return 0  # No spaces if there are fewer than 2 words
    spaces_between_words = len(words) - 1
    return spaces_between_words

def compare_code(user_code, stored_code):
    # Initial score (scaled to 100)
    score = 100
    
    # Normalize and simplify code for a fair comparison
    user_code_normalized = user_code.strip().lower()
    stored_code_normalized = stored_code.strip().lower()
    
    # 1. Code Similarity (using SequenceMatcher)
    similarity_ratio = SequenceMatcher(None, user_code_normalized, stored_code_normalized).ratio()
    score *= similarity_ratio  # Adjust score based on overall similarity
    
    # 2. Keyword Comparison
    user_keywords = count_keywords(user_code_normalized)
    stored_keywords = count_keywords(stored_code_normalized)
    
    keyword_penalty = 0
    total_keywords = len(stored_keywords)
    
    for keyword in user_keywords:
        difference = abs(user_keywords[keyword] - stored_keywords[keyword])
        keyword_penalty += difference
        
    if total_keywords > 0:
        keyword_penalty /= total_keywords  # Calculate average keyword difference

    score -= (keyword_penalty * 10)  # Adjust score by keyword differences

    # 3. Special Character Comparison
    user_special_chars = count_special_characters(user_code_normalized)
    stored_special_chars = count_special_characters(stored_code_normalized)
    
    special_char_penalty = 0
    total_special_chars = len(stored_special_chars)
    
    for char in user_special_chars:
        difference = abs(user_special_chars[char] - stored_special_chars[char])
        special_char_penalty += difference
        
    if total_special_chars > 0:
        special_char_penalty /= total_special_chars

    score -= (special_char_penalty * 5)  # Adjust score by special char differences

    # 4. Whitespace patterns
    user_spaces = count_whitespace_patterns(user_code_normalized)
    stored_spaces = count_whitespace_patterns(stored_code_normalized)
    
    space_penalty = abs(user_spaces - stored_spaces)
    
    score -= (space_penalty * 2)  # Penalize for whitespace differences
    
    # 5. Correct the scoring with number of lines
    user_lines = user_code_normalized.strip().splitlines()
    stored_lines = stored_code_normalized.strip().splitlines()

    line_differences = abs(len(user_lines) - len(stored_lines))

    score -= (line_differences * 3)
    
    # Ensure score is within range
    score = max(1, min(score, 100))
    
    return {
        'score': int(score),  # Return score as an integer
    }
