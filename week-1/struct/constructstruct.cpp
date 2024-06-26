#include <iostream>
#include <string>

using namespace std;
struct Person {
    string name;
    int age;
    double height;
    Person(const string& n, int a, double h) : name(n), age(a), height(h) {}
};

int main() {
    Person person1("John Doe", 30, 5.9);    
    cout << "Name: " << person1.name << endl;
    cout << "Age: " << person1.age << endl;
    cout << "Height: " << person1.height << endl;

    return 0;
}
