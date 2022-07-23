#include <iostream>

int main(){
    double x1;
    int x2;
    double sum;
    std::cout << "What is the price for apples? ";
    std::cin >> x1;
    std::cout << "How many apples will you be buying? ";
    std::cin >> x2;
    sum = x1*x2;
    std::cout << "What is the price for oranges? ";
    std::cin >> x1;
    std::cout << "How many oranges will you be buying? ";
    std::cin >> x2;
    std::cout << "The total price is " << x1*x2 + sum;
    return 0;
}