class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        maxi = sm = sum(cardPoints[:k])
        for i in range(k-1, -1, -1):
            sm -= cardPoints[i]
            sm += cardPoints[i-k]
            maxi = max(maxi, sm)
        return maxi
        # elif cardPoints[0]>
            