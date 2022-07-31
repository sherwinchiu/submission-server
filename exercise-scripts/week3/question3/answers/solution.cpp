#include <iostream>

void parity(int x);

int main(){
    return 0;
}

void parity(int x){
    if(x%2 == 0){
        std::cout << "wow it is even!";
    } else{
        std::cout << "wow it is odd!";
    }
}