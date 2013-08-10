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

int main (void) 
{
	int i, N, j;
	while (scanf("%d", &N) != EOF)
	{
		printf("%d\n", N*N);		
	
	}
	return 0;
}
