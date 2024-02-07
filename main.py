#GENERATORS
def my_generators():
  for i in range(50):
    yield i

gen = my_generators()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

for g in gen:
  if g < 25:
    print(g + 1)