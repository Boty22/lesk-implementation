# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 23:16:40 2018

@author: LUCIA
python LESK.py <word> <sentence>
python LESK.py bank "The bank can guarantee deposits will eventually cover future tuition costs because it invests in adjustable-rate mortgage securities"
python LESK.py bank "He went fishing on the bank of the river."


"""
import sys
from nltk.corpus import wordnet as wn 
from nltk import word_tokenize
from nltk.corpus import stopwords 

def preprocess_text(sentence):

    sentence = sentence.lower()
    tokens = word_tokenize(sentence)
    filtered_words = set(tokens)
    #print(filtered_words)
    return filtered_words

def preprocess_text_non_stop(sentence):

    sentence = sentence.lower()
    tokens = word_tokenize(sentence)
    filtered_words = set([w for w in tokens if not w in stopwords.words('english')])
    #print(filtered_words)
    return filtered_words

def simp_lesk(word, sentence):
    senses_of_word = wn.synsets(word)
    best_sense = senses_of_word[0]
    max_overlap_size = 0
    context = preprocess_text(sentence)
    for sense in senses_of_word:
        print('\n________\nFor', sense,':')
        signature = preprocess_text(sense.definition()+" "+" ".join(sense.examples()))
        overlap = context.intersection(signature)
        overlap_size = len(overlap)
        #Prnting part:
        #print('\n*********\nFor', sense,':')
        print('gloss:', sense.definition())
        #print(signature)
        #print(context)
        print('Overlap:', end='')
        print(overlap)
        if overlap_size > max_overlap_size:
            max_overlap_size = overlap_size
            best_sense = sense
    print('\n******\nResult:\n******\nSynset selected:', best_sense)
    print('gloss selected:',best_sense.definition())
    return

def simp_lesk_non_stop(word, sentence):
    senses_of_word = wn.synsets(word)
    best_sense = senses_of_word[0]
    max_overlap_size = 0
    context = preprocess_text_non_stop(sentence)
    for sense in senses_of_word:
        print('\n________\nFor', sense,':')
        signature = preprocess_text_non_stop(sense.definition()+" "+" ".join(sense.examples()))
        overlap = context.intersection(signature)
        overlap_size = len(overlap)
        #Prnting part:
        #print('\n*********\nFor', sense,':')
        print('gloss:', sense.definition())
        #print(signature)
        #print(context)
        print('Overlap:', end='')
        print(overlap)
        if overlap_size > max_overlap_size:
            max_overlap_size = overlap_size
            best_sense = sense
    print('\n******\nResult:\n******\nSynset selected:', best_sense)
    print('gloss selected:',best_sense.definition())
    return


def main():
    word = sys.argv[1]
    sentence = sys.argv[2]
    print('The word is:', word)
    print('The sentence is:', sentence)
    #simp_lesk(word, sentence)
    simp_lesk_non_stop(word, sentence)


main()