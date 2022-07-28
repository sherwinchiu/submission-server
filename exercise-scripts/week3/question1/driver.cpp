#define TESTING
#include <iostream>

int main(int argc, char *argv[]){
    std::cout << sum(5, 10) << std::endl;
    std::cout << (sum(32.312, 61.12)) << std::endl;
    std::cout << (sum(std::atof(argv[1]), std::atof(argv[2]))) << std::endl;
    std::cout << (sum(std::atof(argv[3]), std::atof(argv[4]))) << std::endl;
    return 0;
}
