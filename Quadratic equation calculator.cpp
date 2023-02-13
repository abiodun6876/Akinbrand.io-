#include <iostream>

#include <cmath>

using namespace std;

int main() {

  int a, b, c;

  double d, x1, x2;

  cout << "QUADRATIC EQUATION SOLVER" << endl;

  cout << "ax^2 + bx + c = 0" << endl;

  cout << "Enter the value of a: ";

  cin >> a;

  cout << "Enter the value of b: ";

  cin >> b;

  cout << "Enter the value of c: ";

  cin >> c;

  d = sqrt(b*b - 4*a*c);

  x1 = (-b + d) / (2*a);

  x2 = (-b - d) / (2*a);

  cout << endl << "The solutions are:" << endl;

  cout << "x1 = " << x1 << endl;

  cout << "x2 = " << x2 << endl;

  return 0;

}

