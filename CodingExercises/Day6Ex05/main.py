row = input('Add a new member: ')

file = open('members.txt', 'r')
members = file.readlines()
file.close()

members.append(row + '\n')

file = open('members.txt', 'w')
file.writelines(members)
file.close()

file = open('members.txt', 'r')
members = file.readlines()
file.close()

for name in members:
    print(name)
