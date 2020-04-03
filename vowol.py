import keyboard

triggers = ('a', 'e', 'i', 'u')
target = 'o'

for trigger in triggers:
	keyboard.remap_key(trigger, target)

input("Press enter to quit\n")
