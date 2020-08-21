
#-----------------------------Physic's Class----------------------------------------------------

train_mass = 22680
train_acceleration = 10
train_distance = 100

bomb_mass = 1

def f_to_c(f_temp):
  return (f_temp - 32) * 5/9
f100_in_celsius = f_to_c(100)
print(f100_in_celsius)

def c_to_f(c_temp):
  return c_temp * (9/5) + 32
c0_in_fahrenheit = c_to_f(0)
print(c0_in_fahrenheit)

def get_force(mass, acceleration):
  return mass * acceleration
train_force = get_force(train_mass, train_acceleration)
print("The GE train supplies "+ str(train_force) + " Newtons of force.")

def get_energy(makis, c=3*10**8):
  return makis * c **2
bomb_energy = get_energy(bomb_mass)
print("A 1kg bomb supplies " + str(bomb_energy)+ " Joules.")

def get_work(mass, acceleration, distance):
  force = get_force(mass, acceleration)
  return force * distance

train_work = get_work(train_mass, train_acceleration, train_distance)

train_work = get_work(train_mass, train_acceleration, train_distance)
print("The GE train does " + str(train_work) +  " Joules of work over " + str(train_distance) + " meters.")

x=''
print(x)

#Shipping Costs

def cost_ground_shipping(weight):
  if (weight) <= 2:
    return weight * 1.5 + 20
  elif (weight) > 2 and (weight) <= 6:
    return weight * 3 + 20
  elif (weight) > 6 and (weight) <= 10:
    return weight * 4 + 20
  else:
    return weight * 4.75 + 20
  
print(cost_ground_shipping(2))
print(cost_ground_shipping(6))
print(cost_ground_shipping(10))
print(cost_ground_shipping(10.1))
print(cost_ground_shipping(22.1))
print(cost_ground_shipping(8.4))

cost_premium_ground_shipping = 125.00

def cost_drone_shipping(weight):
  if (weight) <= 2:
    return weight * 4.5
  elif (weight) > 2 and (weight) <= 6:
    return weight * 9
  elif (weight) > 6 and (weight) <= 10:
    return weight * 12
  else:
    return weight * 14.25
  
print(cost_drone_shipping(2))
print(cost_drone_shipping(6))
print(cost_drone_shipping(10))
print(cost_drone_shipping(10.1))
print(cost_drone_shipping(22.1))
print(cost_drone_shipping(1.5))

def cheapest_shipping_method(weight):
  if (weight) <= 2:
    return weight * 4.5
  elif (weight) > 2 and (weight) <= 6:
    return weight * 3 + 20
  elif (weight) > 6 and (weight) <= 10:
    return weight * 4 + 20
  elif (weight) > 10 and (weight) <= 22.1:
    return weight * 4.75 + 20
  else:
    return 125

print(cheapest_shipping_method(4.8))
print(cheapest_shipping_method(41.5))
print(cheapest_shipping_method(2))
  
x=''
print(x)

#Python Gradebook

last_semester_gradebook = [("politics", 80), ("latin", 96), ("dance", 97), ("architecture", 65)]
subjects = ["physics", "calculus", "poetry", "history"]
grades = [98, 97, 85, 88]
subjects.append('computer science')
grades.append(100)
gradebook = list(zip(subjects, grades))
gradebook.append(('visual arts', 93))
print(gradebook)
full_gradebook = gradebook + last_semester_gradebook
print(full_gradebook)

x=''
print(x)

#TNS Pizza

toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]
toppings1 = toppings[5]
prices = [2, 6, 1, 3, 2, 7, 2]

num_pizzas = len(toppings) 
print("We sell "+ str(num_pizzas) + " different kinds of pizza!")

pizzas = list(zip(prices, toppings))
pizzas.sort()
print(pizzas)

cheapest_pizza = pizzas[0]
priciest_pizza = pizzas[-1]
print("I will have your " + str(toppings1) + " pizza!")

three_cheapest = pizzas[:3]
print(three_cheapest)

num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)

x=''
print(x)

# Karl Clippers

hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]
prices = [30, 25, 40, 20, 20, 35, 50, 35]
last_week = [2, 3, 5, 8, 4, 4, 6, 2]
total_price = 0
total_revenue = 0
i = 0 

for price in prices:
  total_price += price

average_price = total_price / len(prices)
print("Average Haircut Price: {0}€".format(average_price))

new_prices = [price - 5 for price in prices]
print(new_prices)

for i in range(len(hairstyles)):
  total_revenue += prices[i] * last_week[i]
print("Total Revenue: {0}€".format(total_revenue))

average_daily_revenue = total_revenue / 7
print(average_daily_revenue)


