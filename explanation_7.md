# HTTPRouter using a Trie

## Algorithm
This is a straight-forward implementation using a Trie data structure.

The implementation allows us to add a route with a handler. The route can
be a deep path separated by slashes(/) and only the final path component
will have a handler associated.

This will also allow us to return the handler given any path and return a 
default / catchall handler if the path has not been added to the router.

## Time Complexity

### Insertion
Insertion of a single path suffix is done in `O(1)` time since it involved only
adding one node to the trie.\
For a deep path with `n` components, the insertion is done in `O(n)` time.

### Lookup
Lookup happens by going down the trie until the leaf path is found. If a 
section of the path is not found, then the default handler or None is returned.

Time complexity for this is `O(n)` where there are `n` components to the path.

## Space Complexity

The router will have to create a new trie node for every section of the path
and an additional string to store the handler (or None) for each section.

For a single route where the path has `n` components the space used is `O(n)`.
