.. toctree::
   :maxdepth: 1

.. _Tree:

Tree
====

**Inherits:** object

**Module:** :ref:`string_tree <module_string_tree>`

.. note:: in this class "path" always refers to a string of the titles of each node joined by a period.
    Example: "Grandparent.Parent.Child" is a path to the "Child" TreeNode

Brief Description
-----------------

Represents a simple tree system for a non-linear parent-child string system such as a dialogue system.

Instance Methods
----------------

+---------------------------+------------------------------------------------------------------------------------------+
| :ref:`Tree <tree>`        | :ref:`TreeNode <tree.init>` ( )                                                          |
+---------------------------+------------------------------------------------------------------------------------------+
| :ref:`TreeNode <treenode>`| :ref:`add_node <tree.add_node>` ( str path, str title, str string )                      |
+---------------------------+------------------------------------------------------------------------------------------+
| :ref:`TreeNode <treenode>`| :ref:`get_node <tree.get_node>` ( str path )                                             |
+---------------------------+------------------------------------------------------------------------------------------+
| :ref:`TreeNode <treenode>`| :ref:`remove_node <tree.remove_node>` ( str path )                                       |
+---------------------------+------------------------------------------------------------------------------------------+
| str                       | :ref:`get_string <tree.get_string>` ( str path )                                         |
+---------------------------+------------------------------------------------------------------------------------------+
| list                      | :ref:`get_children <tree.get_children>` ( str path )                                     |
+---------------------------+------------------------------------------------------------------------------------------+
| list                      | :ref:`get_biological_children <tree.get_biological_children>` ( str path )               |
+---------------------------+------------------------------------------------------------------------------------------+
| None                      | :ref:`add_adopted_child <tree.add_adopted_child>` ( str path, str child )                |
+---------------------------+------------------------------------------------------------------------------------------+
| list                      | :ref:`get_adopted_children <tree.get_adopted_children>` ( str path )                     |
+---------------------------+------------------------------------------------------------------------------------------+
| :ref:`TreeNode <treenode>`| :ref:`remove_adopted_child <tree.remove_adopted_child>` ( str path )                     |
+---------------------------+------------------------------------------------------------------------------------------+
| list                      | :ref:`get_lineage <tree.get_lineage>` ( str path )                                       |
+---------------------------+------------------------------------------------------------------------------------------+
| list                      | :ref:`remove_lineage <tree.remove_lineage>` ( str path )                                 |
+---------------------------+------------------------------------------------------------------------------------------+

Description
-----------

A tree system that stores in a parent-child relationship by title. Strings are added to the root and to the roots
children and so on. Example: "root.foo.bar"

Instance Variables
------------------

.. _tree.tree:

- :ref:`list <tree>` **tree -** A list of TreeNodes that this tree contains.

.. _tree.root:

- :ref:`TreeNode <treenode>` **root -** The root node of this tree, with the :ref:`title <treenode.title>` "root".

Instance Method Descriptions
----------------------------

.. _tree.init:

- :ref:`Tree <tree>` **TreeNode ( )**

Creates a Tree instance

.. _tree.add_node:

- :ref:`TreeNode <treenode>` **add_node ( str path, str title, str string )**

Creates a node using the ``title`` and ``string``, and adds it to the parent node ``path`` then returns its instance.

.. _tree.get_node:

- :ref:`TreeNode <treenode>` **get_node ( str path )**

Returns the TreeNode at the ``path``

.. _tree.remove_node:

- :ref:`TreeNode <treenode>` **remove_node ( str path )**

Removes and returns the node at the ``path``. This will add the children of the node as children of the
nodes parent. Note that if one of the children of this node is the same as a child of the parents node it
will raise a ValueError

.. _tree.get_string:

- **str get_string ( str path )**

Returns the contents of the TreeNode at path.

.. _tree.get_children:

- :ref:`TreeNode <treenode>` **get_children ( str path )**

Returns the children of the TreeNode at ``path``.

.. _tree.get_biological_children:

- **list get_biological_children ( str path )**

Returns the node at ``path's`` children that are directly created from the node.

.. _tree.add_adopted_child:

- **None add_adopted_child ( str path, str child )**

Adds an adopted child to the node at path. ``Child`` is a path to a node that already exists as a child of
another node but is also the indirect child of this node

.. _tree.get_adopted_children:

- **list get_adopted_children ( str path )**

Returns the node at path's children that are not created from the node, but are added to this node
using :ref:`add_adopted_child ( ) <tree.add_adopted_child>` from the :ref:`Tree <tree>` or :ref:`TreeNode <treenode>`.

.. _tree.remove_adopted_child:

- :ref:`TreeNode <treenode>` **remove_adopted_child ( str path )**

Removes and returns the adopted child from the node at ``path``. ``Child`` is the path to the existing child.

.. _tree.get_lineage:

- **list get_lineage ( str path )**

Returns the lineage of the node at ``path``. This includes all biological children,
their biological children, and so on.

.. _tree.remove_lineage:

- **list remove_lineage ( str path )**

Removes and returns the lineage of the node at ``path``. This includes all biological children,
their biological children, and so on.

Supported Magic Methods
-----------------------

.. _tree.iter:

- :ref:`TreeNode <treenode>` **__iter__ ( ):**

Iterates through this Tree's :ref:`tree <tree.tree>` list

- **str __repr__ ( )**

Returns the representation of this Tree's :ref:`tree <tree.tree>` list

- **str __str__ ( )**

Returns this Tree's :ref:`tree <tree.tree>` list with each node on a new line and casting each node to a string
