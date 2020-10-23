#include <iostream>
#include <algorithm>

int main()
{
    using namespace std;
    int N;
    cin >> N;

    int array[N];
    if (N >= 1 && N <= 1000000)
    {
        for (int i = 0; i < N; i++)
            cin >> array[i];
        sort(array, array + N);
        for (int i = 0; i < N; i++)
            cout << array[i] << "\n";
    }
}