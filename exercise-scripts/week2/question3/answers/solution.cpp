#include <iostream>

int main(){
    int grade;
    std::cout << "What was your grade? ";
    std::cin >> grade;
    if (grade >= 80){
        std::cout << "Congrats on getting an A!";
    } else if (grade >= 70){
        std::cout << "Good job on getting a B!";
    } else if (grade >= 60){
        std::cout << "You got a C, you can do it!";
    } else if (grade >= 50){
        std::cout << "You got a D.";
    } else{
        std::cout << "Unfortunately, you got a F. Try again, you can do it!";
    }
    return 0;
}