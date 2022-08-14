#include <iostream>

int main(){
    int x1, x2;
    std::cout << "What is the width of the rectangle? ";
    std::cin >> x1; 
    std::cout << "What is the height of the rectangle? ";
    std::cin >> x2;

    for(int i = 0; i < x2; i++){
        for(int j = 0; j < x1; j++){
            std::cout << "*";
        }
        std::cout << std::endl;
    }

    return 0;
}