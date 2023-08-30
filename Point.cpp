#include <iostream>
#include "Point.h"



int main() {
    Point p(1,1);
    Point p2(1,1);
    if (p == p2) 
    {
        std::cout << "equal" << std::endl;
    }
}