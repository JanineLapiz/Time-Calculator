from utils.time_calculator import add_duration

print('********* Time Calculator *********')

start_time = input('Enter start time in 12-hour format: ')
duration = input('Enter duration: ')
start_day_of_week = input('Enter start day of week: ')

result = add_duration(start_time, duration, start_day_of_week)

print(f'Result: {result}')