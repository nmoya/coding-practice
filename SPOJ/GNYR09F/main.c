#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>


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
            int id=0, sizen = 0, adj = 0;
            scanf("%d %d %d\n", &id, &sizen, &adj);
            int sum =0;


            for (j = 2 ; j <= adj + 1; j++)
            {
                int nfits = 0;
                int remaining = 0;
                nfits = (int) sizen / j;
                remaining = sizen - (nfits * j);
                printf("%d %d %d \n", j, nfits, remaining);
                sum = sum + (int) pow(2,remaining);
            }
            printf("%d\n", sum);
        }
	
	}
	return 0;
}
