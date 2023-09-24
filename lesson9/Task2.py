import pandas as pd

file_path = 'sample_data/california_housing_train.csv'
data = pd.read_csv(file_path)

min_population = data['population'].min()

zone_with_min_population = data[data['population'] == min_population]

max_households_in_zone = zone_with_min_population['households'].max()

print("Максимальное количество households в зоне с минимальным значением population:", max_households_in_zone)
