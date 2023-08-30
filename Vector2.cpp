#include "Vector2.h"

//Constructor definitions for Vector2
//Also initiate the Coordinate objects
Vector2::Vector2(Point& point) {
        this->x = Coordinate(this, point.x);
        this->y = Coordinate(this, point.y);
}
Vector2::Vector2(Point& point, Point& point2) {
    this->x = Coordinate(this, point2.x - point.x);
    this->y = Coordinate(this, point2.y - point.y);
}


//Operator overloads for Coordinate
float Vector2::Coordinate::operator =(float num) {
    this->value = num;
    return this->value;
}

int main() {

}