# %%

class BetterCountMissing(object):
    def __init__(self):
      self.added = 0

    def __call__(self, *args, **kwds):
      self.added += 1
      print(self.added)
      return 0


if __name__ == '__main__':
   counter = BetterCountMissing()
   counter()

   assert callable(counter)
# %%

class LazyDB(object):
  def __init__(self) -> None:
      self.exists = 5

  def __getattr__(self, name):
      value = f'Value for {name}'
      setattr(self, name, value)
      return value

# %%
class RegistryMeta(type):
    registry = []  # 클래스 이름을 저장할 리스트

    def __new__(cls, name, bases, attrs):
        # 새로운 클래스를 생성
        new_class = super().__new__(cls, name, bases, attrs)
        # 클래스 이름을 등록
        cls.registry.append(name)
        return new_class

# 메타클래스를 사용하는 기본 클래스
class BaseClass(metaclass=RegistryMeta):
    pass

# 서브클래스 정의
class FirstClass(BaseClass):
    pass

class SecondClass(BaseClass):
    pass

# 클래스가 등록되었는지 확인
print("등록된 클래스:", RegistryMeta.registry)

# 실행
# 등록된 클래스: ['BaseClass', 'FirstClass', 'SecondClass']

# %%

import functools

def my_decorator(func):
    @functools.wraps(func)  # 원래 함수의 메타데이터를 유지
    def wrapper(*args, **kwargs):
        print("함수를 호출합니다.")
        result = func(*args, **kwargs)  # 원래 함수 호출
        print("함수가 호출되었습니다.")
        return result
    return wrapper

@my_decorator
def say_hello(name):
    """인사말을 출력하는 함수."""
    print(f"안녕하세요, {name}!")

# 사용 예
say_hello("뤼튼")
print(say_hello.__name__)  # 원래 함수 이름 확인
print(say_hello.__doc__)   # 원래 함수의 문서화 문자열 확인

# %%
import pickle

# 저장할 데이터
data_list = [1, 2, 3, 4, 5]
data_dict = {'name': '뤼튼', 'age': 30, 'city': '서울'}

# 데이터 파일에 저장하기
with open('data.pkl', 'wb') as file:
    pickle.dump(data_list, file)  # 리스트 저장
    pickle.dump(data_dict, file)   # 딕셔너리 저장

print("데이터가 파일에 저장되었습니다.")

# 파일에서 데이터 읽기
with open('data.pkl', 'rb') as file:
    loaded_list = pickle.load(file)  # 리스트 읽기
    loaded_dict = pickle.load(file)   # 딕셔너리 읽기

print("읽어온 리스트:", loaded_list)
print("읽어온 딕셔너리:", loaded_dict)

# %%
import pickle

# 사용자 정의 클래스
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        #  __repr__ 메서드를 오버라이드하여 객체의 문자열 표현을 제공합니다.        
        return f"Person(name={self.name}, age={self.age})"

    def __reduce__(self):
        # 직렬화 시 호출되는 메서드
        return (unpickle_person, (self.name, self.age))

# 역직렬화 함수
def unpickle_person(name, age):
    return Person(name, age)

# copyreg에 등록하지 않고 __reduce__ 메서드만 정의
# copyreg.pickle(Person, Person.__reduce__) # 이 부분은 필요 없음

# 사용 예
person = Person("뤼튼", 30)

# 객체 직렬화
serialized_person = pickle.dumps(person)
print("직렬화된 데이터:", serialized_person)

# 객체 역직렬화
deserialized_person = pickle.loads(serialized_person)
print("역직렬화된 객체:", deserialized_person)

# %%
import builtins

# 내장 자료 구조 목록
data_structures = [name for name in dir(builtins) if isinstance(getattr(builtins, name), type)]
print("내장 자료 구조:")
print(data_structures)

# %%
import functools
import itertools

# functools의 함수 목록
functools_functions = dir(functools)
print("functools의 함수:")
print(functools_functions)

# itertools의 함수 목록
itertools_functions = dir(itertools)
print("itertools의 함수:")
print(itertools_functions)


# %%
import builtins

# 내장 자료 구조 목록과 docstring 출력
data_structures = [(name, getattr(builtins, name).__doc__) for name in dir(builtins) if isinstance(getattr(builtins, name), type)]

print("내장 자료 구조 및 docstring:")
for name, doc in data_structures:
    print(f"{name}: {doc}")
