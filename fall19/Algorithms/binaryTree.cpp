// file: BinaryTree.cpp
//
# include <iostream>

using namespace std;

class IntBinaryTree
{
	public:
		struct TreeNode
		{
			int Value;
			TreeNode *Left;
			TreeNode *Right;
		};
		
		TreeNode *root;
		void destroySubTree(TreeNode *);
		void deleteNode(int, TreeNode *&);
		void makeDeletion(TreeNode *&);
		void displayInOrder(TreeNode *);
		void displayPreOrder(TreeNode *);
		
		void displayPostOrder(TreeNode *);
		
		//
		IntBinaryTree()  			//constructor
			{ root = NULL;}
		~IntBinaryTree()        	//destructor
			{destroySubTree(root);}
		void insertNode(int);
		bool searchNode(int);
		void remove(int);
		void showNodesInOrder()
			{ displayInOrder(root);}
		void showNodesPreOrder(void)
			{ displayPreOrder(root);}
		void showNodesPostOrder(void)
			{ displayPostOrder(root); }
						
};
void IntBinaryTree::displayInOrder(TreeNode *nodePtr)
{
	if (nodePtr == NULL)
		return;
	displayInOrder(nodePtr->Left);
	cout <<"\n" << nodePtr->Value << endl;
    displayInOrder(nodePtr->Right);
		
}
void IntBinaryTree::displayPostOrder(TreeNode *nodePtr)
{
	if (nodePtr == NULL)
		return;
	displayPostOrder(nodePtr->Left);
	displayPostOrder(nodePtr->Right);
	cout <<"\n" << nodePtr->Value << endl;		
}
void IntBinaryTree::displayPreOrder(TreeNode *nodePtr)
{
	if (nodePtr == NULL)
		return;
	cout <<"\n" << nodePtr->Value << endl;
	displayPreOrder(nodePtr->Left);
	displayPreOrder(nodePtr->Right);
		
}
void IntBinaryTree::destroySubTree(TreeNode *nodePtr)
{
	if(nodePtr == NULL)
		return;
	if (nodePtr->Left != NULL)
		destroySubTree(nodePtr->Left);
	if (nodePtr->Right !=NULL)
		destroySubTree(nodePtr->Right);
}
/*************************************************
**                                              **
**                 remove(int num)              **
**                                              **
**************************************************/
void IntBinaryTree::remove(int num)
{
	cout << "\ndeleteNode(num, root) not implemented. \n";
}

/*************************************************
**                                              **
**                 searchNode(int num)          **
**                                              **
**************************************************/
bool IntBinaryTree::searchNode(int num)
{
	TreeNode *nodePtr = root;
	while (nodePtr != NULL)
	{
			cout << "\nSearch num " << num << " not implemented \n";
			return false;
	}
	
}
void IntBinaryTree::insertNode(int num)
{
		TreeNode *newNode;
		TreeNode *ptr;
		cout << "\nEnter to insert ... "<< num << endl;
		newNode = new TreeNode;
		newNode->Value = num;
		newNode->Left = newNode->Right = NULL;
		
		if (root == NULL)
			root = newNode;
		else
		{
			ptr = root;
			while (ptr != NULL) //search for the num in the tree
			{
				if (num < ptr->Value)
				{
					if (ptr->Left != NULL)
						ptr = ptr->Left;
					else
					{
						ptr->Left = newNode;
						return;
					}
						
				}
				else if (num > ptr->Value)
					
					if(ptr->Right != NULL)
						ptr = ptr->Right;
					else
					{
						ptr->Right = newNode;
						return;
					}
				else
				{
					cout << "Duplicate  " << num << " found in the tree. \n";
					return;
				}
			}
		}
}

int main (void)
{
	IntBinaryTree treeA;
	treeA.insertNode(4);
	treeA.insertNode(5);
	treeA.insertNode(9);
	treeA.insertNode(4);
	treeA.insertNode(1);
	treeA.insertNode(-1);
	treeA.insertNode(-1);
	treeA.insertNode(1);
	cout <<"\nIn Order\n";
	treeA.showNodesInOrder();
	cout <<"Post Order\n";
	treeA.showNodesPostOrder()
	;
	cout <<"Pre Order\n";
	treeA.showNodesPreOrder();
	treeA.searchNode(9);
	treeA.remove(5);
}



