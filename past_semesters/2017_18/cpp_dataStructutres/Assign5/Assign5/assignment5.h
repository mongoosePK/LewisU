/*
William Pulkownik
z1805341
csci 340_003
Assignment 5
assignment5.cc

*/

#ifndef ASSIGNMENT5_H
#define ASSIGNMENT5_H

class binTree;
class BST;

class Node {
	friend class binTree;
private:
	int value;
	Node* left;
	Node* right;
	
public:
	Node() { left = right = nullptr; } //constructors
	Node(int val) { left = nullptr, right = nullptr, 
		value = val; }
};

class binTree {
public:
	binTree() { root = nullptr; }
	virtual void insert(int);
	int height() const;
	unsigned size() const;
	void inorder(void(*)(int));
	void preorder(void(*)(int));
	void postorder(void(*)(int));
	

protected:
	Node* root;

private:
	void insert(Node*&, int);
	int height(Node*) const;
	unsigned size(Node*) const;
	void inorder(Node*, void(*)(int));
	void preorder(Node*, void(*)(int));
	void postorder(Node*, void(*)(int));
};

#endif




