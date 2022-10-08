class Solution {
public:
     map<char, string> numToLetterMap = {
            {'2', "abc"},
            {'3', "def"},
            {'4', "ghi"},
            {'5', "jkl"},
            {'6', "mno"},
            {'7', "pqrs"},
            {'8', "tuv"},
            {'9', "wxyz"},
        };
    
    vector<string> letterCombinations(string digits) {
        vector<string> combination;
        if(digits == "") return combination;
        string ch;
        
        for (int i = 0; i < digits.length(); i++)
        {
            if(i == 0)
            {
                for (auto c: numToLetterMap[digits[0]])
                {
                    ch = c;
                    combination.push_back(ch);
                }
            }
            else
                makeCombination(combination, digits[i]);    
        }
        return combination;
    }
    void makeCombination(vector<string> &combination, char current)
    {
        int size = combination.size();
        for (int i = 0; i < size; i++)
        {
            string letters = numToLetterMap[current];
            string prevComb = combination[i];
            for (int j = 0; j < letters.length(); j++)
            {
                if(j == 0)
                    combination[i] += letters[j];
                else{
                    combination.push_back(prevComb + letters[j]);
                }
            }
        }
    }
};