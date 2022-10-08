class Solution {
    public int[][] generateMatrix(int n) {
        int[][] matrix = new int[n][n];
        int left = 0, right = n - 1, up = 0, down = n - 1;
        int value = 1;
        
        while (left <= right)
        {
            //going to the right
            for (int i = left; i <= right; i++)
                matrix[up][i] = value++;

            up++;
            //going down
            for (int i = up; i <= down; i++)
                matrix[i][right] = value++;

            right--;
            //going to the left
            for (int i = right; i >= left; i--)
                matrix[down][i] = value++;
            down--;
            
            //going up
            for (int i = down; i >= up; i--)
                matrix[i][left] = value++;
            left++;
        }
        return matrix;
    }
}