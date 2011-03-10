Markov Sentence Generator
=========================

This program generates a sentence's worth of "real-looking" text using a Markov model and sample textual training input.  Given some sample text from which to build a model, the program prints out a sentence based on a Markov chain.  Use it thus:

`$ ./sentence-generator.py  filename  [chain length]`

where `filename` is a file containing some training text for the sentence to imitate (one of Project Gutenberg's books fits the bill nicely) and `chain length` optionally represents the number of words taken into account when choosing the next word.  Chain length defaults to 1 (which is fastest), but increasing this may generate more realistic text, albeit slightly more slowly.  Depending on the text, increasing the chain length past 6 or 7 words probably won't do much good -- at that point you're usually plucking out whole sentences anyway, so using a Markov model is kind of redundant.

The texts of *Portrait of the Artist as a Young Man* and *Leaves of Grass* (in `snippet.txt`) are taken from Project Gutenberg.  The usual copyright headers had to be removed so that they could serve as useful sample input, but naturally all the rights and restrictions of a Gutenberg book still apply.
