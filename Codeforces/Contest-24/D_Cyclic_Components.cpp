#include <bits/stdc++.h>

using namespace std;
int connected = 0;
map<int, set<int>> graph;
set<int> visited;

bool isCyclic = true;
void dfs(int curr)
{
    visited.insert(curr);
    if (graph[curr].size() != 2)
        isCyclic = false;

    for (int nei : graph[curr])
    {
        if (visited.find(nei) == visited.end())
            dfs(nei);
    }
}

int main()
{
    int n, m, temp;
    cin >> n >> m;
    temp = m;
    while (temp--)
    {
        int u, v;
        cin >> u >> v;
        graph[u].insert(v);
        graph[v].insert(u);
    }
    for (int i = 1; i <= m; i++)
    {
        isCyclic = true;
        if (visited.find(i) == visited.end())
        {
            dfs(i);
            if (isCyclic)
                connected++;
        }
    }
    cout << connected << endl;
}