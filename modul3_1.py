calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    length = len(string)
    upper_case = string.upper()
    lower_case = string.lower()
    return(length, upper_case, lower_case)

def is_contains(string, list_to_search):
    count_calls()
    return string.upper() in (item.upper() for item in list_to_search)

result = string_info('Capybara')
print(result)
result = string_info('Armageddon')
print(result)
result = is_contains('urban', ('Urban', ['ban', 'BaNaN', 'urBAN']))
print(result)
result = is_contains('urban', ('cycle', 'recycling', 'cyclic'))
print(result)
print(calls)