bob={
    'pay':50000,
    'age': 35,
    'name': 'Bob Smith'
}

sue={
    'pay':40000,
    'age':26,
    'name':'Sue Jones'
}

people=[bob,sue]
for person in people:
    print(person['name'], person['pay'], sep=' = ')