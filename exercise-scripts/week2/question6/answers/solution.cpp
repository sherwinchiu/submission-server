#include <iostream>
#include <cstdlib>

int main(){
    srand (time(NULL));
    int answer = rand() % 100 +1;
    std::cout << answer;
    int x1;
    while(x1 != answer){
        std::cout << "What number do you guess? ";
        std::cin >> x1;
        if(x1 > 100 || x1 < 1){
            std::cout << "That number is out of range. Choose a different number." << std::endl;
        } else if(x1 < answer){
            std::cout << "The number to guess is higher." << std::endl;
        } else if(x1 > answer){
            std::cout << "The number to guess is lower." << std::endl;
        } else{
            std::cout << "That is the correct number!" << std::endl;
        }
    }
    return 0;
}