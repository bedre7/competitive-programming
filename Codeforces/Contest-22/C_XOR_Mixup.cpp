#include <bits/stdc++.h>

using namespace std;

void solve(){
    int n;
    cin >> n;
    vector<int> array(n);

    for (int i = 0; i < n; i++)
        cin >> array[i];
    
    for (int i = 0; i < n; i++)
    {
        int XOR = 0;
        for (int j = 0; j < n; j++){
            if (i != j)
                XOR ^= array[j];
        }
        if (XOR ^ array[i] == 0) {
            cout << array[i] << endl;
            return;
        }
    }
}

int main()
{
    int test;
    cin >> test;
    while (test--)
        solve();
}