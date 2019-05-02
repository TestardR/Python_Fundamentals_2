print('Imported my_module...')

test = 'Test String'


def find_index(to_search, target):
    # Find the idnex of a value in a sequence
    for index, value in enumerate(to_search):
        if value == target:
            return index

    return -1
