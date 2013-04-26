#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int myCompareChar (const void * a, const void * b)
{
  if ( *(int*)a <  *(int*)b ) return -1;
  if ( *(int*)a == *(int*)b ) return 0;
  if ( *(int*)a >  *(int*)b ) return 1;
}
//memset(diferencas, 0, sizeof(int)*3000);



int main (void) 
{	
	int i, j, k, N;
	int aux;
	char texto[200];
	char saida[26];
	int counter = 0;
	int previous;
	int max = 0;


	while (scanf("%d\n", &N) != EOF)
	{
		printf("%d\n", N);
		for (i=0; i < N; i++)
		{
			printf("I, N: %d %d\n", i, N);
		}
	}
	return 0;
}

/*
			saida[0] = '\0';
			texto[0] = '\0';
			printf("I, N: %d %d\n", i, N);
			gets(texto);
			if (strlen(texto) == 1)
				break;
			printf("Tam: %d\n", strlen(texto));
			for (aux = 0; aux < strlen(texto); aux++)
				printf("%c", texto[aux]);
			
			qsort(texto, strlen(texto), sizeof(char), myCompareChar);
			max = 0;
			counter = 0;
			previous = tolower(texto[0]);
			for (j = 0; j < strlen(texto); j++)
			{
				if (previous == tolower(texto[j]))
					counter+=1;
				else
				{
					if (counter > max)
						max = counter;
					counter = 0;
				}
				previous = tolower(texto[j]);
			}
			counter = 0;
			previous = texto[j];
			k = 0;
			for (j = 0; j < strlen(texto); j++)
			{
				if (previous == tolower(texto[j]))
					counter+=1;
				else
				{
					if (counter == max)
					{ 
						saida[k] = previous;
						k++;
					}
				}
				previous = tolower(texto[j]);
			}
			saida[k] = '\0';
			for (j = 0; j < strlen(saida); j++)
				printf("%c", saida[j]);
			printf("\n");*/
