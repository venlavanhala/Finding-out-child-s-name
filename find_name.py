
file = open("names.txt", "r")
all_names = file.read().splitlines()
file.close()
names = [name.lower() for name in all_names]

allowed_letters = ["a", "i", "v", "u", "n", "l", "r", "e", "o", "m", "-"]
unused_letters = {key: [] for key in allowed_letters}
print(unused_letters)
allowed_names = []

# return names that only have allowed letters
def filter_names(letters):
    for name in names:
        check = True
        for letter in name:
            if letter not in letters:
                check = False
        if check == True:
            allowed_names.append(name)
    return allowed_names
    
# return names based on non-used letters
def missing_letter(names, letters):
    for name in names:
        for letter in letters:
            if letter not in name:
                unused_letters[letter].append(name)
    # one has to have "-" in it
    
    return unused_letters


#print(filter_names(allowed_letters))
print(missing_letter(filter_names(allowed_letters), allowed_letters))
