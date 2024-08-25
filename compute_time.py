import time

number1 = []
number2 = []
number3 = []

def calculate_square(num):
    for i in range(num):
        number1.append(i*i)

def calculate_cube(num):
    for i in range(num):
        number1.append(i*i*i)

def calculate_four(num):
    for i in range(num):
        number1.append(i*i*i)


for i in range(10):
    start = time.time()

    calculate_square(1000000);
    calculate_cube(1000000);
    calculate_four(1000000);

    end = time.time()

    print("Duration: " + str(end - start))
  

