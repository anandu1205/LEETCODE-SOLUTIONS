from typing import List
from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0
        
        queue = deque([(beginWord, 1)])  # (word, steps)
        
        while queue:
            word, steps = queue.popleft()
            
            if word == endWord:
                return steps
            
            for i in range(len(word)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    new_word = word[:i] + c + word[i+1:]
                    
                    if new_word in wordSet:
                        queue.append((new_word, steps + 1))
                        wordSet.remove(new_word)  # mark visited
        
        return 0