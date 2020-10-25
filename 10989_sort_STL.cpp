#include <stdio.h>
#include <algorithm>

int main(void)
{
    int N;

    scanf("%d", &N);
    if (N < 1 || N > 10000000)
    {
        printf("1보다 크거나 같고, 10,000,000보다 작거나 같은 수로 입력해주세요.");
        return (0);
    }
    int array[N];
    for (int i = 0; i < N; i++)
    {
        scanf("%d", &array[i]);
        if (array[i] > 10000)
        {
            printf("10,000보다 작거나 같은 자연수를 입력해주세요.");
            return (0);
        }
    }
    std::sort(array, array + N);
    for (int i = 0; i < N; i++)
        printf("%d\n", array[i]);
    return (0);
}