def calculate_structure_sum(data_structure):
  total_sum = 0

  def helper(item):
    nonlocal total_sum
    if isinstance(item, (int, float)):
      total_sum += item
    elif isinstance(item, str):
      total_sum += len(item)
    elif isinstance(item, (list, tuple, set)):
      for element in item:
        helper(element)
    elif isinstance(item, dict):
      for key, value in item.items():
        helper(key)
        helper(value)

  helper(data_structure)

  return total_sum

data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]
result = calculate_structure_sum(data_structure)
print(result)
