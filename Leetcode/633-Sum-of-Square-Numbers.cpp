#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool judgeSquareSum(int c) {
        int bSquared;
        for (long a = 0; pow(a, 2) <= c; a++)
        {
            bSquared = c - (int)pow(a, 2);
            if (binarySearch(0, bSquared, bSquared))
                return true;
        }
        return false;
    }
    bool binarySearch(long start, long end, int num)
    {
        if (start > end) return false;
        long mid = (start + end) / 2;
        
        if (pow(mid, 2) == num) return true;
        else if (pow(mid, 2) > num)
            return binarySearch(start, mid - 1, num);
        else return binarySearch(mid + 1, end, num);
    }
};
