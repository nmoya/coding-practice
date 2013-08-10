#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int myCompare (const void * a, const void * b)
{
  if ( *(int*)a <  *(int*)b ) return -1;
  if ( *(int*)a == *(int*)b ) return 0;
  if ( *(int*)a >  *(int*)b ) return 1;
  return 0;
}
//memset(diferencas, 0, sizeof(int)*3000);

int main (void) 
{
	int i, N, j;
	int A, B;
	int trocas[500000];
	while (scanf("%d", &N) != EOF)
	{
		if (N == 0)
			break;
		memset(trocas, 0, sizeof(int)*500000);
		for (i = 0; i < N; i++)
		{
			scanf("%d %d", &A, &B);
			//printf ("%d: %d %d\n", i, A, B);
			trocas[A]++;
			trocas[B]--;
		}
		for (i = 0; i< N; i++)
		{
			if (trocas[i] != 0)
			{
				printf("NO\n");	
				break;
			}
		}
		if (i == N)
			printf("YES\n");
	}
	return 0;
}
