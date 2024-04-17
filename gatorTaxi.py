import sys

from rideModel import Ride
from minHeap import MinHeap
from minHeap import MinHeapNode
from redBlackTree import RedBlackTree, RBTNode

#handles Insert but with more parameters, inserts ride into heap and red black tree.
def insertRide(ride, heap, rbt):
    if rbt.getRide(ride.rideNumber) is not None:
        outputManager(None, "Duplicate rideNumber, Exiting application.", False)
        sys.exit(0)
    rbt_node = RBTNode(None, None)
    min_heap_node = MinHeapNode(ride, rbt_node, heap.currentSize + 1)
    heap.insert(min_heap_node)
    rbt.insert(ride, min_heap_node)

#control how output file is printed for each action.
def outputManager(ride, message, list):
    file = open("output.txt", "a")
    if ride is None:
        file.write(message + "\n")
    else:
        message = ""
        if not list:
            message += ("(" + str(ride.rideNumber) + "," + str(ride.rideCost) + "," + str(ride.tripDuration) + ")\n")
        else:
            if len(ride) == 0:
                message += "(0,0,0)\n"
            for i in range(len(ride)):
                if i != len(ride) - 1:
                    message = message + ("(" + str(ride[i].rideNumber) + "," + str(ride[i].rideCost) + "," + str(
                        ride[i].tripDuration) + "),")
                else:
                    message = message + ("(" + str(ride[i].rideNumber) + "," + str(ride[i].rideCost) + "," + str(
                        ride[i].tripDuration) + ")\n")

        file.write(message)
    file.close()

#handles Print(rideNumber) with one parameter.
def printRide(rideNumber, rbt):
    res = rbt.getRide(rideNumber)
    if res is None:
        outputManager(Ride(0, 0, 0), "", False)
    else:
        outputManager(res.ride, "", False)

#handles Print(rideNumber1,rideNumber2) but with two parameters.
def printRide2(l, h, rbt):
    list = rbt.getRidesInRange(l, h)
    outputManager(list, "", True)

#handles GetNextRide(), pops ride with the lowest cost from the heap and red black tree.
def getNextRide(heap, rbt):
    if heap.currentSize != 0:
        popped_node = heap.pop()
        rbt.deleteNode(popped_node.ride.rideNumber)
        outputManager(popped_node.ride, "", False)
    else:
        outputManager(None, "No active ride requests", False)

#handles CancelRide(rideNumber), nukes the node from the heap and red black tree.
def cancelRide(ride_number, heap, rbt):
    heap_node = rbt.deleteNode(ride_number)
    if heap_node is not None:
        heap.deleteElement(heap_node.min_heap_index)

#handles UpdateTrip(rideNumber, new_tripDuration) for the heap and red black tree
def updateTrip(rideNumber, new_duration, heap, rbt):
    rbt_node = rbt.getRide(rideNumber)
    if rbt_node is None:
        print("")
    elif new_duration <= rbt_node.ride.tripDuration:
        heap.updateElement(rbt_node.min_heap_node.min_heap_index, new_duration)
    elif rbt_node.ride.tripDuration < new_duration <= (2 * rbt_node.ride.tripDuration):
        cancelRide(rbt_node.ride.rideNumber, heap, rbt)
        insertRide(Ride(rbt_node.ride.rideNumber, rbt_node.ride.rideCost + 10, new_duration), heap, rbt)
    else:
        cancelRide(rbt_node.ride.rideNumber, heap, rbt)

#reads the input file line by line and calls the functions as needed. 
if __name__ == "__main__":
    heap = MinHeap()
    rbt = RedBlackTree()
    file = open("output.txt", "w")
    file.close()
    file = open(sys.argv[1], "r")
    for s in file.readlines():
        n = []
        for num in s[s.index("(") + 1:s.index(")")].split(","):
            if num != '':
                n.append(int(num))
        if "Insert" in s:
            insertRide(Ride(n[0], n[1], n[2]), heap, rbt)
        elif "Print" in s:
            if len(n) == 1:
                printRide(n[0], rbt)
            elif len(n) == 2:
                printRide2(n[0], n[1], rbt)
        elif "UpdateTrip" in s:
            updateTrip(n[0], n[1], heap, rbt)
        elif "GetNextRide" in s:
            getNextRide(heap, rbt)
        elif "CancelRide" in s:
            cancelRide(n[0], heap, rbt)