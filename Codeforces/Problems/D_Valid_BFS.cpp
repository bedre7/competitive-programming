#include <bits/stdc++.h>

using namespace std;
int n, u, v;
map<int, vector<int>> graph;

bool isValid(vector<int> &seq)
{
    vector<bool> visited(n + 1, false);
    queue<set<int>> q;
    set<int> root;
    root.insert(1);
    q.push(root);
    int i = 0;

    while (!q.empty() && i < n)
    {
        if (q.front().empty()) q.pop();
        if (visited[seq[i]])
            return false;
        visited[seq[i]] = true;

        if (q.front().find(seq[i]) == q.front().end())
            return false;

        set<int> chlidren;
        for (int v : graph[seq[i]])
        {
            if (!visited[v])
                chlidren.insert(v);
        }
        if (chlidren.size() > 0)
            q.push(chlidren);
        q.front().erase(seq[i++]);
    }
    return true;
}

int main()
{
    cin >> n;
    for (int i = 0; i < n - 1; i++)
    {
        cin >> u >> v;
        graph[u].push_back(v);
        graph[v].push_back(u);
    }
    vector<int> seq(n);
    for (int i = 0; i < n; i++)
    {
        cin >> seq[i];
        // cout << seq[i];
    }
    bool ok = isValid(seq);
    cout << (ok ? "Yes" : "No");
}