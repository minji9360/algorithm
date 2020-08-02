#include <stdio.h>

int		main(void)
{
	int i;
	int n;
	int sum;

	scanf("%d", &n);
	i = n / 2;
	sum = (1 + n) * i;
	if (n % 2)
	{
		sum += (i + 1);
	}
	printf("1부터 n까지의 정수 합은 %d입니다.\n", sum);
	return (0);
}
