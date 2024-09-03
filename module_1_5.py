tuple=1,2,'g','f'
immutable_var = tuple
print('Immutable tuple:',immutable_var)
food=['погода',2,'имя']
mutable_list= food
mutable_list[2]='арбуз'
print('Mutable list:',mutable_list)
immutable_var[1]='гиена' #невозможно изменить по той причине, что этот список изначально создан неизменяемым