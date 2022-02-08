from main import dec_one, parametrized_decor

#@dec_one def sum(x, y):return x + y; eleven = sum(5, 6); nine = sum(5, 4); result = sum(eleven, nine); print('result: ', result); print('result type: ', type(result))
@parametrized_decor(path)
def summator(x, y):
   return x + y

three = summator(1, 2)
five = summator(2, 3)

result = summator(three, five)

print('result: ', result)
print('result type: ', type(result))