class MinHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0
    #insert into heap
    def insert(self, element):
        self.heapList.append(element)
        self.currentSize += 1
        self.heapifyUp(self.currentSize)
    #split array into two then add elements into a segement then sort by moving the heap up as needed.
    def heapifyUp(self, p):
        while (p // 2) > 0:
            if self.heapList[p].ride.lesserThan(self.heapList[p // 2].ride):
                self.swap(p, (p // 2))
            else:
                break
            p = p // 2
    #swap heap elements
    def swap(self, ind1, ind2):
        temp = self.heapList[ind1]
        self.heapList[ind1] = self.heapList[ind2]
        self.heapList[ind2] = temp
        self.heapList[ind1].min_heap_index = ind1
        self.heapList[ind2].min_heap_index = ind2

    #split array into two then add elements into a segement then sort by moving the heap down as needed.
    def heapifyDown(self, p):
        while (p * 2) <= self.currentSize:
            ind = self.getMinChildIndex(p)
            if not self.heapList[p].ride.lesserThan(self.heapList[ind].ride):
                self.swap(p, ind)
            p = ind

    def getMinChildIndex(self, p):
        if (p * 2) + 1 > self.currentSize:
            return p * 2
        else:
            if self.heapList[p * 2].ride.lesserThan(self.heapList[(p * 2) + 1].ride):
                return p * 2
            else:
                return (p * 2) + 1

    def updateElement(self, p, new_key):
        node = self.heapList[p]
        node.ride.tripDuration = new_key
        if p == 1:
            self.heapifyDown(p)
        elif self.heapList[p // 2].ride.lesserThan(self.heapList[p].ride):
            self.heapifyDown(p)
        else:
            self.heapifyUp(p)

    def deleteElement(self, p):

        self.swap(p, self.currentSize)
        self.currentSize -= 1
        *self.heapList, _ = self.heapList

        self.heapifyDown(p)

    def pop(self):

        if len(self.heapList) == 1:
            return 'No Rides Available'

        root = self.heapList[1]

        self.swap(1, self.currentSize)
        self.currentSize -= 1
        *self.heapList, _ = self.heapList

        self.heapifyDown(1)

        return root

#initializes a node in the heap.
class MinHeapNode:
    def __init__(self, ride, rbt, min_heap_index):
        self.ride = ride
        self.rbTree = rbt
        self.min_heap_index = min_heap_index
