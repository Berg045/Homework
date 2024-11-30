
first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
first_result = [len(word) for word in first_strings if len(word) >= 5]

second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']
second_result = [(word1, word2) for word1 in first_strings for word2 in second_strings if len(word1) == len(word2)]

combined_strings = first_strings + second_strings
third_result = {word: len(word) for word in combined_strings if len(word) % 2 == 0}

print(first_result)
print(second_result)
print(third_result)