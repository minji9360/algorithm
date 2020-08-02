#include <stdio.h>

int		main(void)
{
	int i;
	int n;
	int sum;

	i = 1;
	sum = 0;
	scanf("%d", &n);
	while (i <= n)
	{
		sum += i;
		i++;
	}
	printf("변수 n의 값은 %d입니다.\n", n);
	printf("변수 i의 값은 %d + 1인 %d입니다.\n", n, i);
	printf("1부터 %d까지의 합은 %d입니다.\n", n, sum);

	return (0);
}
