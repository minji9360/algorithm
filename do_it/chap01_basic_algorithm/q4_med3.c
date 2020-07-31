#include <stdio.h>

int		med3(int a, int b, int c)
{
	if (a >= b)
		if (b >= c)
			return (b);
		else if (a >= c)
			return (c);
		else
			return (a);
	else if (a > c)
		return (a);
	else if (b > c)
		return (c);
	else
		return (b);
}

int		main(void)
{
	int a;
	int b;
	int c;

	scanf("%d", &a);
	scanf("%d", &b);
	scanf("%d", &c);
	printf("세 값에서 중앙값은 %d입니다.", med3(a, b, c));
}

