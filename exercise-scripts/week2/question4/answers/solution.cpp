#include <iostream>

int main(){
    int character;
    std::cout << "What is your character? ";
    std::cin >> character;
    if ((character >= 123 && character <= 126) || (character >= 91 && character <= 96) || (character >= 58 && character <= 64) || (character >= 33 && character <= 47)){
        std::cout << "That is a special character.";
    } else if(character >= 48 && character <= 57){
        std::cout << "That is a number.";
    } else if(character >= 65 && character <= 90){
        std::cout << "That is an uppercase letter.";
    } else{
        std::cout << "That is a lowercase letter.";
    }
    return 0;
}