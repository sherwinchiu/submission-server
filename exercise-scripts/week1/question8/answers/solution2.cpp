#include <iostream>

int main(){
    int nickles, dimes, quarters, loonies, toonies;
    std::cout << "How many nickles do you have? ";
    std::cin >> nickles;
    std::cout << "How many dimes do you have? ";
    std::cin >> dimes;
    std::cout << "How many quarters do you have? ";
    std::cin >> quarters;
    std::cout << "How many loonies do you have? ";
    std::cin >> loonies;
    std::cout << "How many toonies do you have? ";
    std::cin >> toonies;
    std::cout << "You have " << nickles*0.05+dimes*0.1+quarters*0.25+loonies+toonies*2 << "in change.";
    return 0;
}