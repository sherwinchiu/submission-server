#include <iostream>

int main(){
    double x1, x2;
    char operation;
    double answer;
    std::cout << "What is the first number? ";
    std::cin >> x1;
    std::cout << "What is the second number? ";
    std::cin >> x2;
    std::cout << "What operation do you want to do? ";
    std::cin >> operation;
    if (operation == '+'){
        answer = x1 + x2;
    } else if (operation == '-'){
        answer = x1 - x2;
    } else if (operation == '*'){
        answer = x1 * x2;
    } else if (operation == '/'){
        answer = x1 / x2;
    }
    std::cout << "The answer is " << answer << std::endl;
    return 0;
}