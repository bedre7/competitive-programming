#include <iostream>
#include <string>
#include <vector>
using namespace std;

int reverse(int number)
{
    string str = to_string(number);
    char temp;
    for(int i = 0, j = str.length() - 1; i < j; i++, j--)
    {
        temp = str[i];
        str[i] = str[j];
        str[j] = temp;  
    }
    return stoi(str);
}
bool isPalindrome(int number)
{
    return number == reverse(number);
}
vector<long long> findMaxPalindromicProduct()
{
    int maxMultiplier = 999;
    int variableMultiplier = 999;
    long long product;
    vector<long long> prods;
    for(int i = 999; i > 99; i--)
    {
        for(int j = 999; j > 99; j--)
        {
            product = i * j;
            if(isPalindrome(product))
                prods.push_back(product);
        }
        maxMultiplier--;
    }
    return prods;
}
int main()
{
    vector<long long> prods = findMaxPalindromicProduct();
    long long max = INT64_MIN;
    for(auto c : prods)
    {
        if(c > max)
            max = c;
    }
    cout << max << endl;
    return 0;
}