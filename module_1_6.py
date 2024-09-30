from dicts import list_

my_dict_ = {'Alex': 1976, 'Boris': 1980, 'Anton': 1984}
print(my_dict_)
print(my_dict_['Boris'])
print(my_dict_.get('Anna'))
my_dict_.update({'Karina': 1977, 'Anna': 1975})
a  = my_dict_.pop('Boris')
print(a)
print(my_dict_)


my_set_ = {1, 1, 1, 'Яблоко', 42.314}
print(my_set_)
list_= [13, (5,6,1.6)]
list_ = set(list_)
print(my_set_.update(list_))
print(my_set_.remove(1))
print(my_set_)

