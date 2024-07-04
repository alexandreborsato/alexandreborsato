#include <iostream>
#include <string>

struct MyStruct {
    int intValue;
    std::string strValue;
};

// Function to parse a struct and an integer to another function
void functionA(const MyStruct& myStruct, int number) {
    std::cout << "Received struct: intValue = " << myStruct.intValue << ", strValue = " << myStruct.strValue << std::endl;
    std::cout << "Received integer: " << number << std::endl;

    // Call functionB and pass the struct and integer
    functionB(myStruct, number);
}

void functionB(const MyStruct& myStruct, int number) {
    std::cout << "Received struct in functionB: intValue = " << myStruct.intValue << ", strValue = " << myStruct.strValue << std::endl;
    std::cout << "Received integer in functionB: " << number << std::endl;
}

int main() {
    MyStruct myData;
    int myNumber;

    std::cout << "Enter an integer: ";
    std::cin >> myNumber;

    std::cout << "Enter struct values (intValue strValue): ";
    std::cin >> myData.intValue >> myData.strValue;

    // Call functionA and pass the struct and integer
    functionA(myData, myNumber);

    return 0;
}
