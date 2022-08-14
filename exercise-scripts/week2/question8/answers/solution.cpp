#include <iostream>

int main(){
    int x1;
    std::cout << "What number do you want to reverse? ";
    std::cin >> x1; 
    while(x1 > 0){
        std::cout << x1 % 10;
        x1 = x1/10;
    }
    return 0;
}