class Solution:
    def encode(self, strs: List[str]) -> str:
        result = ""
        #loop through the words and adds the length of the word, and # and the word
        for word in strs:
            #turn into string
            result += str(len(word)) + "#" + word

        return result

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        #loop till end of string
        while i < len(s):
            j = i
            #loop till we find a hashtag
            while s[j] != "#":
                j += 1

            #get the length number before the hashtag
            length = int(s[i:j])

            #word starts right after the hashtag
            wordStart = j + 1
            wordEnd = wordStart + length

            #add the original word back into result
            result.append(s[wordStart:wordEnd])

            #move i to the start of the next encoded word
            i = wordEnd

        return result