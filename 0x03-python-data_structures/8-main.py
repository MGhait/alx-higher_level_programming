#!/usr/bin/python3
multiple_returns = __import__('8-multiple_returns').multiple_returns

sentence = "At school, I learnt C!"
i2 = ''
length, first = multiple_returns(sentence)
len1, first1 = multiple_returns(i2)
print("Length: {:d} - First character: {}".format(length, first))
print("Length: {:d} - First character: {}".format(len1, first1))
