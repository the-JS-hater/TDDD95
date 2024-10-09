// https://en.wikipedia.org/wiki/Disjoint-set_data_structure

//  Implement a data structure to handle disjunct sets. When the data structure is created, all elements are in their own sets. Your implementation should at least support the following operations:
// 
//     union(int a, int b) - merge the sets containing the elements a and b
//     boolean same(int a, int b) - test whether a and b are in the same set
// 
// Recommended time complexity: amortized O(log n) for both operations, where n is the total number of elements.
// 
// Warning: You are expected to produce a lot of output data for this problem. Make sure that you don't flush the output buffer after each line, since this might make your otherwise correct solution too slow. 


// Each node in a disjoint-set forest consists of a pointer and some auxiliary information, either a size or a rank (but not both). The pointers are used to make parent pointer trees, where each node that is not the root of a tree points to its parent. To distinguish root nodes from others, their parent pointers have invalid values, such as a circular reference to the node or a sentinel value. Each tree represents a set stored in the forest, with the members of the set being the nodes in the tree. Root nodes provide set representatives: Two nodes are in the same set if and only if the roots of the trees containing the nodes are equal.
// 
// Nodes in the forest can be stored in any way convenient to the application, but a common technique is to store them in an array. In this case, parents can be indicated by their array index. Every array entry requires Θ(log n) bits of storage for the parent pointer. A comparable or lesser amount of storage is required for the rest of the entry, so the number of bits required to store the forest is Θ(n log n). If an implementation uses fixed size nodes (thereby limiting the maximum size of the forest that can be stored), then the necessary storage is linear in n. 

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
