#include <stdio.h>

int array[1000001];

void quickSort(int *array, int start, int end)
{
	int pivot, i, j, temp;

	pivot = start;
	i = start + 1;
	j = end;
	if (start >= end)
		return;
	while (i <= j)
	{
		while (array[i] <= array[pivot])
			i++;
		while (array[j] >= array[pivot] && j > start)
			j--;
		if (i > j)
		{
			temp = array[j];
			array[j] = array[pivot];
			array[pivot] = temp;
		}
		else
		{
			temp = array[j];
			array[j] = array[i];
			array[i] = temp;
		}
	}
	quickSort(array, start, j - 1);
	quickSort(array, j + 1, end);
}

int		main(void)
{
	int N, i;

	scanf("%d", &N);
	for (i = 0; i < N; i++)
	{
		scanf("%d", &array[i]);
		if (array[i] < 1 || array[i] > 1000000)
		{
			printf("값은 1보다 크거나 같고, 1,000,000보다 작거나 같아야 합니다.");
			return (0);
		}
	}
	quickSort(array, 0, N - 1);
	for (i = 0; i < N; i++)
		printf("%d\n", array[i]);
	return (0);
}
