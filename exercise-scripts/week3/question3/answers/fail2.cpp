#include <iostream>

void parity(int x);

int main(){
    return 0;
}

void parity(int x){
    if(x%2 == 1){
        std::cout << "wow it is even!";
    } else{
        std::cout << "wow it is odd!";
    }
}