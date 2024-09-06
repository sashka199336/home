def add_everything_up(a, b):
    try:
        res = a + b
        return round(res, 3)
    except TypeError:
        return f'{a}{b}'




print(add_everything_up(725.4463, 'теха'))
print(add_everything_up('маня', 6321))
print(add_everything_up(4343.43416, 8))
