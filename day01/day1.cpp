

#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int calc_fuel(int mass) {
   int sum = 0;
   while(mass > 0) {
      int fuel = (mass / 3) - 2;
      if (fuel > 0) sum += fuel;
      mass = fuel;
   }
   return sum;
}

int main() {
   ifstream input("input.txt");

   int n;
   int sum_1 = 0;
   int sum_2 = 0;
   while (input >> n) {
      sum_1 += (n / 3) - 2;
      sum_2 += calc_fuel(n);
   }

   cout << "Part 1: " << sum_1 << "\n";

   cout << "Part 2: " << sum_2 << "\n";
}