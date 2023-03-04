# codebasics/py/Basics/Exercise/8_if/8_exercise_description.md
india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore", "karachi", "islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]
# 01
# city = input('City Name: ')

# if city in india:
#     print(f'{city} is in India')
# elif city in pakistan:
#     print(f'{city} is in Pakistan')
# elif city in bangladesh:
#     print(f'{city} is in Bangladesh')
# else:
#     print(f'{city} is not in our list')

# 02

city1, city2 = input("cities name:").split()

if (city1 and city2) in india:
    print(f'{(city1,city2)} is in India')
elif (city1 and city2) in pakistan:
    print(f'{city1,city2} is in Pakistan')
elif (city1 and city2) in bangladesh:
    print(f'{city1} and {city2} is in Bangladesh')
else:
    print(f'{city1,city2} is not in our list')
