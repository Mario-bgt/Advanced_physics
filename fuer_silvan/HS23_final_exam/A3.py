class BinaryTree:
    def __init__(self, key, value=0, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right

    def tally(self, needle):
        res = 0
        if self.left == None and self.right == None:
            return 0
        if needle == self.key:
            res += self.value
        else:
            res -= self.value
        return res + self.tally(self.right) + self.tally(self.left)



tree = BinaryTree("root",
                  left=BinaryTree("A",
                                  left=BinaryTree("B", 20,
                                                  left=BinaryTree("C", 60),
                                                  right=BinaryTree("D", -50)
                                                  ),
                                  right=BinaryTree("E",
                                                   right=BinaryTree("D", 70)
                                                   )
                                  ),
                  right=BinaryTree("D", 80)
                  )
print(tree.tally("C"))  # - 0 - 0 - 20 + 60 - -50 - 0 - 70 - 80
print(tree.tally("D"))  # - 0 - 0 - 20 - 60 + -50 - 0 + 70 + 80
