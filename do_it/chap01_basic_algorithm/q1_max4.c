#include <stdio.h>

int		max4(int a, int b, int c, int d)
{
	int max;
	
	max = a;
	if (b > max)
		max = b;
	if (c > max)
		max = c;
	if (d > max)
		max = d;
	return (max);
}

int		main(void)
{
	printf("max4(%d, %d, %d, %d) = %d\n", 4, 3, 2, 1, max4(4, 3, 2, 1));
	printf("max4(%d, %d, %d, %d) = %d\n", 4, 2, 3, 1, max4(4, 2, 3, 1));
	printf("max4(%d, %d, %d, %d) = %d\n", 3, 1, 4, 2, max4(3, 1, 4, 2));
	printf("max4(%d, %d, %d, %d) = %d\n", 1, 2, 3, 4, max4(1, 2, 3, 4));
	printf("max4(%d, %d, %d, %d) = %d\n", 4, 2, 4, 1, max4(4, 2, 4, 1));
	return (0);
}
