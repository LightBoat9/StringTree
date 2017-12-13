.. toctree::
   :maxdepth: 1

.. _getting_started:

Getting Started
===============

Installation
------------

StringTree can be installed be running the setup.py file from terminal or command prompt

.. code-block:: python

    python setup.py install

Creating A Tree
---------------

To start simply create a :ref:`tree <tree>`

.. code-block:: python

   from string_tree import Tree

   tree = Tree()

This creates a :ref:`root <tree.root>` :ref:`TreeNode <treenode>` and adds it to the new Tree instance.

Adding to the Tree
------------------

So to add the first nodes use :ref:`add_node <tree.add_node>` on the path "root". Or use
:ref:`add_child <treenode.add_child>` on the root itself.

.. code-block:: python

   tree.add_node("root", "Foo", "Foo is a placeholder name")
   tree.root.add_child("Bar", "Bar is a placeholder name")

From here children can be added to those nodes and so on. Added nodes can be accessed by using :ref:`get_node <tree.get_node>`
more on accessing later.

.. code-block:: python

   tree.add_node("Foo", "Child", "Child of Foo")
   tree.get_node("Bar").add_child("Child", "Child of Bar")

Accessing nodes
---------------

Now that there are two nodes that are named ``Child`` they can no longer be accessed by just their title. If "Child"
was used as the path to that node it would always return Foo's Child and never Bar's because Foo was added to the Tree
first. To access Bar's child the full or partial path must be used.

.. code-block:: python

   # This will return Foo's Child
   tree.get_node("Child")

   # Both of these will return Bar's Child
   tree.get_node("root.Bar.Child")
   tree.get_node("Bar.Child")

   # It can also be accessed from the TreeNode itself
   bar = tree.get_node("Bar")
   bar.get_child("Child")

Accessing Contents
------------------

:ref:`get_string <tree.get_string>` can be used to access the contents of the TreeNode from a path. Or access the TreeNode's
:ref:`string <treenode.string>` property directly

.. code-block:: python

   tree.get_string("Foo")  # Will return "Foo is a placeholder name"
   tree.get_string("Foo.Child")  # Will return "Child of Foo"

   foo = tree.get_node("Foo")
   foo.string # "Foo is a placeholder name"
   foo_child = tree.get_node("Foo.Child")
   foo_child.string  # "Child of Foo"

Adopted Children
----------------

Normally each child noe has one parent. However, if it is possible to connect two paths in the tree by adding any node
as an adoptive parent to another node. The node's must have a unique title from all current
:ref:`children <treenode.children>` and can not be the :ref:`root <tree.root>` node. So Foo can not adopt "Bar.Child"
because Foo already has a node named "Child". However if another child is added to Bar with a different name, then
Foo can adopt that child as an adopted child.

.. seealso::
   :ref:`get_adopted_children <tree.get_adopted_children>` in
   :ref:`Tree <tree>` and :ref:`get_adopted_children <treenode.get_adopted_children>` in :ref:`TreeNode <treenode>`

.. code-block:: python

   bar.add_child("Unique", "This node has a unique title")

   foo.add_adopted_child("Unique")

   unique = foo.get_child("Unique")
   unique.string  # Will return "This node has a unique title"

   unique in foo.children  # Returns True
   unique in foo.get_biological_children  # Returns False
   unique in foo.get_adopted_children  # Returns True

   unique.parent  # Still Bar
   unique.adoptive_parents  # Returns a list including foo

Accessing Paths
---------------

To get a list of every node on a path use :ref:`get_lineage <tree.get_lineage>`. This will return the node at the path's
children and their children's children and so on. :ref:`remove_lineage <tree.remove_lineage>` can be used to
remove all of a node's biological children as opposed to :ref:`remove_node <tree.remove_node>` which will append the
nodes children to its parent. :ref:`get_lineage <treenode.get_lineage>` and :ref:`remove_lineage <treenode.remove_lineage>`
are also accessible from individual :ref:`TreeNodes <treenode>`

.. note::
   The passed in node is not included in the returned list and the list only includes biological children.

.. code-block:: python

   foo in tree.get_lineage("root") # Returns True
   tree.get_node("Unique") in tree.get_lineage("root") # Returns True

   tree.root in tree.get_lineage("root")  # Returns False
   tree.get_node("Bar.Child") in tree.get_lineage("Foo")  # Returns False