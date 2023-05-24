#include <bits/stdc++.h>

using namespace std;
set<pair<int, int>> visited;
vector<vector<int>> dirs{{0, 1}, {1, 0}, {-1, 0}, {0, -1}};
bool dfs(int x, int y, vector<vector<int>> &grid)
{
    if (grid[x][y] == 2)
        return true;
    visited.insert({x, y});
    for (auto &d : dirs)
    {
        int a = x + d[0], b = y + d[1];
        if (a >= 0 && a < grid.size() && b >= 0 && b < grid[0].size() && grid[a][b] != 0 && visited.find({a, b}) == visited.end())
            if (dfs(a, b, grid))
                return true;
    }
    return false;
}
bool is_Possible(vector<vector<int>> &grid)
{
    for (int i = 0; i < grid.size(); i++)
    {
        for (int j = 0; j < grid[0].size(); j++)
        {
            if (grid[i][j] == 1)
                return dfs(i, j, grid);
        }
    }

    return false;
}
int main()
{
    int n, m;
    cin >> n >> m;
    vector<vector<int>> grid;
    for (int i = 0; i < n; i++)
    {
        vector<int> row(m);
        for (int j = 0; j < m; j++)
            cin >> row[j];
        grid.push_back(row);
    }
    if (is_Possible(grid))
        cout << 1 << endl;
    else
        cout << 0 << endl;
}