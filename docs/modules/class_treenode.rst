.. toctree::
   :maxdepth: 1

.. _treenode:

TreeNode
========

**Inherits:** object

**Module:** :ref:`string_tree <module_string_tree>`

.. _treenode.note:

.. note:: in this class "path" always refers to a string of the titles of each node joined by a period.
    Example: "Grandparent.Parent.Child" is a path to the "Child" TreeNode

Brief Description
-----------------

A node in the :ref:`Tree <tree>` that holds references to this nodes :ref:`parent <treenode.parent>`, biological and
adopted :ref:`children <treenode.children>` and this nodes :ref:`string <treenode.string>` contents.

Instance Methods
----------------

+------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| :ref:`TreeNode <treenode>`         | :ref:`TreeNode <treenode.init>` ( :ref:`Tree <tree>` tree, :ref:`TreeNode <treenode>` parent, str title, str string )  |
+------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| str                                | :ref:`get_path <treenode.get_path>` ( )                                                                                |
+------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| :ref:`TreeNode <treenode>`         | :ref:`add_child <treenode.add_child>` ( str title, str string )                                                        |
+------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| :ref:`TreeNode <treenode>`         | :ref:`get_child <treenode.get_child>` ( str title )                                                                    |
+------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| :ref:`TreeNode <treenode>`         | :ref:`remove_child <treenode.remove_child>` ( str title )                                                              |
+------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| list                               | :ref:`get_biological_children <treenode.get_biological_children>` ( )                                                  |
+------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| None                               | :ref:`add_adopted_child <treenode.add_adopted_child>` ( str path )                                                     |
+------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| list                               | :ref:`get_adopted_children <treenode.get_adopted_children>` ( )                                                        |
+------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| None                               | :ref:`remove_adopted_child <treenode.remove_adopted_child>` ( str title )                                              |
+------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| list                               | :ref:`get_lineage <treenode.get_lineage>` ( )                                                                          |
+------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| list                               | :ref:`remove_lineage <treenode.remove_lineage>` ( )                                                                    |
+------------------------------------+------------------------------------------------------------------------------------------------------------------------+

Description
-----------

A node in the :ref:`Tree <tree>` that holds references to this nodes :ref:`parent <treenode.parent>`, biological and
adopted :ref:`children <treenode.children>` and this nodes :ref:`string <treenode.string>` contents.

Instance Variables
------------------

.. _treenode.tree:

- :ref:`Tree <tree>` **tree -** The tree that the node belongs to.

.. _treenode.parent:

- :ref:`TreeNode <treenode>` **parent -** The direct TreeNode this node derives from.

.. _treenode.adoptive_parents:

- **list adoptive_parents -** A list of this nodes adoptive parent TreeNodes, these are nodes that are not the direct parent of this node but still are connected as a parent.

.. _treenode.children:

- **list children -** A list of this nodes child TreeNodes.

.. _treenode.title:

- **str title -** The title that describes this node. This is used in the path to access the node. See :ref:`note <treenode.note>`

.. _treenode.string:

- **str string -** The contents of this node.

Instance Method Descriptions
----------------------------

.. _treenode.init:

- :ref:`TreeNode <treenode>` TreeNode ( :ref:`Tree <tree>` tree, :ref:`TreeNode <tree>` parent, str title, str string )

Creates a TreeNode instance on the ``tree`` as a child of the ``parent`` with the ``title`` and ``string`` contents.

.. _treenode.get_path:

- **str get_path ( )**

Returns the path to this node.

.. _treenode.add_child:

- :ref:`TreeNode <treenode>` **add_child ( str title, str string )**

Creates a TreeNode with the ``title`` and ``string`` and adds it as a
child to this node and appends it to this nodes :ref:`tree <treenode.tree>` .

.. _treenode.get_child:

- :ref:`TreeNode <treenode>` **get_child ( str title )**

Returns the child of this node with the ``title`` .

.. _treenode.remove_child:

- :ref:`TreeNode <treenode>` **remove_child ( str title )**

Removes and returns the child of this node with the ``title`` . This will append all of the children of the
removed node as children of this node.

.. _treenode.get_biological_children:

- **list get_biological_children ( )**

Returns a list of this nodes :ref:`children <treenode.children>` that are directly created from this node.

.. _treenode.add_adopted_child:

- **None add_adopted_child ( str path )**

Adds the TreeNode from the ``path`` as an adopted child of this node. Adopted children are the same as biological children
except they are not directly made from this parent.

.. _treenode.get_adopted_children:

- **list get_adopted_children ( )**

Returns a list of this nodes :ref:`children <treenode.children>` that are adopted. Meaning they are not
directly created from this node.

.. _treenode.remove_adopted_child:

- None **remove_adopted_child ( str title )**

Removes the child of this node with the ``title`` from this nodes :ref:`children <treenode.children>`.

.. _treenode.get_lineage:

- **list get_lineage ( )**

Returns the lineage of this node. This includes all biological children, their biological children, and so on.

.. _treenode.remove_lineage:

- **list remove_lineage ( )**

Removes and returns the lineage of this node. This includes all biological children, their biological children, and so on.

Supported Magic Methods
-----------------------

.. _treenode.eq:

- **bool __eq__ ( )**

Returns true if this node and the other node have the same :ref:`title <treenode.title>`, :ref:`parent <treenode.parent>`,
and :ref:`children <treenode.children>`


