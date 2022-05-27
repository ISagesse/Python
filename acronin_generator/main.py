# based on the user input turn it to an acronym, ATM, RAM
word = input('Enter words to convert to acronym: ')

#convert to upper case
word = word.upper()

# convert to a list
word_list = word.split()

for i in word_list:
    print(i[0], end='')
    