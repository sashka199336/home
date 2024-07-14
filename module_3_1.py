calls = 0
def count_calls ():
    global calls
    calls =15

def string_info (string):
    count_calls()
    return (len(string), string.upper(), string.lower())
def is_contains (string, list_to_search):
    count_calls()
    return string.upper() in [s.upper() for s in list_to_search]

print(string_info('Вкусочка'))
print(string_info('Жопасручкой'))
print(is_contains('Хохол', ['Хохол', 'ХОХОЛ', 'хохол']))
print(is_contains('Козел', ['Кызел', 'Казел']))
print(calls)
