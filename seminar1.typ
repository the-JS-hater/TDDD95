= GENERAL
- modern processor does ~ 4 * 10^9 CPU instructions per second
- so ~10^6 "lines of code" instructions per second. PROBABLY FINE!
- Labs greatly help with excercises. Labs are the tools
- check complexity, do the simple things first


= HELP!
- uneven string lengths cant match
- O(10^6)

- first, find a pattern-word pair, and replace in both strings (repeat)
- tripple nested for-loop will be just fine for complexity (probably)
- lastly replace pattern-pattern pairs remaining with basically anything
 
 
= LJUTNJA
- im a genius
 
 
= SPIDERMAN
- just do knapsacks lol
- "cant have gone down from 6 to 5", so backtracking through the matrix possible
- ">="
 
 
= ASPEN
- minimization/DP-problem
- always use Doubles (duh)
- HolesRemainingLeft x HolesRemainingRight matrix
- "never cross the streams"
- doeesnt matter how we fill the holes before
- min cost on the diagonal part i.e diff between left-right and right-left
- m[0][0] = 0 
- m[2000][2000] table size needed
 
 
= FENWICK
- Good idea to do
- very strict with documentation
- M * log N, M = nr. of ops
- + least significant bit that's 1, gives the next nodes index

