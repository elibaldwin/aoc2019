
#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>

#include <boost/algorithm/string.hpp>

int run(std::vector<int> mem, int noun, int verb) {
   mem[1] = noun;
   mem[2] = verb;

   int pos = 0;
   while(1) {
      int opcode = mem[pos];

      if (opcode == 1) {
         mem[mem[pos+3]] = mem[mem[pos+1]] + mem[mem[pos+2]];
      } else if (opcode == 2) {
         mem[mem[pos+3]] = mem[mem[pos+1]] * mem[mem[pos+2]];
      } else if (opcode == 99) {
         break;
      } else {
         std::cout << "unknown opcode " << opcode << std::endl;
      }

      pos += 4;
   }

   return mem[0];
}

int main() {
   std::vector<int> input({1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,10,19,1,19,5,23,1,6,23,27,1,27,5,31,2,31,10,35,2,35,6,39,1,39,5,43,2,43,9,47,1,47,6,51,1,13,51,55,2,9,55,59,1,59,13,63,1,6,63,67,2,67,10,71,1,9,71,75,2,75,6,79,1,79,5,83,1,83,5,87,2,9,87,91,2,9,91,95,1,95,10,99,1,9,99,103,2,103,6,107,2,9,107,111,1,111,5,115,2,6,115,119,1,5,119,123,1,123,2,127,1,127,9,0,99,2,0,14,0});

   std::cout << "Part 1: " << run(std::vector<int>(input), 12, 2) << std::endl;

   int part2 = 19690720;

   for (int i = 0; i < 100; i++) {
      for (int j = 0; j < 100; j++) {
         int output = run(std::vector<int>(input), i, j);
         if (output == part2) {
            std::cout << "Part 2: " << (100 * i + j) << std::endl;
            exit(EXIT_SUCCESS);
         }
      }
   }
}

