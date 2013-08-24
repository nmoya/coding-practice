#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>


int compareFunc (const void * a, const void * b)
{
  if ( *(int*)a <  *(int*)b ) return -1;
  if ( *(int*)a == *(int*)b ) return 0;
  if ( *(int*)a >  *(int*)b ) return 1;
}
//memset(array, value, sizeof(int)*3000);
//qsort(array, lenght, sizeof(int), compareFunc);

int main (void) 
{
	int i, N, j;
	int Q;
	int flag = 0;
	while (scanf("%d", &N) != EOF)
	{
		//Initialize

		for (i = 0; i<N; i++)
		{
			//Your code here
			//scanf("%d", &Q);
		}

		
		//Results
		printf("\n");

		
	
	}
	return 0;
}