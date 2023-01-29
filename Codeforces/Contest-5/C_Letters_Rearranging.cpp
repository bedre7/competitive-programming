#include <bits/stdc++.h>

using namespace std;

void runcase()
{
    string word;
    cin >> word;

    string temp = word;
    reverse(word.begin(), word.end());
    if (temp != word){
        cout << temp << endl;
        return;
    }

    for (int i = 0; i < word.size() / 2; i++)
    {
        char tmp = word[i];
        word[i] = word[i+1];
        word[i+1] = tmp;

        temp = word;
        reverse(word.begin(), word.end());
        if (word != temp)
        {
            cout << temp << endl;
            return;
        }
    }

    cout << -1 << endl;
}
int main(){
    int test;
    cin >> test;
    while (test--)
        runcase();
}