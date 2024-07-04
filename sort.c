#include <cstdio>

struct MyStruct {
    int firstVar;
    int secondVar;
};

bool compareStructs(const MyStruct &a, const MyStruct &b) {
    return a.firstVar < b.firstVar;
}

void swap(MyStruct &a, MyStruct &b) {
    MyStruct temp = a;
    a = b;
    b = temp;
}

void bubbleSort(MyStruct arr[], int size) {
    for (int i = 0; i < size - 1; ++i) {
        for (int j = 0; j < size - i - 1; ++j) {
            if (compareStructs(arr[j + 1], arr[j])) {
                swap(arr[j], arr[j + 1]);
            }
        }
    }
}

int main() {
    int size;
    printf("Enter the size of the array: ");
    scanf("%d", &size);

    MyStruct *array = new MyStruct[size];

    printf("Enter values for the structs (firstVar secondVar):\n");
    for (int i = 0; i < size; ++i) {
        scanf("%d %d", &array[i].firstVar, &array[i].secondVar);
    }

    bubbleSort(array, size);

    printf("Sorted array of structs:\n");
    for (int i = 0; i < size; ++i) {
        printf("%d %d\n", array[i].firstVar, array[i].secondVar);
    }

    delete[] array;

    return 0;
}
