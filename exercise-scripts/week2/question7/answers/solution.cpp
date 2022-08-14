#include <iostream>

int main(){
    int x1;
    std::cout << "What number do you want to factorial? ";
    std::cin >> x1; 
    int factorial = 1;
    for(int i = 1; i <= x1; i++){
        factorial *= i;
    }
    std::cout << factorial;
    return 0;
}