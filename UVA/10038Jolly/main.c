#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int myCompare (const void * a, const void * b)
{
  if ( *(int*)a <  *(int*)b ) return -1;
  if ( *(int*)a == *(int*)b ) return 0;
  if ( *(int*)a >  *(int*)b ) return 1;
}

int main (void) 
{
	int N, i;
	int vetor[3000];
	int diferencas[3000];
	int proximo = 0;
	while (scanf("%d", &N) != EOF)
	{
		memset(diferencas, 0, sizeof(int)*3000);
		int jolly = 1;
		proximo = 0;
		
		for (i = 0; i < N ; i++)
			scanf("%d", &vetor[i]);
		
		for (i = 0; i < N-1 ; i++)
		{
			diferencas[proximo] = abs(vetor[i] - vetor[i+1]);
			proximo++;
		}
		
		qsort(diferencas, 3000, sizeof(int), myCompare);
		i = 3000 - (N-1);
		proximo = 1;
		for ( ; i < 3000 ; i++)
		{
			//printf("I:  %d, Dif: %d, Prox: %d\n", i, diferencas[i], proximo);
			if (proximo != diferencas[i])
			{
				jolly = 0;
				break;
			}
			proximo++;
		}
		if (jolly)
			printf("Jolly\n");
		else
			printf("Not jolly\n");
	
	}
	return 0;
}