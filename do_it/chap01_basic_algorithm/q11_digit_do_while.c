#include <stdio.h>

int		main(void)
{
	int number;
	int digit;

	digit = 0;
	scanf("%d", &number);
	if (number > 0)
	{
		do
		{
			number /= 10;
			digit++;
		} while (number);
		printf("그 수는 %d자리입니다.", digit);
	}
	else
		printf("양의 정수만 입력해주세요.");
	return (0);
}

