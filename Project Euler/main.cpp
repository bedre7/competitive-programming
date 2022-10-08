#include <queue>
#include <iostream>
#include <string>
#include <fstream>
#include <string>

using namespace std;
void print_queue(std::queue<int> &q)
{
  while (!q.empty())
  {
   cout << q.front() << " ";
    q.pop();
  }
  cout << endl;
}

int main()
{
  string line;
  ifstream readfile;

  readfile.open("Nokta.txt");

  if(!readfile.is_open())
    cout << "File is not open" << endl;
    
  while(getline(readfile, line))
  {
    cout << line << endl;
  }
  
  readfile.close();
  return 0;
}