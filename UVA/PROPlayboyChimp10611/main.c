#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int myCompare (const void * a, const void * b)
{
  if ( *(int*)a <  *(int*)b ) return -1;
  if ( *(int*)a == *(int*)b ) return 0;
  if ( *(int*)a >  *(int*)b ) return 1;
}
//memset(diferencas, 0, sizeof(int)*3000);
int binSearch (int *vet, int tamVet, int query)
{
	int begin = 0;
	int end = tamVet;
	
	while (end >= begin)
	{
		//printf("Begin: %d, End: %d\n", begin, end);
		int middle = (begin+end) / 2;
		if (vet[middle] == query)
			return middle;
		else if (query < vet[middle])
			end = middle -1;
		else
			begin = middle+1;
	}
	return begin;
}

int main (void) 
{
	int i, N, j, Q, k;
	int query;
	int fila [50000];
	int index = 0;
	int inf, sup;
	int previous;

	while (scanf("%d", &N) != EOF)
	{
		index = 0;
		inf = 0;
		sup = 0;
		
		for (i = 0; i<N; i++)
			scanf("%d", &fila[i]);
		
		qsort(fila, N, sizeof(int), myCompare);
		
		scanf("%d\n", &Q);
		for (i = 0; i<Q; i++)
		{	
			scanf("%d", &query);
			index = binSearch(fila, N, query);
			//printf("Index: %d\n", index);
			previous = fila[index];
			inf = -1;
			sup = -1;
			if (index-1 <= 0 && query != fila[index])
				inf = previous;
			else
			{
				for (k = index-1 ; k >= 0 ; k--)
				{
					if (fila[k] != previous)
					{
						inf = fila[k];
						break;
					}				
				}
			}
			//printf("Fila na pos index: %d\n", fila[index]);
			//printf("Previous: %d\n", previous);
			if (index+1 == N && query != fila[index])
				sup = previous;
			else
			{
				for (k = index+1 ; k < N ; k++)
				{

					if (fila[k] != previous)
					{
						sup = fila[k];
						if (k+1 == N)
							sup = fila[k];
						break;
					}		
				}				
			}
			
			if (inf == -1)
				printf("x %d\n", sup);
			else if (sup == -1)
				printf("%d x\n", inf);
			else
				printf("%d %d\n", inf, sup);
			
		}
		
	
	}
	return 0;
}