#define TESTING
#include <iostream>

int main(int argc, char *argv[]){
    std::cout << absolute(23) << std::endl;
    std::cout << absolute(-23) << std::endl;
    std::cout << (absolute(std::atof(argv[1]))) << std::endl;
    std::cout << (absolute(std::atof(argv[2])))  << std::endl;
    std::cout << (absolute(std::atof(argv[3])))  << std::endl;
    return 0;
}
