# An implementation of the WorldPiece algorithm
The goal is to create a WordPiece(text) function which takes as input a string representing the corpus and outputs the tokens vocabulary using the WordPiece Algorithm.
The algorithm can be defined as follows:

    - Trivial word pre-tokenization of the corpus 
    - Initial V0 vocabulary generation  
    - As a first iteration, we associate to each word a list of it's chars (apple : [a, ##p, ##p, ##l, ##e]
    - We simplify trough merges the chars list using a score method (score = freq_of_pairs/freq_first_element*freq_second_element)
    - The end condition of the algorithm is the size of the constituted vocabulary (size_vocab = size_V0 + simplified tokens)

This repo contains a notebook and its html report in addition of the python project.

### Execution
This repo is provided with a virtual environment.</br>
Please use this command to execute the script in the root of the project.

```bash
python main.py text [--vocab_size]
```

for exemple:</br>
python main.py "word pre-tokenization of the corpus" --vocab_size 35</br>
python main.py "word pre-tokenization of the corpus"

As long as the input text is longer, the relevance of the WordPiece algorithm will be more visible.


HADDOU Younes
