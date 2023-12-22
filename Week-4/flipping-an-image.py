class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        col=len(image[0])
        for r in range(len(image)):
            row=image[r]
            reversedMat=row[::-1]
            image[r]=reversedMat
            for c in range(col):
                if image[r][c]==0:
                    image[r][c]=1
                elif image[r][c]==1:
                    image[r][c]=0
        return image
        
        