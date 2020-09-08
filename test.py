# -*- coding:utf-8 -*-
import os
import sys

#input: [0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1]
#output: 8, 4


class Solution(object):
  def getWordsChain(self, words):

    wordmap = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"
      , "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
               "u", "v", "w", "x", "y", "z"]
    reswords = []
    reswords.append(words[0])
    word = words[0]
    letter = word[-1]
    words.remove(word)
    while (len(words) > 1):
      for item in words:
        if item.startswith(letter):
          reswords.append(item)
          words.remove(item)
          letter = item[-1]
        else:
          index = wordmap.index(letter)
          if letter == "z":
            letter = "a"
          else:
            letter = wordmap[index + 1]
    return reswords
print Solution().getWordsChain(["abs", "fgg", "solute"])

