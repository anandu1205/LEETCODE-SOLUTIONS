class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lowercase='abcdefghijklmnopqrstuvwxyz'
        uppercase='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        dict={}
        visited=set()
        length=len(lowercase)
        for i in range(length):
            dict[lowercase[i]]=uppercase[i]
        special=0
        for i in range(len(word)):
            if word[i] in lowercase and dict[word[i]] in word and  word[i] not  in visited:
                special+=1
                visited.add(word[i])
        return special
        