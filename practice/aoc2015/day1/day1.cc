
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main() {
   
   ifstream input("input.txt");

   string parens;
   input >> parens;

   int floor = 0;

   for (string::iterator it = parens.begin(); it < parens.end(); it++) {
      floor += *it == '(' ? 1 : -1;
   }

   cout << "Part 1: " << floor << endl;

   floor = 0;

   for (string::iterator it = parens.begin(); it < parens.end(); it++) {
      floor += *it == '(' ? 1 : -1;
      if (floor == -1) {
         cout << "Part 2: " << distance(parens.begin(), it) + 1 << endl;
         break;
      }
   }

}