import statistics

def find_average(numbers):
    average = statistics.mean(numbers)
    return average

numbers = [1,2,3,4,5]
print(find_average(numbers))