#include <stdio.h>

int		sumof(int a, int b)
{
	int i;
	int large_number;
	int small_number;
	int sum;

	sum = 0;
	if (a > b)
	{
		large_number = a;
		small_number = b;
	}
	else
	{
		small_number = a;
		large_number = b;
	}
	i = (large_number - small_number + 1) / 2;
	sum = (large_number + small_number) * i;
	if ((large_number - small_number + 1) % 2)
		sum += (i + 1);
	return (sum);
}

int		main(void)
{
	printf("%d입니다.\n", sumof(1, 10));
}
