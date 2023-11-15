some_string = input()
my_dict = {}
for letter in some_string:

    if letter not in my_dict:
        my_dict[letter] = 0
    my_dict[letter] += 1

for letters, times in sorted(my_dict.items(), key = lambda x: x[0]):

    print(f"{letters}: {times} time/s")
