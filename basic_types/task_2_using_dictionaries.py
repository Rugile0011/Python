p1 = {'name': 'Foo', 'karma': 123, 'value': -1}
p2 = {'karma': 123, 'value': -1}
p3 = {'name': 'Foo', 'value': -1}

dict_filter = lambda x, y: dict([(i, x[i]) for i in x if i in set(y)])

key_karma = "karma"
key_name = "name"


def new_p1_dictionary():
    """Adjust p1 dictionary and get keys name and karma"""
    new_p1 = ("name", "karma")
    modified_p1 = dict_filter(p1, new_p1)
    if key_karma and key_name in p1:
        print(f'New p1 dictionary: ', modified_p1)


def new_p2_dictionary():
    """Adjust p2 dictionary and get keys name and karma"""
    new_p2 = ("name", "karma")
    modified_p2 = dict_filter(p2, new_p2)
    if key_karma and key_name in p2:
        print(f'New p1 dictionary: ', modified_p2)
    else:
        modified_p2['name'] = 'Unknown'
        print(f'New p2 dictionary: ', modified_p2)


def new_p3_dictionary():
    """Adjust p3 dictionary and get keys name and karma"""
    new_p3 = ("name", "karma")
    modified_p3 = dict_filter(p3, new_p3)
    if key_karma and key_name in p2:
        print(f'New p1 dictionary: ', modified_p3)
    else:
        modified_p3['karma'] = 'Unknown'
        print(f'New p3 dictionary: ', modified_p3)


print(new_p1_dictionary())
print(new_p2_dictionary())
print(new_p3_dictionary())
