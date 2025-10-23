#include <iostream>
using namespace std;

unsigned long long factorial(int n) {
    if (n < 0) return 0; // undefined for negative inputs
    unsigned long long result = 1;
    for (int i = 2; i <= n; ++i) result *= i;
    return result;
}

int main() {
    cout << "Input: 5 -> Output: Factorial = " << factorial(5) << endl;
    cout << "Input: 0 -> Output: Factorial = " << factorial(0) << endl;
    return 0;
}
