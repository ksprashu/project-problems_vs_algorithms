"""Implements an HTTPRouter like you would find in a typical web server.

The purpose of an HTTP Router is to take a URL path like "/", "/about", 
or "/blog/2019-01-15/my-awesome-blog-post" and figure out what content 
to return. In a dynamic web server, the content will often come from a 
block of code called a handler.

This uses the Trie Data Structure
"""

import collections

# A RouteTrieNode will be similar to our autocomplete TrieNode... 
# with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, handler=None):
        # Initialize the node with children as before, plus a handler
        self.handler = handler
        self.children = collections.defaultdict(RouteTrieNode)

    def insert(self, path):
        # Insert the node as before
        return self.children[path]


# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, handler):
        # Initialize the trie with an root node and a handler, 
        # this is the root path or home page node
        self.root = RouteTrieNode(handler)

    def insert(self, route, handler):
        """Add paths of route recursively and handler to the leaf node.
        """
        node = self.root
        paths = self._get_paths_from_route(route)
        assert paths, 'cannot override root handler'

        for path in paths:
            node = node.children[path]
        node.handler = handler

    def find(self, route):
        """Starting at the root, navigate the Trie to find a match for this path
        Returns the handler for a match, or None for no match
        """
        node = self.root
        paths = self._get_paths_from_route(route)
        for path in paths:
            if not path in node.children:
                return None
            node = node.children[path]        
        return node

    def _get_paths_from_route(self, route):
        """Splits the route on / and return the paths.
        """
        assert route[0] == '/', 'route must be absolute (begin with /)'        
        # ignore first part of split which will be none for root
        return [r for r in route.split('/') if r]


# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, root_handler, not_found_handler = None):
        # Create a new RouteTrie for holding our routes
        self.trie = RouteTrie(root_handler)
        self.not_found_handler = not_found_handler

    def add_handler(self, route, handler):
        # Add a handler for a route
        self.trie.insert(route, handler)

    def lookup(self, route):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        node = self.trie.find(route)
        if not node or not node.handler:
            return self.not_found_handler
        return node.handler


# Test Cases
# ----------

# Basic tests
router1 = Router('root_handler', 'route_not_found')
print(router1.lookup('/'))
# root_handler
print(router1.lookup('/home'))
# route_not_found
router1.add_handler('/home', 'home_handler')
print(router1.lookup('/home'))
# home_handler

# Tests without catchall
router2 = Router('root_handler')
print(router2.lookup('/home'))
# None

# Test Deep path
router2.add_handler('/this/is/a/long/path/blog', 'blog_handler')
print(router2.lookup('/this/is/a/long/path'))
# None
print(router2.lookup('/this/is/a/long/path/blog'))
# blog_handler

# Test Bonus cases
router3 = Router('root_handler')
router3.add_handler('/about', 'about_handler')
print(router3.lookup('/about'))
# about_handler
print(router3.lookup('/about/'))
# about_handler

# Error Cases
try:
    print(router3.lookup('about'))
except AssertionError as e:
    print(e)
# route should be absolute (start with /)
try:
    print(router3.add_handler('/', 'new_handler'))
except AssertionError as e:
    print(e)
# cannot override root handler
