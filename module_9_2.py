first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']
united_list = first_strings + second_strings
print(united_list)

first_result = [len(item) for item in first_strings if len(item)>5]
second_result = [(item1, item2)for item1 in first_strings for item2 in second_strings if len(item1) == len(item2)]
third_result = []

# парой ключ-значение будет строка-длина строки.
# Значения строк будут перебираться из объединённых вместе списков first_strings и second_strings.
# Условие записи пары в словарь - чётная длина строки.

print(first_result)
print(second_result)
print(third_result)

