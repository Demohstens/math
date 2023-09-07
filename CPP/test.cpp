#include "Vector2.cpp"
#include <iostream>

int main() {
    Vector2 v = Vector2(5.0f, 5.0f);
    char s[10];
    sprintf(s, "%f", v.x);
    std::cout << s << std::endl;
}