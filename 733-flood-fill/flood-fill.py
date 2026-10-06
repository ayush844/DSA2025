class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        original = image[sr][sc]
        row_len = len(image)
        col_len = len(image[0])

        if original == color:
            return image

        def dfs(row, col):
            if row < 0 or row >= row_len or col < 0 or col >= col_len:
                return False
            
            if image[row][col] != original:
                return

            image[row][col] = color

            dfs(row+1, col)
            dfs(row-1, col)
            dfs(row, col+1)
            dfs(row, col-1)

        dfs(sr, sc)

        return image