from main import dec_one, parametrized_decor

@dec_one
def sum(x, y):
   return x + y

eleven = sum(5, 6)
nine = sum(5, 4)
result = sum(eleven, nine)

print('result: ', result)
print('result type: ', type(result))

@parametrized_decor(parameter='path')
def sum(x, y):
   return x + y

eleven = sum(5, 6)
nine = sum(5, 4)
result = sum(eleven, nine)

print('result: ', result)
print('result type: ', type(result))