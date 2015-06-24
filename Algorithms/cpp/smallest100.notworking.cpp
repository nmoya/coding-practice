#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

bool compare (const int &a, const int &b)
{
	return a>b;
}

int main(int argc, char **argv)
{
	int tmp, i;
	FILE *fp = NULL;
	vector<int> array;
	fp = fopen("hundred", "r");
	
	while(!feof(fp))
	{
		fscanf(fp, "%d\n", &tmp);
		array.push_back(tmp);
	}

	make_heap(array.begin(), array.end(), compare);

	for (i=0; i<10; i++)
	{
		cout << array.front() << endl;
		pop_heap(array.begin(), array.end());
		array.pop_back();
	}

}