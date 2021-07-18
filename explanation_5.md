# Autocomplete with Tries

## Algorithm
The dictionary of words is stored in a Trie data structure.

The following are the key operations that are made on the Trie

### Insert a word
This involves creating a new node for every character in the word and marking
the final node as a `word`.

#### Time Complexity
We have to go through each letter in the word and create a new node in a dictionary
for the letter. For a word of length `n`, then time taken is `O(n)`.

#### Space Complexity
For each character in the word, 1) the character itself is stored, 2) a node
with a boolean value is stored, 3) an empty dictionary is created.

Since a fixed number of elements are created for each letter, the space required 
for a word of length `n` is `O(n)`.

### Find a prefix
This involves walking down the Trie data strcuture from the root until all the
characters of the word are found. The corresponding node when we have reached 
the end is returned.

#### Time Complexity
Every iteration to walk down the Trie happens in constant time. In order to 
search for a word of length `n`, it will take a worst case of `O(n)` time.

#### Space Complexity
The iterations to walk down the Trie happens in memory, and the existing node
reference is what is returned. A couple of book-keeping references are used
for the loops and is independent of the size of the word. Hence space complexity
is linear `O(1)`

### Find all suffixes
Starting from the given node, all the possible words need to be identified. This
is done by recursively walking down all the paths of the Trie data structure 
from the given node.

#### Time Complexity
In the worst case, if we were to start from the root, the entire Trie will have
to be traversed. Also in the worst case if there are no common substring between
the words then all the words have to be traversed. 

Hence worst case time complexity will be `O(m*n)` where `n` is the average length
of each word and `m` is the total number of words in the Trie.

### Space Complexity
Similary, in the worst case, all the data has to be returned. This means that 
all the words have to be stred while recursing down the Trie. 

The worst case complexity then is `O(m*n)` where `n` is the average length
of each word and `m` is the total number of words in the Trie.
