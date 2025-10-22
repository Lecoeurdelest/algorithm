class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        list = []
        for index, str in enumerate(words):
            if x in str:
                list.append(index)
        return list