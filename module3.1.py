calls = 0
def count_calls():
    global calls
    calls += 1

def string_info (string):
    count_calls()
    return len(string), string.upper(), string.lower()

def is_contains (string,list_to_search):
    count_calls()
    lower_list = [i.lower() for i in list_to_search]
    if string.lower() in lower_list:
        return True
    else:
        return False




print(string_info('Capybara'))
print(string_info('Armagedon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  
print(is_contains('cycle', ['recycle', 'cyclic']))
print(calls)
