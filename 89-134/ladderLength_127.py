class Solution:
    def ladderLength_127(self, beginWord, endWord, wordList):
        wordList = set(wordList)
        if endWord not in wordList: return 0
        use_word = {beginWord}
        cur = [[beginWord]]
        step = 0

        def findNext(word):
            ans = []
            for i in range(len(word)):
                for j in range(97, 123):
                    tmp = word[:i] + chr(j) + word[i + 1:]
                    if tmp != word and tmp in wordList and tmp not in use_word:
                        ans.append(tmp)
                        use_word.add(tmp)
            return ans

        while cur:
            cWord = cur.pop(0)
            step += 1
            next_words = []
            for i in range(len(cWord)):
                ans = findNext(cWord[i])
                next_words += ans
                if endWord in ans: return step
            if next_words:
                cur = [next_words]
        return 0
    
def main():
    beginWord = "hot"
    endWord = "dog"
    wordList = ["hot", "dog"]

    a = Solution()
    print(a.ladderLength_127(beginWord, endWord, wordList))


if __name__ == '__main__':
    main()
