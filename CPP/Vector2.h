#include "Point.h"
#include <iostream>

class Vector2 {
private:
    class Coordinate {
        private:
            Vector2* super;
            float value;
        public:
            //Constructor
            Coordinate(Vector2* v, float num) : super(v), value(num) {};
            Coordinate() = default;
            //Overloads
            float operator =(float num);
    };
public:
    Coordinate x;
    Coordinate y;
    //Constructors
    //Default constructor
    Vector2(float& x_init, float& y_init) : x(this, x_init), y(this, y_init)  {};
    Vector2() = default;

    //Constructor from Point
    Vector2(Point& point);
    //Constructor from two Points
    Vector2(Point& point, Point& point2); 
};

