'''------------------------Stage 1/5: Preprocess the text corpus----------------------------------'''
import random
import nltk

from collections import  Counter
#nltk.download("punkt")
from nltk.tokenize import regexp_tokenize
filepath = input()
#filepath = "C:\\Users\\savad\\Downloads\\corpus.txt"


list_word = []
regexp = r"\S+"
with open(filepath, 'r', encoding="utf-8") as corpus:
    corpus = corpus.readlines()
    for line in corpus:
        list_word += regexp_tokenize(line, regexp)

# print("Corpus statistics")
# print("All tokens: ", len(list_word))
# print("Unique tokens: ", len(set(list_word)))

# x = input()
#
# while x != "exit":
#     try:
#         print(list_word[int(x)])
#     except TypeError:
#         print("Type Error. Please input an integer.")
#     except ValueError:
#         print("Type Error. Please input an integer.")
#     except IndexError:
#         print("Index Error. Please input an integer that is in the range of the corpus.")
#     x = input()
# quit()


'''................................Stage 2/5: Break the dataset into bigrams........'''

'''a bigram is a sequence ot two adjacent tokens '''

# bigram_list = []
#
# for head in range(0, len(list_word) - 1):
#     for tail in range(1, len(list_word)):
#         if head != tail:
#             bigram_list.append((list_word[head], list_word[tail]))

bigrams = list(nltk.bigrams(list_word))

bigramsv2 = [f"Head: {x[0]} Tail: {x[1]}" for x in bigrams]
#print(f"Number of bigrams: {len(bigrams)}")
# user_input = input()
# while user_input != "exit":
#     try:
#         print(bigramsv2[int(user_input)])
#     except TypeError:
#         print("Type Error. Please input an integer.")
#     except ValueError:
#         print("Type Error. Please input an integer.")
#     except IndexError:
#         print("Index Error. Please input a value that is not greater than the number of all bigrams.")
#     user_input = input()
# quit()


'''------------------------------------------STAGE 3/5:CREATE A MARKOV CHAIN MODEL---------------------------------------'''


#print(bigrams[0:10])
# list of heads

list_heads = set([x[0] for x in bigrams])

# dictionary containing head and the list of corresponding tails

head_dict = {}

for el in bigrams:
    head_dict.setdefault(el[0], []).append(el[1])


# creating the dictionary of heads and tails and their corresponding occurrences
count_dict = {}

for head in head_dict.keys():
    count_dict[head] = Counter(head_dict[head])
    #count_dict[head] = Counter(head_dict[head]).most_common()


# user_input = input("Enter ")
#
# while user_input != "exit":
#     print(f"Head: {user_input}")
#     try:
#         for key, value in count_dict[user_input]:
#             print(f"Tail: {key}\tCount: {value}")
#     except KeyError:
#         print("Key Error. The requested word is not in the model. Please input another word.")
#
#     user_input = input("Enter again ")
# quit()

'''---------------------------------------------------------------STAGE 4/5: GENERATE RANDOM TEXT---------------------------'''


# Choose a random word from the corpus and then generate 10 sentences with a  length of 10 words for each sentence
# rd_word = random.choice(list_word)
# list_sents = 0
# while list_sents < 10:
#     sentence = []
#     rd_word_1 = rd_word
#     while len(sentence) < 10:
#         pop = list(count_dict[rd_word].keys())
#         weights = list(count_dict[rd_word].values())
#         sentence.append(random.choices(population=pop, weights = weights)[0])
#         rd_word_1 = sentence[-1]
#     print(" ".join(sentence))
#     list_sents += 1
#     rd_word = sentence[-1]


'''----------------------------------STAGE 5/5: GENERATE FULL SENTENCES----------------------------------------------------------'''

def punc_start(x):
    ponc = ["!", "?", ".", ";"]
    sum = 0
    for p in ponc:
        if x.startswith(p)==True or x.endswith(p):
            sum += 1
    return sum == 0

def punc_ends(x):
    ponc = ["!", "?", ".", ";"]
    sum = 0
    for p in ponc:
        if x.endswith(p)==True:
            sum += 1
    return sum == 0





for _ in range(10):
    st_word = random.choice(list_word)
    sentence = []
    while st_word.capitalize() != st_word or punc_start(st_word) == False:
            st_word = random.choice(list_word)


    sentence.append(st_word)

    while len(sentence) < 5 or punc_ends(sentence[-1]) ==True:
            pop = list(count_dict[sentence[-1]].keys())
            weights = list(count_dict[sentence[-1]].values())
            sentence.append(random.choices(population=pop, weights = weights)[0])

    print(" ".join(sentence))