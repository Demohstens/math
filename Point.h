//CPP adaptation of the Point class from /datatypes/Point.py
#ifndef POINT_H
#include <iostream>
#endif

class Point {
    public:
        class Coordinate {
            private:
                Point* super;
                int value;
            public:
                Coordinate(Point* point, int num) : value(num), super(point) {};
                //Overload the assignment operator to allow for a function call on change or coordinate
                int operator=(int num) {
                    this->value = num;
                    super->coordinateChanged(num);
                    return this->value;
                }
                int  operator +(int num) {
                    this->value += num;
                    return this->value;
                }
                bool operator==(int num) {
                    return this->value == num;
                }
                int operator-(int num) {
                    this->value -= num;
                    return this->value;
                }
                int operator/(int num) {
                    this->value /= num;
                    return this->value;
                }
                operator int() const{
                    return this->value;
                }
        };
        Coordinate x;
        Coordinate y;
        //Class constructor. Args: x, y
        Point(int x, int y) : x(this, x), y(this, y) {};
        bool operator==(Point& other) {
            return this->x == other.x && this->y == other.y;
        }
        bool operator!=(Point& other) {
            return this->x != other.x || this->y != other.y;
        }
        //Operator overloads went here but it's so cluttered. Gonna leave out for now
        private:
        //function to express a coordinate change [placeholder for now]
        void coordinateChanged(int change) {
            std::cout << "changed by " << change << std::endl;
            }
};
