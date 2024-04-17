class Ride:
    def __init__(self, rideNumber, rideCost, tripDuration): #initialization
        self.rideNumber = rideNumber
        self.rideCost = rideCost
        self.tripDuration = tripDuration

    def lesserThan(self, other_ride): #compares two ride costs, uses trip duration if costs are same.
        if self.rideCost < other_ride.rideCost:
            return True
        elif self.rideCost > other_ride.rideCost:
            return False
        elif self.rideCost == other_ride.rideCost:
            if self.tripDuration > other_ride.tripDuration:
                return False
            else:
                return True
