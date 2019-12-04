
#include <iostream>
#include <string>
#include <fstream>
#include <sstream>

#include <boost/algorithm/string.hpp>
using namespace std;

int parse_ints(vector<string> tokens, vector<int> &result) {
   for (auto &s : tokens) {
      stringstream parser(s);
      int n;
      parser >> n;
      result.push_back(n);
   }
}

int main() {
   ifstream input("input.txt");

   string line;

   int sum_1 = 0;

   while (input >> line) {
      vector<string> strings;
      boost::split(strings, line, boost::is_any_of("x"));
      vector<int> tokens;
      parse_ints(strings, tokens);

      vector sa({tokens[0] * tokens[1], tokens[1] * tokens[2], tokens[2] * tokens[1]});

      sum_1 += 2 * (sa[0] + sa[1] + sa[2]) + *min_element(sa.begin(), sa.end());
   }
   
   cout << "Part 1: " << sum_1 << endl;
   
}