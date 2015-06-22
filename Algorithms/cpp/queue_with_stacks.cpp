#include <iostream>
#include <stack>
#include <queue>

using namespace std;

class queue_with_stacks
{
	stack<int> stack_in, stack_out;
public:
	queue_with_stacks();
	~queue_with_stacks();

	void enqueue(int);
	int dequeue();
};

queue_with_stacks::queue_with_stacks() {}
queue_with_stacks::~queue_with_stacks(){}

void queue_with_stacks::enqueue(int element)
{
	this->stack_in.push(element);
}
int queue_with_stacks::dequeue()
{
	int element;
	if (this->stack_out.empty())
	{
		while (!this->stack_in.empty())
		{
			this->stack_out.push(this->stack_in.top());
			this->stack_in.pop();
		}
	}
	if (!this->stack_out.empty())
	{
		element = this->stack_out.top();
		this->stack_out.pop();
		return element;
	}
	else
	{
		cout << "Queue is empty" << endl;
		return -1;
	}

}


int main(int argc, char ** argv)
{
	queue_with_stacks q;
	q.enqueue(1);
	q.enqueue(2);
	cout << q.dequeue() << endl;
	q.enqueue(3);
	q.enqueue(4);
	cout << q.dequeue() << endl;
	cout << q.dequeue() << endl;
	cout << q.dequeue() << endl;
	return 1;
}