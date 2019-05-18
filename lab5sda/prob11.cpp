#include "p11.h"
#include "heap.h"
void removeMin(list<TElem>& elements, int k)
{
	if (k <= 0)
		throw std::exception();
	heap hp;
	int p = 0,current;
	list<TElem> secondary;
	for (auto it = elements.begin(); it != elements.end(); ++it)
	{
		if (p < k)
		{
			hp.add(*it);
			p++;
		}
		else
		{
			current = *it;
			if (hp.getRoot() > current)
			{
				secondary.push_back(hp.getRoot());
				hp.remove();
				hp.add(current);
			}
			else
			{
				secondary.push_back(current);
			}
		}
	}
	elements = secondary;
}