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
                int operator += (int num) {
                    this->value += num;
                    return this->value;
                }
                int operator++(int) {
                    this->value++;
                    return this->value;
                }
                int operator--(int) {
                    this->value--;
                    return this->value;
                }
                bool operator==(int num) {
                    return this->value == num;
                }
                int operator-(int num) {
                    this->value -= num;
                    return this->value;
                }
                int operator -= (int num) {
                    this->value -= num;
                    return this->value;
                }
                int operator*(int num) {
                    this->value *= num;
                    return this->value;
                }
                int operator*= (int num) {
                    this->value *= num;
                    return this->value;
                }
                int operator/(int num) {
                    this->value /= num;
                    return this->value;
                }
                int operator/= (int num) {
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
        //Generate operator overload functions for all possible combinations of operators

        //Addition
        Point operator+(Point& other) {
            return Point(this->x + other.x, this->y + other.y);
        }
        Point operator+(int num) {
            return Point(this->x + num, this->y + num);
        }
        Point operator+=(Point& other) {
            return Point(this->x += other.x, this->y += other.y);
        }
        Point operator+=(int num) {
            return Point(this->x += num, this->y += num);
        }
        //Subtraction
        Point operator-(Point& other) {
            return Point(this->x - other.x, this->y - other.y);
        }
        Point operator-(int num) {
            return Point(this->x - num, this->y - num);
        }
        Point operator-=(Point& other) {
            return Point(this->x -= other.x, this->y -= other.y);
        }
        Point operator-=(int num) {
            return Point(this->x -= num, this->y -= num);
        }
        //Multiplication
        Point operator*(Point& other) {
            return Point(this->x * other.x, this->y * other.y);
        }
        Point operator*(int num) {
            return Point(this->x * num, this->y * num);
        }
        Point operator*=(Point& other) {
            return Point(this->x *= other.x, this->y *= other.y);
        }
        Point operator*=(int num) {
            return Point(this->x *= num, this->y *= num);
        }
        //Division
        Point operator/(Point& other) {
            return Point(this->x / other.x, this->y / other.y);
        }
        Point operator/(int num) {
            return Point(this->x / num, this->y / num);
        }
        Point operator/=(Point& other) {
            return Point(this->x /= other.x, this->y /= other.y);
        }
        Point operator/=(int num) {
            return Point(this->x /= num, this->y /= num);
        }
        //Increment
        Point operator++(int) {
            return Point(this->x++, this->y++);
        }
        //Decrement
        Point operator--(int) {
            return Point(this->x--, this->y--);
        }
        //Negation
        Point operator-() {
            return Point(-this->x, -this->y);
        }
        //Assignment
        Point operator=(Point& other) {
            return Point(this->x = other.x, this->y = other.y);
        }
        Point operator=(int num) {
            return Point(this->x = num, this->y = num);
        }
        private:
        //function to express a coordinate change [placeholder for now]
        void coordinateChanged(int change) {
            std::cout << "changed by " << change << std::endl;
            }
};
