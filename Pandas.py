import pandas as pd

world_economies = {
    'countries': ['USA', 'Russia', 'Japan', 'China', 'Canada'],
    'GPD': ['$27trln', '$2trln', '$4trln', '$17trln', '$2trln'],
    'Population': ['334mln', '144mln', '124mln', '1.4bln', '39mln']
}

overall_economy = pd.DataFrame(world_economies) #Creates a table directly in python


print(overall_economy)
print(overall_economy.shape) #The size of the table
print(overall_economy.values[1, 1]) #As 'pandas' works based on NumPy, here we are printing a specific element by its coordinates (world_economies is a two-dimensional array)
print(overall_economy.head(3)) #The first three lines
print(overall_economy.tail(2)) #The last 2 lines