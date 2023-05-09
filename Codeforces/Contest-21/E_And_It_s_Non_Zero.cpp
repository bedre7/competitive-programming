#include <bits/stdc++.h>

using namespace std;
int prefix[200001][32];

void init()
{

    int mask = 1;
    for (int bit = 0; bit <= 31; bit++)
    {
        for (int i = 1; i <= 200000; i++)
        {
            prefix[i][bit] = prefix[i - 1][bit] + ((i & mask) != 0 ? 1 : 0);
        }
        mask <<= 1;
    }
}

void solve()
{
    int l, r;
    cin >> l >> r;

    int maxOnes = 0;
    for (int bit = 0; bit <= 31; bit++)
    {
        int ones = prefix[r][bit] - prefix[l - 1][bit];
        maxOnes = max(maxOnes, ones);
    }

    cout << r - l + 1 - maxOnes << endl;
}

int main()
{
    int t;
    cin >> t;
    init();
    while (t--)
    {
        solve();
    }
}