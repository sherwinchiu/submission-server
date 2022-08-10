#include <iostream>

int main(){
    int x1, x2;
    std::cout << "What is the first number? ";
    std::cin >> x1; 
    std::cout << "What is the second number? ";
    std::cin >> x2;
    if(x1 % x2 == 0){
        std::cout << x1 << " is divisible by " << x2 << ".";
    } else{
        std::cout << x1 << " is not divisible by " << x2 << ".";
    }
    return 0;
}