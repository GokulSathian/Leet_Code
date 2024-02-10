class Solution:
    def groupAnagrams(self, strs):
        anagram_map=collections.defaultdict(list)
        for word in strs:
            letter_collection=[0]*26
            for letter in word:
                letter_collection[ord(letter)-ord('a')]+=1

            anagram_map[tuple(letter_collection)].append(word)
        return anagram_map.values()
