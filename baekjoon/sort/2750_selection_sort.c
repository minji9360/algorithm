#include <stdio.h>

int		main(void)
{
	/* N개의 수가 주어졌다는 말에 꽂혀서 N의 수에 따라 array를 할당하려고 했다.
	 * N을 입력받은 후 array를 정의해줘야 했는데 그러면 array는 선언부에 선언을 할 수 없었다. 
	 * 동빈나님께서 array를 1001로 정의하는 걸 보고 나는 동적할당을 사용해야 하는 생각을 했구나,  예전에 42 seoul에서 했던 malloc이 생각나면서 정신이 번쩍 들었다. */
	int array[1001];
	int N, i, j, min, index, temp;
	
	scanf("%d", &N);
	for (i = 0; i < N; i++)
	{
		scanf("%d", &array[i]);
		if (array[i] > 1000 || array[i] < 1)
		{
			printf("입력 값의 범위를 확인해주세요");
			return (0);
		}
	}
	for (i = 0; i < N; i++)
	{
		min = 1001;
		for (j = i; j < N; j++)
			if (array[j] < min)
			{
				min = array[j]; /* array[j]를 array[i]로 해서 값이 미묘하게 정렬이 안됐다.
								현재 탐색하는 값이 최소값보다 작으면 최소값을 바꿔주고*/
				index = j; /* 최소값을 가진 배열의 순서를 index에 저장해야 하니까
							i로 하면 0부터 전체를 반복하는 횟수가 되기 때문에 틀리는 것 */
			}
		temp = array[index];
		array[index] = array[i];
		array[i] = temp;
	}
	for (i = 0; i < N; i++)
		printf("%d\n", array[i]);
	return (0);
}

