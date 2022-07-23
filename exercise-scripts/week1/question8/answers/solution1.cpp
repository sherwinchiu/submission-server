#include <iostream>

int main(){
    int nickles, dimes, quarters, loonies, toonies;
    std::cin >> nickles >> dimes >> quarters >> loonies >> toonies;
    std::cout << nickles*0.05+dimes*0.1+quarters*0.25+loonies+toonies*2;
    return 0;
}