#include <iostream>

double absolute(double x){
    if ( x < 0){
        x = x*-1.0;
    } 
    return x;
}

int main(){
    std::cout << absolute(5) << std::endl;
    std::cout << absolute(-5) << std::endl;
    std::cout << absolute(-5.321) << std::endl;
    std::cout << absolute(25) << std::endl;
    std::cout << absolute(53.3) << std::endl;
    return 0;
}

