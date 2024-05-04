# Mode Fair Software Developer (AI) Technical Assessment
This repository is a Technical Assessment for Mode Fair Software Developer (AI)

## Overview
1. assessment.py
    - Technical assesment contents were completed here
2. images
    - images of code snipets

## Approach

1. Class Implementation 
    - Customer
        - Represents a customer with attributes such as customer ID, latitude, longitude, and demand.
    
    <p align="center">
    <img src="images/customer.png" alt="outlier" width="max-width: 100%;">
    </p>    

    - Vehicle 
        - Represents a vehicle with attributes like vehicle type, capacity, and cost per kilometer.

    <p align="center">
    <img src="images/vehicle.png" alt="outlier" width="max-width: 100%;">
    </p>

    - Solution
        - Represents a solution consisting of three routes (route1, route2, route3).
        - Calculates distances, costs, and loads for each route.
        - Evaluates the solution based on predefined scores for distance, capacity, and cost.

    <p align="center">
    <img src="images/solution.png" alt="outlier" width="max-width: 100%;">
    </p>

2. Genetic Algorithm Components
    - Initialization
        - Generates an initial population of solutions with random chromosome values.
        - Each chromosome represents a combination of vehicle types and customer orders.

    <p align="center">
    <img src="images/Initialization.png" alt="outlier" width="max-width: 100%;">
    </p>

    - Fitness Calculation
        - Calculates the fitness of each solution based on distance, capacity, and cost.
        - Evaluates each solution using a fitness function that combines these factors.

    <p align="center">
    <img src="images/Fitness.png" alt="outlier" width="max-width: 100%;">
    </p>

    - Selection
        - Selects individuals from the population based on their fitness scores.
        - Higher fitness individuals have a higher chance of being selected.

    <p align="center">
    <img src="images/Selection.png" alt="outlier" width="max-width: 100%;">
    </p>

    - Crossover and Mutation
        - Applies order crossover to selected individuals to create new offspring.
        - Incorporates mutation to introduce genetic diversity and explore new solutions.

    <p align="center">
    <img src="images/Selection.png" alt="outlier" width="max-width: 100%;">
    </p>

    <p align="center">
    <img src="images/Mutation.png" alt="outlier" width="max-width: 100%;">
    </p>


    - Rule Checking
        - Ensures that chromosomes adhere to defined rules such as no duplicate customers and valid vehicle types.

    <p align="center">
    <img src="images/Mutation.png" alt="outlier" width="max-width: 100%;">
    </p>

    - Example Output

    <p align="center">
    <img src="images/Output.png" alt="outlier" width="max-width: 100%;">
    </p>
