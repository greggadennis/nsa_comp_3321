# Lesson 11: String Formatting

print('this is a formatted string {}'.format("--->hi i'm a formatted string argument<---"))

print('\n')
print('{2} {1} and {0}'.format('Henry', 'Bill', 'Bob'))

print('\n')
print('{who} is really {what}!'.format(who='Tony', what='awesome'))

cities = ['Dallas', 'Baltimore', 'DC', 'Austin', 'New York']
print('\n')
print('{0[4]} is a really big city'.format(cities))

lower_to_upper = {'a': 'A', 'b':'B', 'c':'C'}
print('\n')
print('This is a big letter {0[a]}'.format(lower_to_upper))
print('This is a big letter {lookup[a]}'.format(lookup=lower_to_upper))

print('\n')
for little, big in lower_to_upper.items():
  print('[-->{0:10} -- {1:10}<--]'.format(little, big))

print('\n')
print("{{0}} {0}".format('Where do I get printed?'))

the_way_i_want_it = '{0:>6} = {0:>#16b} = {0:#06x}'
print('\n')
for i in 1, 25, 458, 7890:
  print(the_way_i_want_it.format(i))