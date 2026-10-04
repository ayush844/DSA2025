class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        original = image[sr][sc]
        if original == color:
            return image
        
        rows = len(image)
        columns = len(image[0])

        def dfs(row, col):
            if row < 0 or row >= rows or col < 0 or col >= columns:
                return

            if image[row][col] != original:
                return

            image[row][col] = color

            dfs(row+1, col)
            dfs(row-1, col)
            dfs(row, col+1)
            dfs(row, col-1)

        dfs(sr, sc)

        return image