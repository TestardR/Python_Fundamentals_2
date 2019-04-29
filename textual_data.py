message = 'Hello World'

print(message)
print(len(message))
print(message[10])
print(message[:5])
print(message[6:])
print(message.upper())
print(message.count('o'))
print(message.find('World'))

new_message = message.replace('World', 'Romain')

print(new_message)

greeting = 'Hello'
name = 'Vanessa'

last_message = f'Hello {name.upper()}. Welcome!'
print(last_message)

# see all methods available
print(dir(name))
print(help(name.upper))
