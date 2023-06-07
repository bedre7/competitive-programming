#include <bits/stdc++.h>

using namespace std;
int n, m, k;
int unmarked = 0, marked = 0;
void dfs(int x, int y, vector<string> &board)
{
    if (x < 0 || x >= n || y < 0 || y >= m || board[x][y] != 'X')
        return;
    if (unmarked == marked - k)
        return;
    board[x][y] = '.';
    unmarked++;
    dfs(x + 1, y, board);
    dfs(x - 1, y, board);
    dfs(x, y + 1, board);
    dfs(x, y - 1, board);
}

int main()
{
    cin >> n >> m >> k;
    vector<string> board(n);

    for (int i = 0; i < n; i++)
        cin >> board[i];

    int x = 0, y = 0;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            if (board[i][j] == '.')
            {
                board[i][j] = 'X';
                marked++;
                x = i, y = j;
            }
        }
    }
    dfs(x, y, board);
    for (auto &row : board)
        cout << row << endl;
}