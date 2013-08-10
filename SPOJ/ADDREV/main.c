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


char n1r[1000];
char n2r[1000];

char * reverse1 (int n)
{
    char n1[1000];
    char reversen1[1000];
    sprintf(n1, "%d" , n);    
    int counter = 0;
    int j;
    for (j = strlen(n1) ; j>= 0; j--)
    {
        reversen1[counter] = n1[j];
        counter++;
    }
    strcpy(reversen1, n1r);
}
char * reverse2 (int n)
{
    char n1[1000];
    char reversen1[1000];
    sprintf(n1, "%d" , n);    
    int counter = 0;
    int j;
    for (j = strlen(n1) ; j>= 0; j--)
    {
        reversen1[counter] = n1[j];
        counter++;
    }
    strcpy(reversen1, n2r);
}

int main (void) 
{
	int i, N, j;
	while (scanf("%d", &N) != EOF)
	{
        for (i = 0; i < N ; i++)
        {
            int num1;
            int num2;
            scanf("%d %d\n", &num1, &num2);

            reverse1(num1);
            reverse2(num2);
            
            int sum = atoi(n1r) + atoi(n2r);

            reverse1(sum);

            printf("%s\n", n1r);
            
        }
	
	}
	return 0;
}
