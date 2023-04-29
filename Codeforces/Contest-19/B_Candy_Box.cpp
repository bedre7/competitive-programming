#include <bits/stdc++.h>

using namespace std;

void runCase()
{
    int n;
    cin >> n;
    vector<int> candies(n);
    for (int i = 0; i < n; i++)
        cin >> candies[i];

    unordered_map<int, int> freq;
    for (int i = 0; i < n; i++)
        freq[candies[i]]++;

    // sort by value
    vector<int> freqSorted;
    for (auto it = freq.begin(); it != freq.end(); it++)
        freqSorted.push_back(it->second);
    sort(freqSorted.begin(), freqSorted.end());

    set<int> counted;
    int size = 0;

    for (int i = 0; i < freqSorted.size(); i++)
    {
        int currCount = freqSorted[i];
        while (counted.find(currCount) != counted.end())
            currCount--;
        
        if (currCount > 0)
        {
            counted.insert(currCount);
            size += currCount;
        }
    }

    cout << size << endl;
}

int main()
{
    int t;
    cin >> t;
    while (t--)
        runCase();
}