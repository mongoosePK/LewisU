/*
William Pulkownik
z1805341
csci 340_003 
Assignment 5
assignment5.cc

*/
#include <iostream>
#include <iomanip>
#include <algorithm>
#include <vector>
#include "assignment5.h"
using namespace std;

const int MAX_SIZE = 40;
const int MAX_COUNT = 40;
const int WIDTH = 5;
const int ROW_SIZE = 8;

int mcount = 0;
int rcount = 0;

void display(int d) {
	if (mcount < MAX_COUNT) {
		cout << setw(WIDTH) << d;
		mcount++;
		rcount++;
		if (rcount == ROW_SIZE) {
			cout << endl;
			rcount = 0;
		}
	}
}

/****************	begin binTree definitions   ************/
// the binTree height function checks if r is
// null. it returns -1 if true and traverses
// both branches returning 1 + the highest of branches
int binTree::height() const
{
	return height(root);
}
int binTree::height(Node* r) const
{
	return (!r ? -1 : 1 + std::max(height(r->left), height(r->right)));
}
// binTree::size traverses whole tree returns the number of nodes
unsigned binTree::size() const
{
	return size(root);
}
unsigned binTree::size(Node* r) const
{
	return (!r ? 0 : 1 + size(r->left) + size(r->right));
}
// binTree::inorder visits each node on the left, depth-first
// then each right node, depth-first
void binTree::inorder(void(*p)(int))
{
	inorder(root, p);
}
void binTree::inorder(Node* r, void(*p)(int))
{
	if (r != nullptr)
	{
		inorder(r->left, p);
		p(r->value);
		inorder(r->right, p);
	}
}
// binTree::preorder visits the left branches top down, 
// then the right-side children of those nodes. 
void binTree::preorder(void(*p)(int))
{
	preorder(root, p);
}
void binTree::preorder(Node* r, void(*p)(int))
{
	if (r != nullptr)
	{
		p(r->value);
		preorder(r->left, p);
		preorder(r->right, p);
	}
}
// binTree::postorder visits the 
// right side children depth first then the left
void binTree::postorder(void(*p)(int))
{
	postorder(root, p);
}
void binTree::postorder(Node* r, void(*p)(int))
{
	if (r != nullptr)
	{
		postorder(r->left, p);
		postorder(r->right, p);
		p(r->value);
	}
}
/*
	insert creates a new node from the int value
	it then inserts the node into the tree as follows
	1) if ROOT == NULL -> set root to new node
	2) if right tree shorter than left, right == new node
	3) else left == new node
*/
void binTree::insert(int x)
{
	insert(root, x);
}
void binTree::insert(Node*& r, int x)
{
	
	Node* n = nullptr;
	n = new Node(x);
	if (r == nullptr)
		r = n;
	else if (height(r->right) < height(r->left))
		insert(r->right, x);
	else
		insert(r->left, x);
}

#define BINTREE_MAIN
#ifdef BINTREE_MAIN
int main() {
	vector<int> v(MAX_SIZE);
	for (int i = 1; i<MAX_SIZE; i++)
		v[i] = i;
	random_shuffle(v.begin(), v.end());

	binTree bt;
	vector<int>::iterator it;
	for (it = v.begin(); it != v.end(); it++)
		bt.insert(*it);

	cout << "Height: " << bt.height() << endl;
	cout << "Size: " << bt.size() << endl;
	cout << "In order traverse (displaying first " << MAX_COUNT << " numbers): \n";
	mcount = rcount = 0;
	bt.inorder(display);
	cout << "\n\nPre order traverse (displaying first " << MAX_COUNT << " numbers): \n";
	mcount = rcount = 0;
	bt.preorder(display);
	cout << "\n\nPost order traverse (displaying first " << MAX_COUNT << " numbers): \n";
	mcount = rcount = 0;
	bt.postorder(display);

	cout << endl;
	return 0;
}

#endif
