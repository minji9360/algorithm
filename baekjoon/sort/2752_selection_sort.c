#include <stdio.h>

int		main(void)
{
	int array[3];
	int i, j, min, temp, index;
	
	for (i = 0; i < 3; i++)
		scanf("%d", &array[i]);
	for (i = 0; i < 3; i++)
	{
		if (array[i] >= 1 && array[i] <= 1000000)
		{
			min = 1000001;
			for (j = i; j < 3; j++)
				if (array[j] < min)
				{
					min = array[j];
					index = j;
				}
			temp = array[index];
			array[index] = array[i];
			array[i] = temp;
		}
		else
		{
			printf("입력 값의 범위를 확인해주세요.");
			return (0);
		}
	}
	printf("%d %d %d", array[0], array[1], array[2]);
	return (0);
}
