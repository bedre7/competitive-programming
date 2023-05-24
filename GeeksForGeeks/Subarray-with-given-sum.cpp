#include <bits/stdc++.h>
using namespace std;

// Function to find a continuous sub-array which adds up to a given number.
vector<int> subarraySum(vector<int> arr, int n, long long s)
{
    int left = 0, right = 0, currSum = 0;
    for (; right < n; right++)
    {
        if (currSum == s)
            return {left + 1, right};
        currSum += arr[right];
        while (currSum > s)
            currSum -= arr[left++];
    }
    while (left < n && currSum > s)
    {
        currSum -= arr[left++];
    }
    if (currSum == s && s != 0)
    {
        return {left + 1, right};
    }
    return {-1, -1};
}

//{ Driver Code Starts.

int main()
{
    int n, s;
    cin >> n >> s;
    vector<int> v(n);
    for (int i = 0; i < n; i++)
    {
        cin >> v[i];
    }
    for (auto &i : subarraySum(v, n, s))
    {
        cout << i << " ";
    }
    return 0;
}