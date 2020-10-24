#include <iostream>
#include <stdio.h>
#include <algorithm>

int main(void)
{
    int N, average, middle_result, middle, frequent_value, range, tot, max, min, j;
    frequent_value = 4001;
    max = 0;
    min = 4001;
    j = 0;

    scanf("%d", &N);
    int array[N];
    if (N >= 1 && N <= 500000)
        for (int i = 0; i < N; i++)
            scanf("%d", &array[i]);
    else
        printf("N은 1 이상 500000 이하로 입력해주세요.");

    int frequent[N];
    std::sort(array, array + N);
    for (int i = 0; i < N; i++)
    {
        if (max <= array[i])
            max = array[i];
        if (min >= array[i])
            min = array[i];
        if (array[i] == array[i - 1])
        {
            frequent[i] = j++;
        }
        else
        {
            j = 0;
        }
        tot += array[i];
    }

    average = tot / N;
    middle = int(N / 2);
    range = max - min;

    printf("%d\n%d\n%d\n%d\n", average, array[middle], 4444, range);
}