import asyncio
def show():
  print("Hello")

def is_blue(color):
  if color == "blue":
    return True
  else:
    return False
async def hello():
  print("ASYNC ASYNC")

def zip_with_idx(input_list, is_zero_based = True):
  if is_zero_based is True:
    return list(zip(list(range(len(input_list))), input_list))
  else:
    return list(zip(list(range(len(input_list) + 1)), [0] + input_list.copy()))[1:]

if __name__ == "__main__":
  show()
  r = is_blue("as")
  print(f'{r}')
  asyncio.run(hello())
  fruits = ["Apple", "Banana"]
  fruits_with_idx = zip_with_idx(fruits)
  for i in fruits_with_idx:
    print(i)
  print("********")
  fruits_with_idx_1 = zip_with_idx(fruits, False)
  for i in fruits_with_idx_1:
    print(i)