#include <stdio.h>

int		main(void)
{
	int i;
	int n;
	int sum;

	sum = 0;
	puts("1부터 n까지의 합을 구합니다.");
	printf("n 값 : ");
	scanf("%d", &n);
	for (i = 1; i <= n; i++)
		sum += i;
	printf("1부터 %d까지의 합은 %d입니다.\n", n, sum);

	return (0);
}
