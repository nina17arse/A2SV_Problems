class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        targetInt=ord(target)
        for i in range(len(letters)):
            if ord(letters[i]) > targetInt:
                return letters[i]
        
        return letters[0]