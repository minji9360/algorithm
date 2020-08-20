#include <stdio.h>

int		main(void)
{
	int n;
	int m;

	scanf("%d", &n);
	scanf("%d", &m);
	if (n <= 10^1000, n >= m 
			&& m >= 1)
		printf("%d\n%d", n / m, n % m);
	else
		printf("m과 n의 범위를 확인해주세요.");
	return(0);
}
