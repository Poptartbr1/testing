#include "heap.h"

void heap::bubbleUp(int p)
{
	int poz = p;
	int elem = this->elems[p];
	int parent = p / 2;
	while (poz > 1 and elem > this->elems[parent])
	{
		this->elems[poz] = this->elems[parent];
		poz = parent;
		parent = poz / 2;
	}
	this->elems[poz] = elem;
}

void heap::add(TElem e)
{
	//if (this->len == this->cap)
		//return;

	this->elems[this->len + 1] = e;
	this->len = this->len + 1;
	bubbleUp(this->len);
}

void heap::remove()
{
	if (this->len == 0)
		return;
	//return element sters
	this->elems[1] = this->elems[this->len];
	this->len = this->len - 1;
	bubbleDown(1);
}

void heap::bubbleDown(int p)
{
	int poz = p;
	int elem = this->elems[p];
	while (poz < this->len)
	{
		int maxChild = -1;
		if (poz * 2 <= this->len)
			maxChild = poz * 2;
		if (poz * 2 + 1 <= this->len and this->elems[2 * poz + 1] > this->elems[2 * poz])
			maxChild = poz * 2 + 1;
		if (maxChild != -1 and this->elems[maxChild] > elem)
		{
			int tmp = this->elems[poz];
			this->elems[poz] = this->elems[maxChild];
			this->elems[maxChild] = tmp;
			poz = maxChild;
		}
		else
			poz = this->len + 1;
	}
}

heap::~heap()
{
}
