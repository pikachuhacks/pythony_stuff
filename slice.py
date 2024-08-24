numbers = [1, 2, 3, 4]
text = "My name is Pika"



# Slice vs [::-1]
rev = slice(None, None, -2)

print(numbers[rev])
print(text[rev])

print("#################################")


#Combining sets
set_a = {1, 2, 4, 5, 6}
set_b = {5, 6, 7, 8}

print(set_a | set_b)
print(set_a - set_b)
print(set_a & set_b)

