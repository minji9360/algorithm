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
		printf("%d", i);
		if (i < n)
			printf(" + ");
		else
			printf(" = ");
		sum += i;
		i++;
	}
	printf("%d", sum);
	return (0);
}
