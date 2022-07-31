#define TESTING
#include <iostream>

int main(int argc, char *argv[]){
    parity(std::atof(argv[1]));
    std::cout << ":";
    parity(std::atof(argv[2]));
    std::cout << ":";
    parity(std::atof(argv[3]));
    std::cout << ":";
    parity(std::atof(argv[4]));
    std::cout << ":";
    (parity(std::atof(argv[5])));
    std::cout << ":";
    (parity(std::atof(argv[6])));
    return 0;
}
