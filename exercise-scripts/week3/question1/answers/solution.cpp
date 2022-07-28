#include <iostream>

double sum(double x1, double x2);

int main(){
    std::cout << sum(5, 10) << std::endl;
    return 0;
}

double sum(double x1, double x2){
    return x1 + x2;
}