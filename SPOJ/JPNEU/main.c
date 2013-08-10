#include <stdio.h>


int main (void)
{

	int actual = 0;
	int aimed = 0;
	while (scanf("%d", &actual) != EOF)
	{
		scanf("%d", &aimed);
		printf("%d\n", actual-aimed);
	}


	return 0;
}