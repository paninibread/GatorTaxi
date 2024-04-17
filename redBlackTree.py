class RBTNode:
    def __init__(self, ride, min_heap_node):
        self.ride = ride
        self.parent = None  # parent node
        self.left = None  # left node
        self.right = None  # right node
        self.color = 1  # 1=red , 0 = black
        self.min_heap_node = min_heap_node


class RedBlackTree:
    def __init__(self):
        self.null_node = RBTNode(None, None)
        self.null_node.left = None
        self.null_node.right = None
        self.null_node.color = 0
        self.root = self.null_node

    # To retrieve the ride with the rideNumber equal to the key
    def getRide(self, key):
        temp = self.root

        # Iterating through the tree to find the node with rideNumber equal to the key
        while temp != self.null_node:
            if temp.ride.rideNumber == key:
                return temp
            if temp.ride.rideNumber < key:
                temp = temp.right
            else:
                temp = temp.left

        return None

    # Balancing the tree after deletion
    def balanceAfterDelete(self, node):
        
        while node != self.root and node.color == 0:
            if node == node.parent.right:
                parent_sibling = node.parent.left
                if parent_sibling.color != 0:
                    node.parent.color = 1
                    parent_sibling.color = 0
                    self.rRotate(node.parent)
                    parent_sibling = node.parent.left

                if parent_sibling.right.color == 0 and parent_sibling.left.color == 0:
                    parent_sibling.color = 1
                    node = node.parent
                else:
                    if parent_sibling.left.color != 1:
                        parent_sibling.right.color = 0
                        parent_sibling.color = 1
                        self.lRotate(parent_sibling)
                        parent_sibling = node.parent.left

                    parent_sibling.color = node.parent.color
                    node.parent.color = 0
                    parent_sibling.left.color = 0
                    self.rRotate(node.parent)
                    node = self.root
            else:
                parent_sibling = node.parent.right
                if parent_sibling.color != 0:
                    node.parent.color = 1
                    parent_sibling.color = 0
                    self.lRotate(node.parent)
                    parent_sibling = node.parent.right

                if parent_sibling.right.color == 0 and parent_sibling.left.color == 0:
                    parent_sibling.color = 1
                    node = node.parent
                else:
                    if parent_sibling.right.color != 1:
                        parent_sibling.left.color = 0
                        parent_sibling.color = 1
                        self.rRotate(parent_sibling)
                        parent_sibling = node.parent.right

                    parent_sibling.color = node.parent.color
                    node.parent.color = 0
                    parent_sibling.right.color = 0
                    self.lRotate(node.parent)
                    node = self.root

        node.color = 0

    # replaces one subtree as a child of its parent with another subtree
    def rbTransplant(self, node, child_node):
        if node.parent is None:
            self.root = child_node
        elif node == node.parent.right:
            node.parent.right = child_node
        else:
            node.parent.left = child_node
        child_node.parent = node.parent

    #cleanup when deleting a node
    def deleteNodeManager(self, node, key):
        delete_node = self.null_node
        while node != self.null_node:
            if node.ride.rideNumber == key:
                delete_node = node
            if node.ride.rideNumber >= key:
                node = node.left
            else:
                node = node.right

        if delete_node == self.null_node:
            return
        heap_node = delete_node.min_heap_node
        y = delete_node
        y_original_color = y.color
        if delete_node.left == self.null_node:
            x = delete_node.right
            self.rbTransplant(delete_node, delete_node.right)
        elif (delete_node.right == self.null_node):
            x = delete_node.left
            self.rbTransplant(delete_node, delete_node.left)
        else:
            y = self.minimum(delete_node.right)
            y_original_color = y.color
            x = y.right
            if y.parent == delete_node:
                x.parent = y
            else:
                self.rbTransplant(y, y.right)
                y.right = delete_node.right
                y.right.parent = y

            self.rbTransplant(delete_node, y)
            y.left = delete_node.left
            y.left.parent = y
            y.color = delete_node.color
        if y_original_color == 0:
            self.balanceAfterDelete(x)

        return heap_node

    # Balancing the tree after insert.
    def balanceAfterInsert(self, curr_node):
        while curr_node.parent.color == 1:
            if curr_node.parent == curr_node.parent.parent.left:
                parent_sibling = curr_node.parent.parent.right

                if parent_sibling.color == 0:
                    if curr_node == curr_node.parent.right:
                        curr_node = curr_node.parent
                        self.lRotate(curr_node)
                    curr_node.parent.color = 0
                    curr_node.parent.parent.color = 1
                    self.rRotate(curr_node.parent.parent)
                else:
                    parent_sibling.color = 0
                    curr_node.parent.color = 0
                    curr_node.parent.parent.color = 1
                    curr_node = curr_node.parent.parent

            else:
                parent_sibling = curr_node.parent.parent.left
                if parent_sibling.color == 0:
                    if curr_node == curr_node.parent.left:
                        curr_node = curr_node.parent
                        self.rRotate(curr_node)
                    curr_node.parent.color = 0
                    curr_node.parent.parent.color = 1
                    self.lRotate(curr_node.parent.parent)
                else:
                    parent_sibling.color = 0
                    curr_node.parent.color = 0
                    curr_node.parent.parent.color = 1
                    curr_node = curr_node.parent.parent

            if curr_node == self.root:
                break
        self.root.color = 0

    def searchRidesInRange(self, node, low, high, res):
        if node == self.null_node:
            return

        if low < node.ride.rideNumber:
            self.searchRidesInRange(node.left, low, high, res)
        if low <= node.ride.rideNumber <= high:
            res.append(node.ride)
        self.searchRidesInRange(node.right, low, high, res)

    def getRidesInRange(self, low, high):
        res = []
        self.searchRidesInRange(self.root, low, high, res)
        return res

    def minimum(self, node):
        while node.left != self.null_node:
            node = node.left
        return node

    def lRotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.null_node:
            y.left.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def rRotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.null_node:
            y.right.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def insert(self, ride, min_heap):
        node = RBTNode(ride, min_heap)
        node.parent = None
        node.left = self.null_node
        node.right = self.null_node
        node.color = 1

        insertion_node = None
        temp_node = self.root

        while temp_node != self.null_node:
            insertion_node = temp_node
            if node.ride.rideNumber < temp_node.ride.rideNumber:
                temp_node = temp_node.left
            else:
                temp_node = temp_node.right

        node.parent = insertion_node
        if insertion_node is None:
            self.root = node
        elif node.ride.rideNumber > insertion_node.ride.rideNumber:
            insertion_node.right = node
        else:
            insertion_node.left = node

        if node.parent is None:
            node.color = 0
            return

        if node.parent.parent is None:
            return

        self.balanceAfterInsert(node)

    def deleteNode(self, rideNumber):
        return self.deleteNodeManager(self.root, rideNumber)
