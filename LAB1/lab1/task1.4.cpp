// https://en.wikipedia.org/wiki/Disjoint-set_data_structure

//  Implement a data structure to handle disjunct sets. When the data structure is created, all elements are in their own sets. Your implementation should at least support the following operations:
// 
//     union(int a, int b) - merge the sets containing the elements a and b
//     boolean same(int a, int b) - test whether a and b are in the same set
// 
// Recommended time complexity: amortized O(log n) for both operations, where n is the total number of elements.
// 
// Warning: You are expected to produce a lot of output data for this problem. Make sure that you don't flush the output buffer after each line, since this might make your otherwise correct solution too slow. 

#include <vector>

struct Node {
	Node* parent; //NULL if root
	int size;
	
	Node(Node* parent, int size) : parent{parent}, size{size} {};
};

struct DisjointSet {
	// I THINK this should suffice
	std::vector<Node> trees;
};

// Making new sets
// 
// function MakeSet(x) is
//     if x is not already in the forest then
//         x.parent := x
//         x.size := 1     // if nodes store size
//         x.rank := 0     // if nodes store rank
//     end if
// end function

// Find
// 
// function Find(x) is
//     if x.parent ≠ x then
//         x.parent := Find(x.parent)
//         return x.parent
//     else
//         return x
//     end if
// end function

// Merge two sets (union by size?)
//
//function Union(x, y) is
    // Replace nodes by roots
    // x := Find(x)
    // y := Find(y)

    // if x = y then
    //     return  // x and y are already in the same set
    // end if

    // // If necessary, swap variables to ensure that
    // // x has at least as many descendants as y
    // if x.size < y.size then
    //     (x, y) := (y, x)
    // end if

    // // Make x the new root
    // y.parent := x
    // // Update the size of x
    // x.size := x.size + y.size
// end function
