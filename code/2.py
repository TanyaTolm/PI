from pprint import pprint

my_dict = {"first": 'so easy'}

def dict_maker(**kwards):
    my_dict.update(**kwards)

dict_maker(a1=1, a2=20, a3=54, a4=13)
dict_maker(name = '', age=31, weight = 70, eyes_color='blue')
pprint(my_dict)