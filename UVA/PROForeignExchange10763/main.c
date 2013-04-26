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
	//int matriz[500000][500000];
	int caminhos[500000];
	int viajantes[500000];
	int flag = 0;
	int origem = 0;
	int destino = 0;
	while (scanf("%d", &N) != EOF)
	{
		for (i = 0; i < N; i++)
		{
			scanf("%d %d", &A, &B);
			viajantes[i] = A;
			caminhos[A] = B;
		}
		for (i = 0; i< N; i++)
		{
			origem = viajantes[i];
			destino = caminhos[origem];
			printf("Testando: %d -> %d\n", origem, destino);
			if (caminhos[destino] != origem)
			{
				printf("Sem caminho\n");
				flag = 1;
				break;
			}
		}
		if (flag == 1)
			printf("NO\n");
		else
			printf("YES\n");
	}
	return 0;
}
