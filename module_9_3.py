first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']
united = zip( first, second)

first_result = [abs(len(item[0]) - len(item[1])) for item in united if len(item[0]) != len(item[1])]
second_result = [len(first[ii]) == len(second[ii]) for ii in range( 0, len(first))]

print(list(first_result))
print(list(second_result))