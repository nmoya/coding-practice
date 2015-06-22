#include <iostream>

using namespace std;

int find_missing(int *original, int *shuffled, int size)
{
	int i;
	int sum1 = 0;
	int sum2 = 0;

	for (int i = 0; i < size; ++i)
		sum1+=original[i];

	for (int i = 0; i < size-1; ++i)
		sum2 += shuffled[i];
	return sum1-sum2;
}

int find_missing_xor(int *original, int *shuffled, int size)
{
	long xor1 = 0;
	int i;
	for (i = 0; i < size; ++i)
	{
		xor1 = xor1 ^ original[i];
		if (i < size-1)
			xor1 = xor1 ^ shuffled[i];
	}
	return xor1;
}

int main(int argc, char ** argv)
{
	int i;
	int input[] = {1, 1, 1, 3, 3, 3, 25, 25, 25, 88, 88, 88};
	int shuffled[] = {88, 1, 3, 25, 1, 3, 88, 3, 1, 25, 88};

	cout << find_missing(input, shuffled, 12) << endl;
	cout << find_missing_xor(input, shuffled, 12) << endl;

	return 1;
}