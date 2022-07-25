#include <iostream>

int main(){
    int x1; 
    int x2 = 0;
    std::cout << "Enter the first number: ";
    std::cin >> x1;
    std::cout << "Enter the second number: "; 
    
    std::cin >> x2;
    std::cin >> x1;
    std::cout << "The sum is " << x1 + x2; 
    return 0;
}