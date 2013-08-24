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
	int idades [100];
	int idadeAtual = 0;
	int nVezes = 0;
	int flag = 0;
	while (scanf("%d", &N) != EOF)
	{
		if (N == 0)
			break;
			
		nVezes = 0;
		idadeAtual = 0;
		
		for ( i = 0 ; i < 100 ;i++)
			idades[i] = 0;

		for (i = 0; i<N; i++)
		{
			scanf("%d", &idadeAtual);
			idades[idadeAtual-1]++;
		}

		int maior = 0;
		for (i=0 ; i<100; i++)
			if (idades[i] != 0)
				maior = i;
		for (i = 0; i<100; i++)
		{
			if (idades[i] != 0){
				for (j = 0; j < idades[i]-1; j++)
					printf("%d ", i+1);
				if (i == maior)
					printf("%d", i+1);
				else
					printf("%d ", i+1);	
			}
			
		}
		printf("\n");
	}
	return 0;
}