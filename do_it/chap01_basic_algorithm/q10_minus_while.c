#include <stdio.h>

int		main(void)
{
	int a;
	int b;

	printf("a의 값 : ");
	scanf("%d", &a);
	printf("\nb의 값 : ");
	scanf("%d", &b);
	while (b <= a)
	{
		printf("\na보다 큰 값을 입력하세요!\nb의 값 : ");
		scanf("%d", &b);
	};
	printf("\nb - a는 %d입니다.", b - a);
	return (0);
}
