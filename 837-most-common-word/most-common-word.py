class Solution:
    def mostCommonWord(self, paragraph, banned):
        banned = set(banned)

        for ch in "!?',;.":
            paragraph = paragraph.replace(ch, " ")

        words = paragraph.lower().split()

        freq = {}

        for word in words:
            if word not in banned:
                freq[word] = freq.get(word, 0) + 1

        return max(freq, key=freq.get)