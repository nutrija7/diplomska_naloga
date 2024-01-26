import numpy as np

file_path = './data/validacija.txt'  

column1_values = []
column2_values = []
percentage_differences = []

with open(file_path, 'r') as file:
    for line in file:
        values = [float(val) for val in line.split()]
        
        column1_values.append(values[0])
        column2_values.append(values[1])

        if values[1] != 0:
            percentage_difference = (abs(values[0] - values[1]) / abs(values[1])) * 100
            percentage_differences.append(percentage_difference)
        else:
            percentage_differences.append(None)  


average_percentage_difference = np.nanmean(percentage_differences)
print(average_percentage_difference)