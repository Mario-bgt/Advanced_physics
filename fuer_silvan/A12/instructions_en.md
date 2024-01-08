In this task, you will implement a class `Inventory` for an item inventory in a game you're working on. An inventory has an associated player name and the available balance of the player.
To represent the inventory a list is used; this list contains the items. These are represented as tuples of the form (item_name, item_value, item_weight).
Since you can't possibly carry all the items that you find along your journey, your inventory also has a maximum capacity.

First, implement the `__init__` function. This function should take as inputs a string for the player name, an integer for the inventory balance, and an integer for the maximum capacity of the inventory.
The player name should be "DEFAULT" by default, and the balance and max_weight should be 0. Also initialize an empty list to store the items in.
Your variables must be private and be called `player_name`, `balance`, and `max_weight` in the `__init__` signature. If you choose different names, the autograder will not work.

To provide access to the items in your inventory, we made the inventory [iterable](https://docs.python.org/3.5/glossary.html#term-iterable), i.e., implemented the [\__iter__](https://docs.python.org/3.5/reference/datamodel.html#object.__iter__) method that returns an [iterator](https://docs.python.org/3.5/glossary.html#term-iterator) object with a meaningful implementation for [\__next__](https://docs.python.org/3.5/library/stdtypes.html#iterator.__next__).
The iterator iterates over the contents ordered by value (things that are most valuable are listed first). You don't need to change anything here, but have a look at the implementation and think about what changes would be needed to iterate over the items' weights, or iterate over items in ascending order of their value etc..

With this, you can use your inventory instance in your game like this:

     print("Items in the inventory:")
     for item in inv:
         print("{} with a value of {} and a weight of {}".format(item[0], item[1], item[2]))

Now you can implement a function `get_inv_weight()` that returns your inventory's total weight, and a function `get_inv_value()` that returns your inventory's value, that is the sum of the value of all of its items.

You must implement a [\__len__](https://docs.python.org/3.5/reference/datamodel.html#object.__len__) function, to make it easy to check how many items are in the inventory.

To enable collecting items you find, implement a `collect()` function that should be used as follows. Note that you should only be able to collect items if that doesn't result in your inventory exceeding its weight capacity.
If it's not possible to collect the item, a `Warning` should be raised:

    inv = Inventory("Great player name",  max_weight=300)
    inv.collect(("butter knife", 2, 1))
    inv.collect(("mighty sword", 500, 25))

Items can be `drop`ped from the inventory. Such an invocation should *remove and return* the matching item in the inventory. A `Warning` should be raised if no matching item can be found.

    inv.drop(("butter knife", 2, 1)) # ok
    inv.drop(("yellow spork", 10_000, 1)) # fails

You should also be able to `sell` items from the inventory (this function could be called by e.g. an instance of a Vendor class etc.).

Again, this should *remove and return* the matching item in the inventory or raise a `Warning` if there is no such item in the inventory.
Unlike `drop()`, the function `sell()` should result in a change of your inventory's balance by the item's value.

    inv.sell(("butter knife", 2, 1)) # increases the balance by 2 and removes the item from the inventory

Analogously, implement a `buy()` function that adds an item to the inventory and decreases its balance by the item's value, but only if the balance is big enough and the weight limit is not exceeded. If not, a `Warning` should be raised. 

Finally, implement the utility functions `get_balance()` and `get_player_name()` that allow the access to these private variables from outside the class.

All functions that take an item as input, should first check if the input has the right type, i.e. tuples of the form (string, int, int). Implement __proper_item for this.



**Note:** All states must be contained within the class. Do not store information in global variables or in class variables. It has to be possible to use multiple instances of the classes in parallel without suffering from side effects.

**Note:** The provided files define the signatures of various functions. Do not change these signatures or the automated grading will fail.

**Note:** We strongly encourage you to add more tests to the public test suite.


