class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        # Extract x-coordinates and sort them
        x_coordinates = sorted(point[0] for point in points)

        # Calculate the maximum difference between adjacent x-coordinates
        max_width = 0
        for i in range(1, len(x_coordinates)):
            width = x_coordinates[i] - x_coordinates[i - 1]
            max_width = max(max_width, width)

        return max_width
        