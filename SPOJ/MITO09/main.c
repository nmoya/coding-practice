#include <stdio.h>


int main (void)
{
	int matrix[1000][1000];
	int i, j;
	int N, x, y;
	int caiu = 0;
	while (scanf("%d", &N) != EOF)
	{
		caiu = 0;
		/*for (i = 0; i < N; i++)
			for (j= 0; j<N; j++)
				matrix[i][j] = 0;*/
		//printf("N: %d\n", N);
		for (i=0; i < N ; i++)
		{
			scanf("%d %d", &x, &y);
			if (matrix[x][y] == 0)
				matrix[x][y] = 1;
			else
				caiu = 1;
		}
		if (caiu)
			printf("1\n");
		else
			printf("0\n");
	}


	return 0;
}