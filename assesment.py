import math
import random

class Customer:
    def __init__(self, customer_id, latitude, longitude, demand):
        self.customer_id = customer_id
        self.latitude = latitude
        self.longitude = longitude
        self.demand = demand

    def get_load(self):
        return self.demand

    def __str__(self):
        return f"Customer {self.customer_id}: Latitude {self.latitude}, Longitude {self.longitude}, Demand {self.demand}"


class Vehicle:
    def __init__(self, vehicle_type, capacity, cost_per_km):
        self.vehicle_type = vehicle_type
        self.capacity = capacity
        self.cost_per_km = cost_per_km

    def __str__(self):
        return f"{self.vehicle_type}: Capacity {self.capacity}, Cost RM{self.cost_per_km} per km"

customers_data = [
    (0, 4.4184, 114.0932, 0 ),
    (1, 4.3555, 113.9777, 5),
    (2, 4.3976, 114.0049, 8),
    (3, 4.3163, 114.0764, 3),
    (4, 4.3184, 113.9932, 6),
    (5, 4.4024, 113.9896, 5),
    (6, 4.4142, 114.0127, 8),
    (7, 4.4804, 114.0734, 3),
    (8, 4.3818, 114.2034, 6),
    (9, 4.4935, 114.1828, 5),
    (10, 4.4932, 114.1322, 8),
]

vehicles_data = [
    ("Type A", 25, 1.2),
    ("Type B", 30, 1.5),
]

#create instances of customers and vehicles
customers_data = [Customer(*data) for data in customers_data]
vehicles = [Vehicle(*data) for data in vehicles_data]

#-------------------

class Solution:
    def __init__(self, route1, route2, route3):
        self.route1 = route1
        self.route2 = route2
        self.route3 = route3

        self.route1_cost = 0
        self.route2_cost = 0
        self.route3_cost = 0

        self.route1_distance = []
        self.route2_distance = []
        self.route3_distance = []

        self.route1_demand = 0
        self.route2_demand = 0
        self.route3_demand = 0

    def calculate_distance(self, customer1, customer2):
            delta_lon = customer2.longitude - customer1.longitude
            delta_lat = customer2.latitude - customer1.latitude
            distance_km = 100 * math.sqrt(delta_lat**2 + delta_lon**2)
            return distance_km

    def cal_route1_distance(self):
        self.route1_distance.append(self.calculate_distance(customers_data[0], self.route1[1])) #depot to 1st customer
        for first, second in zip(self.route1[1:], self.route1[2:]):
            self.route1_distance.append(self.calculate_distance(first, second))
        self.route1_distance.append(self.calculate_distance(customers_data[0], self.route1[-1])) #back to depot

    def cal_route2_distance(self):
        self.route2_distance.append(self.calculate_distance(customers_data[0], self.route2[1]))
        for first, second in zip(self.route2[1:], self.route2[2:]):
            self.route2_distance.append(self.calculate_distance(first, second))
        self.route2_distance.append(self.calculate_distance(customers_data[0], self.route2[-1])) 

    def cal_route3_distance(self):
        self.route3_distance.append(self.calculate_distance(customers_data[0], self.route3[1]))
        for first, second in zip(self.route3[1:], self.route3[2:]):
            self.route3_distance.append(self.calculate_distance(first, second))
        self.route3_distance.append(self.calculate_distance(customers_data[0], self.route3[-1])) 

    def cal_route1_cost(self):
        for i in self.route1_distance:
            self.route1_cost += self.route1[0].cost_per_km * i

    def cal_route2_cost(self):
        for i in self.route2_distance:
            self.route2_cost += self.route2[0].cost_per_km * i

    def cal_route3_cost(self):
        for i in self.route3_distance:
            self.route3_cost += self.route3[0].cost_per_km * i 

    def cal_route1_load(self):
        total_demand = 0 
        for i in self.route1[1:]:
            total_demand += i.get_load()
        self.route1_demand = total_demand

    def cal_route2_load(self):
        total_demand = 0 
        for i in self.route2[1:]:
            total_demand += i.get_load()
        self.route2_demand = total_demand

    def cal_route3_load(self):
        total_demand = 0 
        for i in self.route3[1:]:
            total_demand += i.get_load()
        self.route3_demand = total_demand

    def check_overweight(self, capacity, demand):
        if capacity >= demand:
            return 10 / (capacity / demand)
        else:
            False

    def begin_cal(self):
        self.cal_route1_distance()
        self.cal_route2_distance()
        self.cal_route3_distance()
        self.cal_route1_cost()
        self.cal_route2_cost()
        self.cal_route3_cost()
        self.cal_route1_load()
        self.cal_route2_load()
        self.cal_route3_load()

    def evaluate_solution(self, starting_score, over_capacity_score, capacity_score, cost_multiple): #default (starting_score, over_capacity_score, capacity_score, cost_multiple)
        total_cost = 0
        total_cost += self.route1_cost
        total_cost += self.route2_cost
        total_cost += self.route3_cost

        route_capacity = 0

        route1_cap = self.check_overweight(self.route1_demand, self.route1[0].capacity)
        route2_cap = self.check_overweight(self.route2_demand, self.route2[0].capacity)
        route3_cap = self.check_overweight(self.route3_demand, self.route3[0].capacity)

        #gives a negative score if overweight
        if not route1_cap:
            route_capacity += -over_capacity_score
        else:
            #rewards if its near the capacity weight
            route_capacity += route1_cap * capacity_score
        
        if not route2_cap:
            route_capacity += -over_capacity_score
        else:
            route_capacity += route2_cap * capacity_score

        if not route3_cap:
            route_capacity += -over_capacity_score
        else:
            route_capacity += route3_cap * capacity_score

        #returns starting score + weight limit + total cost (lower better)
        return starting_score + route_capacity - (total_cost * cost_multiple)

    def __str__(self):
        self.begin_cal()
        print("Total Distance = ", int(round(sum(self.route2_distance+ self.route2_distance +self.route2_distance), 0 )) ,'km')
        print("Total Cost = RM", round(self.route1_cost+ self.route2_cost+ self.route3_cost, 2))

        print('Vechicle 1 '+'('+ self.route1[0].vehicle_type +"):")
        print(f'Round Trip Distance: {round(sum(self.route1_distance), 3 )} km, Cost: RM {round(self.route1_cost, 2)}, Demand: {self.route1_demand}')
        print(f'Depot -> C{self.route1[1].customer_id}({round(self.route1_distance[0], 3 )}) -> C{self.route1[2].customer_id}({round(self.route1_distance[1], 3 )}) -> C{self.route1[3].customer_id}({round(self.route1_distance[2], 3 )}) -> C{self.route1[4].customer_id}({round(self.route1_distance[3], 3 )})')

        print('Vechicle 2 '+'('+ self.route2[0].vehicle_type +"):")
        print(f'Round Trip Distance: {round(sum(self.route2_distance), 3 )} km, Cost: RM {round(self.route2_cost, 2)}, Demand: {self.route2_demand}')
        print(f'Depot -> C{self.route2[1].customer_id}({round(self.route2_distance[0], 3 )}) -> C{self.route2[2].customer_id}({round(self.route2_distance[1], 3 )}) -> C{self.route2[3].customer_id}({round(self.route2_distance[2], 3 )}) -> C{self.route2[4].customer_id}({round(self.route2_distance[3], 3 )})')


        print('Vechicle 3 '+'('+ self.route3[0].vehicle_type +"):")
        print(f'Round Trip Distance: {round(sum(self.route3_distance), 3 )} km, Cost: RM {round(self.route3_cost, 2)}, Demand: {self.route3_demand}')
        print(f'Depot -> C{self.route3[1].customer_id}({round(self.route3_distance[0], 3 )}) -> C{self.route3[2].customer_id}({round(self.route3_distance[1], 3 )})')


        return ""

#-------------------

# Generate initial population
def generate_initial_population(population_size):
    population = []
    for _ in range(population_size):
        chromosome = []
        all_numbers = list(range(1, 11)) 
        random.shuffle(all_numbers)  
        for i in range(3):  
            first_value = random.randint(0, 1)  #random 0 or 1 for selecting car type
            templist = []
            templist.insert(0, first_value)  
            for x in range(4):
                if x > 3:
                    break
                try:
                    templist.append(all_numbers.pop(0)) #ensures no duplicates 
                except:
                    pass

            chromosome.append(templist) 
        population.append(chromosome) 
        
    return population

def calculate_distance(customer1, customer2):
    delta_lon = customer2[1] - customer1[1]
    delta_lat = customer2[2] - customer1[2]
    distance_km = 100 * math.sqrt(delta_lat**2 + delta_lon**2)
    return distance_km

def calculate_route_distance(route):
    total_distance = 0
    for i in range(len(route) - 1):
        total_distance += calculate_distance(route[i], route[i + 1])
    return total_distance

def calculate_route_cost(route, vehicle):
    distance = calculate_route_distance(route)
    cost = vehicle[2] * distance
    return cost

def calculate_fitness(chromosome, customers, vehicles, score):
    solution_data = ([],[],[])
    for x in range(0, len(chromosome)):
        for count, i in enumerate(chromosome[x]):
            if count == 0:
                solution_data[x].append(vehicles[i])
            else:
                solution_data[x].append(customers[i])
    
        solution = Solution(*solution_data)

    
    solution.begin_cal()
    starting_score, over_capacity_score, capacity_score, cost_multiple = score
    return solution.evaluate_solution( starting_score, over_capacity_score, capacity_score, cost_multiple) #default (starting_score, over_capacity_score, capacity_score, cost_multiple)

def selection(population, fitness_scores):
    total_fitness = sum(fitness_scores)
    cumulative_probabilities = [sum(fitness_scores[:i+1]) / total_fitness for i in range(len(fitness_scores))]
    
    selected_population = []
    for _ in range(len(population)):
        random_value = random.random()
        for i, prob in enumerate(cumulative_probabilities):
            if random_value <= prob:
                selected_population.append(population[i])
                break
    
    return selected_population

def order_crossover(parent1, parent2):
    ori_parent1 = parent1
    ori_parent2 = parent2
    parent1 = [item for sublist in parent1 for item in sublist[1:]] #convert back to list to apply partial mapped crossover
    parent2 = [item for sublist in parent2 for item in sublist[1:]]

    size = len(parent1)
    child1, child2 = [-1] * size, [-1] * size

    #select a random range for crossover
    cx_point1 = random.randint(0, size - 2)
    cx_point2 = random.randint(cx_point1 + 1, size - 1)

    # Copy the crossover segment from parents to children
    child1[cx_point1:cx_point2 + 1] = parent1[cx_point1:cx_point2 + 1]
    child2[cx_point1:cx_point2 + 1] = parent2[cx_point1:cx_point2 + 1]

    #fill in the rest of the children using order from parents
    fill_in(child1, parent2, cx_point2 + 1)
    fill_in(child1, parent2, 0, cx_point1)
    fill_in(child2, parent1, cx_point2 + 1)
    fill_in(child2, parent1, 0, cx_point1)

    child1 = fix_array(child1)
    child2 = fix_array(child2)

    final_child1 = ([],[],[])
    first_value = [sublist[0] for sublist in ori_parent1]
    for count, i in enumerate(child1):
        x = min(count //4, 2) 
        if count == 0 or count == 4 or count == 8:
            final_child1[x].append(first_value[x])
        final_child1[x].append(i)

    final_child2 = ([],[],[])
    first_value = [sublist[0] for sublist in ori_parent2]
    for count, i in enumerate(child2):
        x = min(count //4, 2) 
        if count == 0 or count == 4 or count == 8:
            final_child2[x].append(first_value[x])
        final_child2[x].append(i)

    return final_child1, final_child2

def fix_array(arr):
    while True:
        #check for duplicates
        duplicates = set([x for x in arr if arr.count(x) > 1])
        
        #find the missing number
        missing_number = set(range(1, 11)) - set(arr)
        
        if len(duplicates) == 0 and len(missing_number) == 0:
            break
        
        #replace duplicates with the missing number
        for i in range(len(arr)):
            if arr[i] in duplicates:
                arr[i] = missing_number.pop() if len(missing_number) > 0 else arr[i]
    
    return arr

def fill_in(child, parent, start, end=None):
    if end is None:
        end = len(parent)
    index = end
    for value in parent:
        if value not in child[start:end]:
            child[index % len(child)] = value
            index += 1

def mutation(chromosome, mutation_rate):
    #pass mutation rate
    if random.uniform(0, 1) > mutation_rate:
        return chromosome
    #random select index to swap
    first_index = random.randint(0, len(chromosome) - 1)
    second_index = random.randint(0, len(chromosome[first_index]) - 1)

    #check if index selected is vehicle 
    if second_index == 0:
        chromosome[first_index][second_index] = chromosome[first_index][second_index] ^ 1
        
    else:
        #check if new mutation matches to original
        mutated_val = random.randint(1, 10)
        original_val = chromosome[first_index][second_index]

        if mutated_val == chromosome[first_index][second_index]:
            return chromosome
        for count1, sub_arr in enumerate(chromosome):
            for count2, val in enumerate(sub_arr[1:]):
                if val == mutated_val:
                    chromosome[count1][count2] = original_val
        chromosome[first_index][second_index] = mutated_val

    return chromosome

def check_rules(chromosome):
    routes = [item for sublist in chromosome for item in sublist[1:]]
    vehicles = [sublist[0] for sublist in chromosome]

    # Check if vehicles contain values other than 0 or 1
    for car_value in vehicles:
        if car_value != 0:
            if car_value != 1:
                return True

    # Check if routes contain duplicate values
    if len(routes) != len(set(routes)):
        return True

    # Check if routes contain numbers from 1 to 10
    if set(routes) != set(range(1, 11)):
        return True

    return False


#begin genetic algorthim
num_generations  = 100
population = generate_initial_population(num_generations)

#starting_score, over_capacity_score, capacity_score, cost_multiple
score = (1000, 600, 150, 1050)

for count in range(num_generations):
    fitness_scores = []
    for chromosome in population:
        
        try:
            fitness_scores.append(calculate_fitness(chromosome, customers_data, vehicles, score))
        except:
            population.remove(chromosome)
            new_chromosome = generate_initial_population(1)[0]
            population.append(new_chromosome)
            fitness_scores.append(calculate_fitness(new_chromosome, customers_data, vehicles, score))

        selected_population = selection(population, fitness_scores)

        #Crossover and Mutation
        mutation_rate = 0.15
        new_population = []
        for i in range(0, len(selected_population), 2):  #pairing parents for crossover
            parent1 = selected_population[i]
            parent2 = selected_population[i + 1]

            child1, child2 = order_crossover(parent1, parent2)

            child1 = mutation(child1, mutation_rate)
            child2 = mutation(child2, mutation_rate)

            if not check_rules(child1) or not check_rules(child2):
                new_population.extend([child1, child2])

    #update population
    population = new_population

    num_of_missing_population = num_generations- len(population)
    
    for _ in range(0, num_of_missing_population):
        population.append(generate_initial_population(1)[0])

    fitness_scores = []
    for chromosome in population:
        try:
            fitness_scores.append(calculate_fitness(chromosome, customers_data, vehicles, score))
        except:
            population.remove(chromosome)
            population.append(generate_initial_population(1)[0])
            fitness_scores.append(calculate_fitness(population[-1], customers_data, vehicles, score))

    #remove weakness
    weakest_index = fitness_scores.index(min(fitness_scores))
    del population[weakest_index]
    del fitness_scores[weakest_index]

    #create new to match the population
    population.append(generate_initial_population(1)[0])
    print('Current Generation:', count)

strongest_index = fitness_scores.index(max(fitness_scores))

solution_data = ([],[],[])
for x in range(0, len(population[strongest_index])):
    for count, i in enumerate(population[strongest_index][x]):
        
        if count == 0:
            solution_data[x].append(vehicles[i])
        else:
            solution_data[x].append(customers_data[i])

    best_solution = Solution(*solution_data)

print(best_solution)