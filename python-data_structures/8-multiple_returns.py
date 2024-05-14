#!/usr/bin/python3

def multiple_returns(sentence):
    if not sentence:
        sentence = None
    return (len(sentence), sentence[0])
