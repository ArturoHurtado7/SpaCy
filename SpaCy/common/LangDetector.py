import spacy
from spacy.language import Language
from spacy_langdetect import LanguageDetector
"""
nlp = spacy.load("en_core_web_sm")
doc = nlp("Apple is looking at buying U.K. startup for $1 billion")

for token in doc:
    print('text:', token.text) # Text: The original word text.
    print('lemma:', token.lemma_) # Lemma: The base form of the word.
    print('pos:', token.pos_) # POS: The simple UPOS part-of-speech tag.
    print('tag:', token.tag_) # Tag: The detailed part-of-speech tag.
    print('dep:', token.dep_) # Dep: Syntactic dependency, i.e. the relation between tokens.
    print('shape:', token.shape_) # Shape: The word shape – capitalization, punctuation, digits.
    print('is_alpha:', token.is_alpha) # is alpha: Is the token an alpha character?
    print('is_stop:', token.is_stop) # is stop: Is the token part of a stop list, i.e. the most common words of the language?
    print('*'*10)

for ent in doc.ents:
    print('text:', ent.text) # Text: The original entity text.
    print('start_char:', ent.start_char) # Start: Index of start of entity in the Doc.
    print('end_char:', ent.end_char) # End: Index of end of entity in the Doc.
    print('label_:', ent.label_) # Label: Entity label, i.e. type.
    print('*'*10)"""


"""
nlp = spacy.load("en_core_web_md")
tokens = nlp("dog cat banana afskfsd")

for token in tokens:
    print('text:', token.text) # Text: The original token text.
    print('has_vector:', token.has_vector) # has vector: Does the token have a vector representation?
    print('vector_norm:', token.vector_norm) # Vector norm: The L2 norm of the token’s vector (the square root of the sum of the values squared)
    print('is_oov:', token.is_oov) # OOV: Out-of-vocabulary
    print('*'*10)

doc1 = nlp("I like salty fries and hamburgers.")
doc2 = nlp("Fast food tastes very good.")

# Similarity of two documents
print(doc1, "<->", doc2, doc1.similarity(doc2))
# Similarity of tokens and spans
french_fries = doc1[3].lex
print(french_fries)
burgers = doc1[5]
print(burgers)
print(french_fries, "<->", burgers, french_fries.similarity(burgers))"""


def get_lang_detector(nlp, name):
    return LanguageDetector()

nlp = spacy.load("en_core_web_lg")
Language.factory("language_detector", func=get_lang_detector)
nlp.add_pipe('language_detector', last=True)
doc = nlp("You know I got a lot to say, all these voices in the background of my brain, Y me dicen todo lo que estás pensando")
print(doc._.language)

"""
for token in doc:
    print('text:', token.text) # Text: The original token text.
    print('has_vector:', token.has_vector) # has vector: Does the token have a vector representation?
    print('vector_norm:', token.vector_norm) # Vector norm: The L2 norm of the token’s vector (the square root of the sum of the values squared)
    print('is_oov:', token.is_oov) # OOV: Out-of-vocabulary
    print('*'*10)"""

print(doc.ents)

for ent in doc.ents:
    print('text:', ent.text) # Text: The original entity text.
    print('start_char:', ent.start_char) # Start: Index of start of entity in the Doc.
    print('end_char:', ent.end_char) # End: Index of end of entity in the Doc.
    print('label_:', ent.label_) # Label: Entity label, i.e. type.
    print('*'*10)