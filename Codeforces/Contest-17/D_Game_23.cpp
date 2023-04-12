#include <bits/stdc++.h>

using namespace std;

int solve(long curr, long target, int steps)
{
    if (curr > target) return -1;
    if (curr == target) return steps;

    long left = solve(curr * 2, target, steps + 1);
    long right = solve(curr * 3, target, steps + 1);

    if (left == -1)
        return right;
    if (right == -1)
        return left;

    return left;
}

int main()
{
    int n, m;
    cin >> n >> m;
    cout << solve(n, m, 0) << endl;
    return 0;
}