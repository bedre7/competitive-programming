#include <bits/stdc++.h>

using namespace std;

#define MAX 200002
int temps[MAX]{0};

int main()
{
    int n, k, q;
    cin >> n >> k >> q;

    int l, r;
    for (int i = 0; i < n; i++)
    {
        cin >> l >> r;
        temps[l] += 1;
        temps[r + 1] -= 1;
    }

    for (int i = 1; i < MAX; i++)
        temps[i] += temps[i - 1];
    
    int admissibles = 0;
    for (int i = 0; i < MAX; i++){
        if (temps[i] >= k) admissibles++;
        temps[i] = admissibles;
    }
        
    int a, b;
    for (int i = 0; i < q; i++)
    {
        cin >> a >> b;
        cout << temps[b] - temps[a - 1] << endl;
    }
    
    return 0;
}