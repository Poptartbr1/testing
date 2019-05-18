#pragma once
#include <utility>
#include <list>

using namespace std;

typedef int TElem;

//removes the smallest k elements from the list.
//if k is less than or equal to 0, it throws an exception
//if k is greater than the number of elements, all elements will be removed
void removeMin(list<TElem>& elements, int k);