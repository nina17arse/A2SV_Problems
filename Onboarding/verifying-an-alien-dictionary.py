class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_map = {}
        for i, letter in enumerate(order):
            order_map[letter] = i + 1

        for i in range(1, len(words)):
            prev_word = words[i - 1]
            curr_word = words[i]

            for j in range(len(prev_word)):
                if j >= len(curr_word):
                    return False

                prev_letter = prev_word[j]
                curr_letter = curr_word[j]

                if order_map[prev_letter] > order_map[curr_letter]:
                    return False
                elif order_map[prev_letter] < order_map[curr_letter]:
                    break

        return True

        

            
            