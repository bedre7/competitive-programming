class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        reflect(matrix);
        Reverse(matrix);
    }
    void reflect(vector<vector<int>>& matrix)
    {
        for (int i = 1; i < matrix.size(); i++)
        {
            for (int j = 0; j < i; j++)
            {
                int temp = matrix[i][j];
                matrix[i][j] = matrix[j][i];
                matrix[j][i] = temp;
            }
        }
    }
    void Reverse(vector<vector<int>>& matrix)
    {
        int size = matrix.size();
        for(int k = 0; k < size; k++)
        {
            for (int i = 0, j = size - 1; i < j; i++, j--)
            {
                int temp = matrix[k][i];
                matrix[k][i] = matrix[k][j];
                matrix[k][j] = temp;
            }
        }
    }
};