from collections import Counter

def basic_tokenize(text:str) -> dict:
    """
    Pre-tokenization
    """
    corpus = []

    tokens = text.split()
    token_counts = Counter(tokens)

    return token_counts

def vocab0(count: dict) -> list:
    """
    Generate a initial vocabulary 
    """
    v0 = []
    for word in count.keys():
        if word[0] not in v0:
            v0.append(word[0])
        for letter in word[1:]:
            if f"##{letter}" not in v0:
                v0.append(f"##{letter}")
    v0.sort()
    return v0

def get_words_parts(count: dict) -> dict:
    """
    Assotiate each word with its parts
    """
    words_parts = {}
    for word in count.keys():
        parts=[]
        for a,b in enumerate(word):
            # words_parts[word] = b if a != 0 else f"##{b}"
            parts.append(b if a == 0 else f"##{b}")
        words_parts[word] = parts
    return words_parts

def calculate_score(parts: dict, count: dict)-> dict:
    """
    calculate scores for the paires
    """
    letter_freqs = {}
    pair_freqs = {}
    for word, freq in count.items():
        part = parts[word]
        if len(part) == 1:
            letter_freqs[part[0]] = letter_freqs.get(part[0], 0) + freq
            continue
        for i in range(len(part) - 1):
            pair = (part[i], part[i + 1])
            letter_freqs[pair[0]] = letter_freqs.get(pair[0], 0) + freq
            letter_freqs[pair[1]] = letter_freqs.get(pair[1], 0) + freq
            pair_freqs[pair] = pair_freqs.get(pair, 0) + freq


    scores = {
        pair: freq / (letter_freqs[pair[0]] * letter_freqs[pair[1]])
        for pair, freq in pair_freqs.items()
    }
    return scores

def simplify_parts(pair: tuple, words_parts: dict)-> dict:
    """
    Simplify parts list
    """
    lc = pair[0]
    rc = pair[1]
    for word, part in words_parts.items():
        if len(part) == 1:
            continue
        for i in range(len(part)-1):
            if part[i] == lc and part[i + 1] == rc:
                simplified = lc + rc[2:] if rc.startswith("##") else lc + rc 
                part[i:i+2] = [simplified]  
        words_parts[word] = part
    return words_parts
