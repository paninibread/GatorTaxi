# GatorTaxi
GatorTaxi is an up-and-coming ride-sharing service. They get many ride requests every day and are planning to develop new software to keep track of their pending ride requests.

## Description

**Project Title: GatorTaxi Ride Management System**

**Introduction:**
GatorTaxi is a ride-hailing service that needs an efficient system to manage ride requests, prioritize them based on cost and duration, and handle various operations such as adding, updating, canceling rides, and selecting the next ride. This project aims to develop a comprehensive Ride Management System for GatorTaxi using a combination of data structures like Min Heap and Red-Black Tree (RBT).

**Features:**

1. **Ride Identification:**
   - Each ride is uniquely identified by a triplet consisting of:
     - `rideNumber`: A unique integer identifier for each ride.
     - `rideCost`: The estimated cost (in integer dollars) for the ride.
     - `tripDuration`: The total time (in integer minutes) needed to get from pickup to destination.

2. **Operations:**
   - **Print(rideNumber):** Prints the triplet (rideNumber, rideCost, tripDuration).
   - **Print(rideNumber1, rideNumber2):** Prints all triplets (rx, rideCost, tripDuration) for which rideNumber1 ≤ rx ≤ rideNumber2.
   - **Insert(rideNumber, rideCost, tripDuration):** Inserts a new ride triplet, ensuring rideNumber is unique.
   - **GetNextRide():** Outputs the ride with the lowest rideCost, breaking ties by selecting the ride with the lowest tripDuration. Deletes the selected ride from the data structure.
   - **CancelRide(rideNumber):** Deletes the ride triplet (rideNumber, rideCost, tripDuration) from the data structure if it exists.
   - **UpdateTrip(rideNumber, new_tripDuration):**
     - Updates the tripDuration of the ride identified by rideNumber.
     - Handles different scenarios based on the new tripDuration:
       - No action if new_tripDuration ≤ existing tripDuration.
       - Cancels the existing ride and creates a new ride request with a penalty of 10 on rideCost if existing_tripDuration < new_tripDuration ≤ 2*(existing tripDuration).
       - Automatically declines the ride if new_tripDuration > 2*(existing tripDuration).

3. **Data Structures:**
   - **Min Heap:** Stores ride triplets ordered by rideCost. In case of ties, prioritizes the ride with the shortest tripDuration.
   - **Red-Black Tree (RBT):** Stores ride triplets ordered by rideNumber.

4. **Integration:**
   - The system maintains pointers between corresponding nodes in the Min Heap and RBT for efficient retrieval and updates.

The GatorTaxi Ride Management System offers a robust solution for handling ride requests efficiently, ensuring optimal selection based on cost and duration, and supporting essential operations like adding, updating, and canceling rides. By utilizing a combination of Min Heap and Red-Black Tree data structures, the system provides a scalable and organized approach to manage ride data, contributing to a seamless experience for both riders and drivers.

## Authors

Prashast Sharma - [LinkedIn](https://www.linkedin.com/in/prashast-sharma-690778230/)
