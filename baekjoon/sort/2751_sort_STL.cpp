#include <iostream>
#include <algorithm>

int main()
{
    int N;
    std::cin >> N;

    int array[N];
    if (N >= 1 && N <= 1000000)
    {
        for (int i = 0; i < N; i++)
            std::cin >> array[i];
        std::sort(array, array + N);
        for (int i = 0; i < N; i++)
            std::cout << array[i] << "\n";
    }
}