#include <iostream>

int main(){
    double x1;
    int x2;
    std::cout << "What is the price for apples? ";
    std::cin >> x1;
    std::cout << "How many apples will you be buying? ";
    std::cin >> x2;
    std::cout << "The price is ";
    std::cout << x1 * x2;
    return 0;
}