
train_mass = 22680
train_acceleration = 10
train_distance = 100

bomb_mass = 1
force =0

def get_force(mass, acceleration):
  force = mass * acceleration
  return force

def get_work(mass, acceleration, distance):
  force = mass * acceleration
  work = force * distance
  return work


new_force = get_force(train_mass, train_acceleration)

train_work = get_work(train_mass, train_acceleration, train_distance)
print(train_work)

print("The GE train supplies " + str(new_force) + " Newtons of force")

def get_energy(mass, c = 3*10**8):
  return mass * c*c

bomb_energy = get_energy(1)
print("A 1kg bomb supplies " + str(bomb_energy) + " Joules")

f_temp = 0
c_temp = 0

def f_to_c (f_temp):
   c_temp = (f_temp -32) * 5/9
   return c_temp 

f100_in_celsius = f_to_c(100)   
print(f100_in_celsius)

def c_to_f(c_temp):
  f_temp = c_temp * 9/5 + 32
  return f_temp

c0_in_fahrenheit = c_to_f(0)
print(c0_in_fahrenheit) 

