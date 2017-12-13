import copy


class TreeNode(object):
    def __init__(self, tree, parent, title, string):
        self.tree = tree
        self.title = title
        self.parent = parent
        self.string = string
        self.children = []
        self.adoptive_parents = []
        if self in self.tree:
            raise ValueError("Node already on this tree level")
        if self.parent:
            self.parent._add_child(self)
        self.tree.tree.append(self)

    def __repr__(self):
        if self.parent:
            par = self.parent.title
        else:
            par = None
        return ("{ title: " + str(self.title) +
                ", string: " + str(self.string) +
                ", parent: " + str(par) +
                ", children: " + str([child.title for child in self.children]) +
                ", adoptive_parents: " + str([parent.title for parent in self.adoptive_parents]) + "}")

    def __hash__(self):
        return hash(str(self))

    def __eq__(self, other):
        return (self.title is other.title and
                self.parent is other.parent and
                self.children == other.children)

    def get_path(self):
        """Returns the path to this node"""
        path = []
        node = self
        while node is not self.tree.root:
            path.append(node.title)
            node = node.parent
        path.reverse()
        return ".".join(path)

    def add_child(self, title, string):
        """Adds a child to this node and to this nodes tree"""
        path = self.get_path()
        if path:
            path += "." + title
        else:
            path = self.tree.root.title
        return self.tree.add_node(path, string)

    def _add_child(self, child):
        self.children.append(child)
        return child

    def get_child(self, title):
        """Returns the child of this node with the title"""
        kid = None
        for i in self.children:  # Find the child by title
            if i.title == title:
                kid = i
        return kid

    def remove_child(self, title):
        node = self.get_child(title)
        if not node:
            raise ValueError("Child does not exist")
        return self.tree.remove_node(node.title)

    def _remove_child(self, child):
        kid = self.get_child(child)
        if not kid:
            raise ValueError("Child must be a child of this node")
        if len(kid.children):  # Add child's children to this node
            for i in kid.children:
                if i in self.children:
                    raise ValueError("A child of the removed node is already a child of the parent node")
                self.children.append(i)
                i.parent = self
        self.children.remove(kid)
        return kid

    def get_biological_children(self):
        """Returns a list of this nodes children that are directly created from this node"""
        return [child for child in self.children if child.parent is self]

    def add_adopted_child(self, child):
        path = self.get_path()
        if not path:
            path = self.tree.root.title
        self.tree.add_adopted_child(path, child)

    def get_adopted_children(self):
        return [child for child in self.children if child.parent is not self]

    def remove_adopted_child(self, title):
        path = self.get_path()
        if not path:
            path = self.tree.root.title
        self.tree.remove_adopted_child(path, title)

    def get_lineage(self):
        lineage = []
        start = self
        tree_node = self
        while tree_node is not start or not set(tree_node.children).issubset(lineage):
            count = 0
            for node in tree_node.children:
                if node in lineage and node.parent is tree_node:
                    count += 1
            if count == len(tree_node.get_biological_children()):
                lineage.append(tree_node)
                tree_node = tree_node.parent
            else:
                for node in tree_node.children:
                    if node not in lineage and node.parent is tree_node:
                        tree_node = node
        lineage.reverse()
        return lineage

    def remove_lineage(self):
        path = self.get_path()
        if not path:
            path = self.tree.root.title
        return self.tree.remove_lineage(path)

    def _remove_lineage(self):
        lineage = []
        start = self
        tree_node = self
        while tree_node is not start or not set(tree_node.children).issubset(lineage):
            children = copy.copy(tree_node.children)
            for node in children:
                if node.parent is not tree_node:
                    self.tree.remove_adopted_child(tree_node.title, node.title)
            count = len(set(tree_node.children).intersection(lineage))
            if count == len(tree_node.children):
                lineage.append(tree_node)
                tree_node.parent.children.remove(tree_node)  # Remove this node from its parent
                tree_node = tree_node.parent
            else:
                for node in tree_node.children:
                    if node not in lineage:
                        tree_node = node
        lineage.reverse()
        return lineage


class Tree(object):
    def __init__(self):
        self.tree = []
        self.root = TreeNode(self, None, "root", None)

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        if self.i < len(self.tree):
            self.i += 1
            return self.tree[self.i - 1]
        else:
            raise StopIteration

    def __hash__(self):
        return hash(repr(self))

    def __repr__(self):
        return repr(self.tree)

    def __str__(self):
        return "\n".join([str(node) for node in self.tree])

    def add_node(self, path, title, string=None):
        parent = self.get_node(path)
        kid = TreeNode(self, parent, title, string)
        return kid

    def get_node(self, path):
        parents = path.split(".")
        tree_node = None
        for i in self.tree:  # Get the first node in path
            if i.title == parents[0]:
                tree_node = i
                break
        if not tree_node:
            raise ValueError('Invalid Path: "' + path + '"')
        parents.remove(tree_node.title)
        for i in parents:  # Loop through the path
            tree_node = tree_node.get_child(i)
            if not tree_node:
                raise ValueError("Node does not exist, possibly invalid path")
        return tree_node

    def remove_node(self, path):
        tree_node = self.get_node(path)
        if tree_node is self.root:
            raise ValueError("Can not remove tree root")
        parent = tree_node.parent
        # Will stop looping early if list is changed while looping
        adoptive_parents = copy.copy(tree_node.adoptive_parents)
        for node in adoptive_parents:
            self.remove_adopted_child(node.title, tree_node.title)
        parent._remove_child(tree_node.title)
        self.tree.remove(tree_node)
        return tree_node

    def get_children(self, path):
        return self.get_node(path).children

    def get_biological_children(self, path):
        return self.get_node(path).get_biological_children()

    def add_adopted_child(self, path, child):
        first = self.get_node(path)
        second = self.get_node(child)
        if second in first.children:
            raise ValueError("Child already connected to this node")
        if second is self.root:
            raise ValueError("Can not connect node to root")
        first.children.append(second)
        second.adoptive_parents.append(first)

    def get_adopted_children(self, path):
        return self.get_node(path).get_adopted_children()

    def remove_adopted_child(self, path, child):
        first = self.get_node(path)
        second = self.get_node(child)
        if first is second.parent:
            raise ValueError("Can not disconnect parent from child")
        first.children.remove(second)
        second.adoptive_parents.remove(first)

    def get_lineage(self, path):
        return self.get_node(path).get_lineage()

    def remove_lineage(self, path):
        tree_node = self.get_node(path)
        lineage = tree_node._remove_lineage()
        self.tree = [i for i in self.tree if i not in lineage]
        return lineage
