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
        for (i = 0; i < N ; i++)
        {
            j = 0;
            int old;
            float prob = 0;
            float nguess = 0;
            float times_per_number = 0;
            scanf("%d\n", &j);
            old= j;
            while (j > 0)
            {
                nguess = nguess + old / (j * 1.0);
                j--;
            }
            printf("%.2f\n", nguess);
        }
	
	}
	return 0;
}
