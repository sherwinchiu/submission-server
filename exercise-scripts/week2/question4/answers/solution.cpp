#include <iostream>

int main(){
    char character;
    std::cout << "What is your character? ";
    std::cin >> character;
    character = int(character);
    if(character >= 48 and character <= 57){
        std::cout << "number";
    } else if(character >= 65 and character <= 90){
        std::cout << "uppercase";
    } else if(character >= 97 and character <= 122){
        std::cout << "lowercase";
    } else{
        std::cout << "special";
    }
    return 0;
}