from sentence_transformers import SentenceTransformer
import numpy as np

words = [w.strip() for w in open('./legal-words.txt', 'r').readlines()]
# print(list(zip([1, 2, 3], ['a', 'b', 'c'])))
    
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
embeddings = list(zip(words, model.encode(words)))

def translate_word(word):
    new_embed = model.encode(word)
    highest_sim = -float('inf')
    most_similar_word = ""

    for w, e in embeddings:
        dot_product = np.dot(e, new_embed)
        normA = np.linalg.norm(e)
        normB = np.linalg.norm(new_embed)
        sim = dot_product / (normA * normB);


        if sim > highest_sim:
            highest_sim = sim
            most_similar_word = w
    
    return most_similar_word

    

# print(embeddings)
while True:
    sentence = input('Enter Sentence To Translate: ')
    translated_sentence = ""
    for w in sentence.split():
        translated_sentence += " " + translate_word(w)
    
    print(translated_sentence)

