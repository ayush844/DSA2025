class Solution {

    class NodeWithDist{
        public int row;
        public int col;
        public int dist;

        public NodeWithDist(int row, int col, int dist) {
            this.row = row;
            this.col = col;
            this.dist = dist;
        }

        public int getFirst(){
            return row;
        }

        public int getSecond(){
            return col;
        }

        public int getThird(){ return dist; }
    }


    public int[][] updateMatrix(int[][] mat) {
        int n = mat.length;
        int m = mat[0].length;

        int vis[][] = new int[n][m];
        int dist[][] = new int[n][m];

        Queue<NodeWithDist> q = new LinkedList<>();

        for (int i = 0; i < n; i++){
            for (int j = 0; j < m; j++){
                if (mat[i][j] == 0){
                    q.add(new NodeWithDist(i, j, 0));
                    vis[i][j] = 1;
                }else{
                    vis[i][j] = 0;
                }
            }
        }

        int delRow[] = {-1, 0, 1, 0};
        int delCol[] = {0, -1, 0, 1};

        while (!q.isEmpty()){
            int row = q.peek().getFirst();
            int col = q.peek().getSecond();
            int step = q.peek().getThird();

            q.remove();

            dist[row][col] = step;


            for (int i = 0; i < 4; i++){
                int nrow = row + delRow[i];
                int ncol = col + delCol[i];

                if (nrow>=0 && nrow<n && ncol>=0 && ncol<m && vis[nrow][ncol] == 0){
                    vis[nrow][ncol] = 1;
                    q.add(new NodeWithDist(nrow, ncol, step + 1));
                }
            }

        }
        
        return dist;
    }
}