## Built in Function

dir([1,2,3,4]) #내장 메서드를 보여줌, 메서드 기억 안나면 찾아서 사용

format(10000000,',' ) #','를 기준으로 원을 표현할 때 사용
format(10000000,'e' ) #지수 표현
format(10000000,'x' ) #16진수 표현
format(10000000,'!>020,.4f' ) #20자리로 앞에는 !로 채울것이며 소수점은 4자리까지
#시간표현, 비트단위 이진 연산 할때 유용

def hojun(value):
    if value % 2 == 0:
        return value
    else:
        return None
list(filter(hojun, range(20))) #어떤 값들을 특정 함수로 필터를 줄때 사용
#출력 [2,4,6,8,10,12,14,16,18]

list(filter(lambda x:x%2==0, range(20))) #true인것만 출력
#출력 [0,2,4,6,8,10,12,14,16,18]

[i for i in range(20) if i%2 == 0]
#출력 [0,2,4,6,8,10,12,14,16,18]

len([1,2,3,4]) #길이출력

map(function, value)
list(map(hojun, range(20)))
list(map(lambda x:x%2==0, range(20)))
#map은 결과값은 반환, filter는 결과값에 해당하는 값을 출력

list(map(lambda x:x**2, range(20)))
#이건 값으로 출력

#하나씩 매핑이 됨
list(zip(['a','b','c','d'], [1,2,3,4]))
#출력 [('a', 1), ('b', 2),...]
list(zip(['a','b','c','d'], [1,2,3,4], [10,20,30,40]))
#출력 [('a', 1, 10), ('b', 2, 20),...]
list(zip(['a','b','c','d'], [1,2,3,4], [10,20,30,40], 'ABCD'))
#출력 [('a', 1, 10,'A'), ('b', 2, 20 'B'),...]

max([1,2,3,4]) #최대
min([1,2,3,4]) #최소

reversed()
sorted()
l = [10,5,4,3,7,6]
l.sort()
# l의 출력값 = [3,4,5,6,7,10]
#sort는 list를 직접만짐, sorted는 list를 직접 만지지않음 리턴값만 정렬된 값이 있냐


testCaseOne = ['abc', 'def', 'hello world', 'hello', 'python']
testCaseTwo = 'Life is too short, You need python'.split()
testCaseThree = list(zip('anvfe', [1,2,5,4,3]))
sorted(testCaseOne, key=len)
# 출력 ['abc', 'def', 'hello', 'python', 'hello world']
sorted(testCaseOne, key=len, reverse= True)
# 출력 ['hello world', 'python', 'hello', 'abc', 'def']
sorted(testCaseTwo, key=str.lower)
# 출력 ['is', 'Life', 'need', 'python', 'short', 'too', 'You']
# 대소문자 구분없이 알파벳 앞에 있는 걸로 정렬
sorted(testCaseThree, key=lambda x:x[1])
# 출력 [('a', 1), ('n', 2), ('e', 3), ('f', 4), ('v', 5)] 뒤에 있는 숫자순으로 정렬
sorted(testCaseThree, key=lambda x:x[0])
# 출력 [('a', 1), ('e', 3), ('f', 4), ('n', 2), ('v', 5)] 앞에 있는 알파벳순으로 정렬
#리스트 안에 튜플 형태 - dictionary를 items했을때 이런 구조를 가져오게 됨 == dictionary 정렬하고 싶을 때 사용

5 in [1,2,3,4,5] # true 출력
5 not in [1,2,3,4,5] #false 출력

append #하나의 요소만 추가
clear #모든 요소를 다 없앰

copy #복사를 하는데 어떤 list를 function으로 넘길 때 function에서 만지지 못하도록 하기 위해서
def listChange(x):
    x[0] = 1000
l = [1,2,3,4,5]
listChange(l) # 1출력 [1000,2,3,4,5]
listChange(l.copy()) # 1출력 [1,2,3,4,5]

#리스트
l = [1,2,3,4,5]
dir(l)
count #갯수 세줌
extend #요소를 많이 추가할 때
index #어떤 요소를 찾을 때
insert #해당되는 자리에 요소를 넣을 때
pop #뒤에서 값을 꺼낼 때
remove # 어떤 요소의 값을 지울 때
# O(n)이라서 del로 지우는 게 좋음 == 시간 측정하는 문제라면
reverse #역순
sort #정렬

l = []
l.append(10)
l.append(20)
l.append(30)
l.pop(0) # 가장 먼저 들어온 데이터 10이 나감 - 큐의 구조
l.pop() #가장 늦게 들어온 데이터 30이 나감 - 스택의 구조

#튜플
t = (1,2,3)
dir(t)
#count, index만 있어서 넘어감

#dictionary
d = {'one':'하나', 'two':'둘'}
dir(d)

#중복존재 - clear, copy, pop
d.keys() #key만 뽑아내라
d.values() #value만 뽑아내라
d.items() #둘다 뽑아내는데 리스트 안에 튜플의 형태로 뽑아내라

del d['one'] #키를 기준으로 제거함
d['one'] = '하나' #이런식으로 데이터를 넣어주면된다


#집합
s = set('11122345666')
# s출력 {'1', '2', '3', '4', '5', '6'}
# 순서가 없어서 순회 할때는 주의

dir(s)
add #어떤 요소 추가
discard # 요소 삭제
difference # 차집합 ex) 집합하나.difference(집합둘)
update #한꺼번에 데이터 많이 추가하고 싶을때
remove # 요소 제거
union #합집합
'1' in s

#판콜에이라는 약 성분이 A,B,C가 있다고 할 때 다른 약과의 유사성분을 알고 싶을 때
판콜에이 = {'A', 'B', 'C'}
타이레놀 = {'A', 'B', 'D'}

print(판콜에이.difference(타이레놀)) #차집합 : 출력 - C
print(판콜에이.intersection(타이레놀)) #교집합 : 출력 - A, B
print(판콜에이.union(타이레놀)) #합집합 : 출력 - A,B,C,D


data = '가 나 가 가 나 다 다 라 마'
len(set(data.split()))
d = {}
for i in set(data.split()):
    print(i, data.split().count(i))
    # d[i] = data.split().count(i)



