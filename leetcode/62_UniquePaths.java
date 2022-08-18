import java.util.Arrays;

class Solution {
    
    public int uniquePaths(int m, int n) {
        int[][] visited = new int[m][n];
        Arrays.stream(visited).forEach(a -> Arrays.fill(a, 1));
        for(int i=1; i<m; i++){
            for(int j=1; j<n; j++){
                visited[i][j] = visited[i-1][j] + visited[i][j-1];
            }
        }
        
        return visited[m-1][n-1];
    }
}