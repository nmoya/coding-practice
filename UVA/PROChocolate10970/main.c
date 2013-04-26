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

int divideEmN(int M, int N)
{
	//printf("Invocando com M = %d e N = %d\n", M, N);
	if (N == 1)
		return 0;
	else if (N % 2 == 0)	//Se o numero de linhas for par
	{
		return 1 + divideEmN(M, N-1);
	}
	else //Se o numero de linhas for impar.
	{
		return 1 + divideEmN(M, N-1);
	}
}

int divideEmM(int M, int N)
{
	if (M == 1)
		return 0;
	else if (M % 2 == 0)	//Se o numero de linhas for par
	{
		return 1 + divideEmM(M-1, N);
	}
	else //Se o numero de linhas for impar.
	{
		return 1 + divideEmM(M-1, N);
	}
}
	

int main (void) 
{
	int i, j;
	int N, M;
	int numeroLinhas = 0;
	int numeroDivisoes = 0;
	int numeroDivisaoPorLinha = 0;
	while (scanf("%d %d", &M, &N) != EOF)
	{
		//printf("--------\n");
		
		numeroLinhas = divideEmM(M, N);
		numeroDivisaoPorLinha = divideEmN(M, N);
		//printf("Numero de Linhas: %d\n", numeroLinhas);
		//printf("Numero de divisao por linha: %d\n", numeroDivisaoPorLinha);
		numeroDivisoes = numeroLinhas * N + numeroDivisaoPorLinha;
		
		printf("%d\n", numeroDivisoes);
		
	}
	return 0;
}
