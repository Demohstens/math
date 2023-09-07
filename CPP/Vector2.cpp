#include "Vector2.h"
#include <iostream>
//Constructor definitions for Vector2
//Also initiate the Coordinate objects
Vector2::Vector2(Point& point): x(this, point.x), y(this, point.y) {}
Vector2::Vector2(Point& point, Point& point2) : x(this, point.x), y(this, point.y) {}
//Operator overloads for Coordinate
float Vector2::Coordinate::operator =(float num) {
    this->value = num;
    return this->value;
}

