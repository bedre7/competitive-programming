#include <bits/stdc++.h>

using namespace std;
map<int, set<int>> graph;
set<int> visited;
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
}