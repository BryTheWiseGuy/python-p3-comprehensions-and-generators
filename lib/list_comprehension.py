#!/usr/bin/env python3

def return_evens(num_list):
    even_num_list = [n for n in num_list if n % 2 == 0]
    return even_num_list

def make_exclamation(sentence_list):
    exclamation_sentence_list = [f"{str}!" for str in (sentence_list)]
    return exclamation_sentence_list