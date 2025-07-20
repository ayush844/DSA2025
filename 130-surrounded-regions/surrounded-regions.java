class Solution {

    public void dfs3(int row, int col, int[][] vis, char[][] borad, int[] delRow, int[] delCol){

        vis[row][col] = 1;
        int n = borad.length;
        int m = borad[0].length;

        for (int i = 0; i < 4; i++){
            int nrow = row + delRow[i];
            int ncol = col + delCol[i];

            if (nrow>=0 && nrow<n && ncol>=0 && ncol<m && vis[nrow][ncol]==0 && borad[nrow][ncol]=='O'){
                dfs3(nrow, ncol, vis, borad, delRow, delCol);
            }
        }

    }

    public void solve(char[][] board) {
        int n = board.length;
        int m = board[0].length;

        int[][] vis = new int[n][m];

        int[] delRow = {-1, 0, 1, 0};
        int[] delCol = {0, -1, 0, 1};

        for (int j = 0; j < m; j++){
            if (vis[0][j] == 0 && board[0][j] == 'O'){
                dfs3(0, j, vis, board, delRow, delCol);
            }

            if (vis[n-1][j] == 0 && board[n-1][j] == 'O'){
                dfs3(n-1, j, vis, board, delRow, delCol);
            }
        }


        for (int i = 0; i < n; i++){
            if (vis[i][0] == 0 && board[i][0] == 'O'){
                dfs3(i, 0, vis, board, delRow, delCol);
            }

            if (vis[i][m-1] == 0 && board[i][m-1] == 'O'){
                dfs3(i, m-1, vis, board, delRow, delCol);
            }
        }


        for (int i = 0; i < n; i++){
            for (int j = 0; j < m; j++){
                if(vis[i][j] == 0 && board[i][j] == 'O'){
                    board[i][j] = 'X';
                }
            }
        }
    }
}