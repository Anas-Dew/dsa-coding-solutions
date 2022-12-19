class BST:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def find_min(self):
        if self.left:
            self.left.find_min()
        else:
            return self.data
            
    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left.delete(val)

        elif val > self.data:
            if self.right:
                self.right.delete(val)

        else:
            if self.left is None or self.right is None:
                return None

            if self.left is None:
                return self.right

            if self.right is None:
                return self.left

            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)

        return self