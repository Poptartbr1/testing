#pragma once
#include <iostream>
typedef int TElem;
class heap
{
private:
	int cap;
	int len;
	TElem* elems;
public:
	heap() {
		this->cap = 100;
		this->len = 0;
		this->elems = new TElem[this->cap];
	}
	void bubbleUp(int p);
	void bubbleDown(int p);
	void add(TElem e);
	void remove();
	int getRoot() { return this->elems[1]; }
	void print()
	{
		for (int i = 1; i <= this->len; i++)
		{
			std::cout << this->elems[i] << " ";
		}
	}
	~heap();
};

