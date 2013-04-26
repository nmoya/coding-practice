#include <stdio.h>
#include <stdlib.h>
#include <string.h>



int main (void) 
{
	int i, j;
	int N, M;
	int numeroLinhas = 0;
	int numeroDivisoes = 0;
	int numeroDivisaoPorLinha = 0;
	while (scanf("%d %d", &M, &N) != EOF)
	{
		
		numeroLinhas = M-1;		
		numeroDivisaoPorLinha = N-1;		
		numeroDivisoes = numeroLinhas * N + numeroDivisaoPorLinha;
		
		printf("%d\n", numeroDivisoes);
		
	}
	return 0;
}
