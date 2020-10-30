#include <stdio.h>

int main(void)
{
    int front, end;
    scanf("%d-%d", &front, &end);
    printf("%06d%06d", front, end);
    return (0);
}