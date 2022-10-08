#include <iostream>
#include <string>
using namespace std;

int sumOfFactors(int number)
{
    int factorsSum = 0;
    for(int i = 1; i <= number/2; i++)
    {
        if(number % i == 0) factorsSum += i;
    }
    return factorsSum;
}
bool areAmicable(int a, int b)
{
    return a == sumOfFactors(b) && b == sumOfFactors(a);
}
int main()
{
    long long sum = 0;
    int number = 220;
    for(int i = 1; i < 10000; i++)
    {
        for(int j = 1; j < 10000; j++)
            if(i != j)
                if(areAmicable(i, j))
                {
                    cout << i << " and " << j << endl;
                    sum += i;
                }
    } 
    cout << sum << endl;  
    return 0;
}