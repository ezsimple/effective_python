# BETTER WAY 15
# 클로저가 변수 스코프와 상호 작용하는 방법을 알자

# %%

numbers = [ 0, 3, 1, 2, 5, 4, 7, 6]
group = { 2, 3, 5, 7 }

def sort_priority(values, group):
  def helper(x):
    if x in group:
      return (0, x)
    return (1, x)

  values.sort(key=helper)

sort_priority(numbers, group)
print(numbers)

# %%
numbers = [ 0, 3, 1, 2, 5, 4, 7, 6]
group = { 2, 3, 5, 7 }

# [2, 3, 5, 7, 0, 1, 4, 6]
def sort_priority2(values, group):
  found = False
  def helper(x):
    if x in group:
      found = True # ???
      return (0, x)
    return (1, x)

  values.sort(key=helper)
  return found

sort_priority2(numbers, group)
print(numbers)