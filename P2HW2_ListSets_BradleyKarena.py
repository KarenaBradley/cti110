# CTI-110
# P2HW2 - List and Sets
# Karena Bradley 
# 6-19-2021

input_string = input('Enter a series of 10 numbers: ')
print("\n")
num_list = input_string.split()

print('List: ', num_list)


for i in range(len(num_list)):
    num_list[i] = int(num_list[i])

print('Lowest number = ', min(num_list))

print('Highest number = ', max(num_list))

print('Total = ',sum(num_list))

