#include <iostream>

int main(){
    double x1, sum;
    int x2;
    std::cin >> x1 >> x2;
    sum = x1*x2;
    std::cin >> x1 >> x2;
    std::cout << "The total price is " << x1*x2 + sum;
    return 0;
}