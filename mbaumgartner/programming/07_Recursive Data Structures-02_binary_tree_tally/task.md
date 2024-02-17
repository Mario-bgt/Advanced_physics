Implement a class `BinaryTree`, which represents a tree-like, recursive data structure.

A `BinaryTree` is initialized with one positional argument `key`, which can be of arbitrary type, a keyword argument `value`, which is a number (`0` by default), and two more keyword arguments `left` and `right`, each of which is another `BinaryTree` (or `None` by default).

`BinaryTree` should have a method `tally` which takes an argument `needle` of arbitrary type. `tally` should recursively traverse the `BinaryTree` data structure and eventually return a kind-of-sum of all `value`s in the tree, *adding* those `value`s where `needle` matches `key`, and *subtracting* all others. Besides comparing `needle` to the tree's `key`, `tally` will also need to call the `left` and `right` `BinaryTree`'s `tally` methods recursively to add their return values to the result.

In the example below, a tree consisting of eight `BinaryTree` instances is constructed. `tree.tally("C")` and `tree.tally("D")` are called on the root (outermost) `BinaryTree` and return the kind-of-sum according to the rule outlined above.

To receive partial points, make sure that `BinaryTree` can at least be instantiated correctly as per the example. Use *public* attribute names that equal the specified constructor argument names.
