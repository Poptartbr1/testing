#include "p11.h"
#include "tests.h"
#include <assert.h>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;


list<TElem> getRandom(int from, int to, int middle, int k, int all) {
	vector<int> v;
	for (int i = 0; i < k; i++) {
		int nr = (rand() % (middle - from)) + from;
		v.push_back(nr);
	}
	for (int i = k; i < all; i++) {
		int nr = (rand() % (to - middle) + middle + 1);
		v.push_back(nr);
	}
	random_shuffle(v.begin(), v.end());
	list<TElem> result;
	for (auto it = v.begin(); it != v.end(); it++) {
		result.push_back(*it);
	}
	return result;
}

void check(list<TElem> l, int from, int to, int middle, int k, int all, list<TElem> orig) {
	assert(l.size() == max(0, all - k));
	for (list<TElem>::iterator it = l.begin(); it != l.end(); it++) {
		assert(*it > middle);
		auto i = find(orig.begin(), orig.end(), *it);
		assert(i != orig.end());
	}
}


void testException() {
	list<TElem> l = { 5, 1, 9, 10, 4, 2 };
	try {
		removeMin(l, -5);
		assert(false);
	}
	catch (exception&) {
		assert(true);
	}
	try {
		removeMin(l, 0);
		assert(false);
	}
	catch (exception&) {
		assert(true);
	}
	removeMin(l, 10);
	assert(l.size() == 0);
}

void testP11() {
	testException();

	for (int lower = 10; lower < 1000; lower += 100) {
		for (int upper = 100; upper < 2000; upper += 200) {
			cout << lower << " " << upper << endl;
			for (int k = 1; k < 50; k = k + 5) {
				int middle = (lower + upper) / 2;
				list<TElem> l = getRandom(lower, upper, middle, k, upper - lower + 1);
				list<TElem> orig = l;
				removeMin(l, k);
				check(l, lower, upper, (lower + upper) / 2, k, upper - lower + 1, orig);

			}
		}
	}
}


