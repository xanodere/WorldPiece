from wp_algo import *
import argparse

def WordPiece(text: str,vocab_size=40)->list:
    """
    Aggregate all above functions.
    Using VOCAB_SIZE, the vocabulary's granularity can be defined
    """
    count = basic_tokenize(text)
    v0 = vocab0(count)
    words_parts = get_words_parts(count)
    while len(v0) < vocab_size:
        scores = calculate_score(words_parts, count)
        # This try block catch an error that happens when VOCAB_SIZE is too high compared to the corpus
        try:
            best_pair = max(scores, key=scores.get)
        except ValueError:
            print(f"VOCAB_SIZE is to high, maximum VOCAB_SIZE is: {len(v0)}")
            break
        lc = best_pair[0]
        rc = best_pair[1]
        words_parts = simplify_parts(best_pair, words_parts)
        tokened_part =  lc + rc[2:] if rc.startswith("##") else lc + rc 
        v0.append(tokened_part)
    v0.sort(reverse=True)
    return v0

def main():
    parser = argparse.ArgumentParser(description="Tokenize text using WordPiece algorithm")
    parser.add_argument("text", type=str, help="Text to tokenize")
    parser.add_argument("--vocab_size", type=int, help="Target vocabulary size (optional)", nargs='?')

    args = parser.parse_args()
    result = WordPiece(args.text, args.vocab_size) if args.vocab_size else WordPiece(args.text)
    print(result)
    return result

if __name__ == "__main__":
    main()