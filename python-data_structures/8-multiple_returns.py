#!/usr/bin/python3

def multiple_returns(sentence):
    if not sentence:
        return(0, None)
    return (len(sentence), sentence[0])

sentence = ""
length, first = multiple_returns(sentence)
print("Length: {:d} - First character: {}".format(length, first))