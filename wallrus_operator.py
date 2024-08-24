inventory = {'coffee': 20, 'milk': 10, 'chocolates': 10}

# product = inventory.get('coffee')
# product = inventory.get('beans')

if product:= inventory.get('coffee'):
    print(f'{product} available')
else:
    print(f'Product not available')


