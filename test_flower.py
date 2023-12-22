import flower

fruits = ["Apple", "Banana"]

def test_zip_with_idx():
  assert flower.zip_with_idx(fruits) == [(0, 'Apple'), (1, 'Banana')]
  assert flower.zip_with_idx(fruits, False) == [(1, 'Apple'), (2, 'Banana')]