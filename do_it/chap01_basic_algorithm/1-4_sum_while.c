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
	printf("1부터 %d까지의 합은 %d입니다.", n, sum);

	return (0);
}
