#include <iostream>
#include <algorithm>

struct MyStruct {
    int firstVar;
    int secondVar;
};

bool compareStructs(const MyStruct &a, const MyStruct &b) {
    return a.firstVar < b.firstVar;
}

int main() {
    int size;
    std::cout << "Enter the size of the array: ";
    std::cin >> size;

    MyStruct *array = new MyStruct[size];

    std::cout << "Enter values for the structs (firstVar secondVar):\n";
    for (int i = 0; i < size; ++i) {
        std::cin >> array[i].firstVar >> array[i].secondVar;
    }

    std::sort(array, array + size, compareStructs);

    std::cout << "Sorted array of structs:\n";
    for (int i = 0; i < size; ++i) {
        std::cout << array[i].firstVar << " " << array[i].secondVar << "\n";
    }

    delete[] array;

    return 0;
}
