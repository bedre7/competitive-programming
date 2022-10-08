#include <iostream>
#include <vector>
#include <math.h>

using namespace std;

bool isPrime(int number)
{
    if(number < 2) return false;
    for(int i = 2; i*i <= number; i++)
        if(number % i == 0) return false;
    return true;
}
int main(){
    long long number = 600851475143 ;
    vector<int> factors;
    for(long long i = 2; i*i <= number; i++)
    {
        if(number % i == 0)
        {
            if(isPrime(i))
                factors.push_back(i);
        }
    }
    cout << "Largest Prime is : " << factors[factors.size() - 1] << endl;
 
    return 0;
} 