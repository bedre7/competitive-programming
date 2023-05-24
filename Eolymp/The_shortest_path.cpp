#include <bits/stdc++.h>

using namespace std;
map<int, vector<int>> graph;
map<int, int> prevs;

vector<int> makePath(int dest)
{
    vector<int> path;
    path.push_back(dest);
    while (prevs.find(dest) != prevs.end())
    {
        dest = prevs[dest];
        path.push_back(dest);
    }
    reverse(path.begin(), path.end());
    return path;
}

vector<int> bfs(int a, int b, int n)
{
    vector<int> visited(n + 1, false);
    queue<int> q;
    q.push(a);
    visited[a] = true;

    while (!q.empty())
    {
        int c = q.front();
        q.pop();
        if (c == b)
            return makePath(c);

        for (auto &d : graph[c])
        {
            if (!visited[d])
            {
                prevs[d] = c;
                visited[d] = true;
                q.push(d);
            }
        }
    }
    return {};
}
int main()
{

    int n, m, a, b, u, v;
    cin >> n >> m;
    cin >> a >> b;

    while (m--)
    {
        cin >> u >> v;
        graph[u].push_back(v);
        graph[v].push_back(u);
    }

    vector<int> path = bfs(a, b, n);
    if (path.empty())
        cout << -1 << endl;
    else
    {
        cout << path.size() - 1 << endl;
        for (auto &v : path)
            cout << v << " ";
    }
}