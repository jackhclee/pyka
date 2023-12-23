import asyncio
import transformers

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

def guess(sentence):
  albert = "albert-base-v2"
  bert = "bert-base-uncased"
  bart = "facebook/bart-base"
  p = transformers.pipeline("fill-mask", model=albert)
  # print(sentence.replace('[MASK]','<mask>'))
  # return p(sentence.replace('[MASK]','<mask>'))
  return p(sentence)

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
  for result in guess("The man is a [MASK]."):
    print(result)
  for result in guess("The woman is a [MASK]."):
    print(result)
  for result in guess("The [MASK] treats the patient."):
      print(result)
  for result in guess("[MASK] save the queen."):
    print(result)