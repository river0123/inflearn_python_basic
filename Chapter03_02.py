# Chapter03-2
# 파이썬 문자형
# 문자형 중요

# 문자열 생성
str1 = "I am Python"
str2 = 'Python'
str3 = """How are you?"""
str4 = '''Thank you'''

print(type(str1), type(str2), type(str3), type(str4))
print(len(str1), len(str2), len(str3), len(str4))


# 빈 문자열
str1_t1 = ''
str2_t2 = str()

print(type(str1_t1), len(str1_t1))
print(type(str2_t2), len(str2_t2))


# 이스케이프 문자 사용
"""
참고 : Escape 코드

\n : 개행
\t : 탭
\\ : 문자
\' : 문자
\" : 문자
\000 : 널 문자
...
"""
# I'm Boy

print("I'm boy")
print('I\m boy')

print('a \t b')
print('a \"\" b')

escape_str1 = "Do you have a \"retro games\"?"
print(escape_str1)
escape_str2 = 'What\'s on TV?'
print(escape_str2)

# 탭, 줄 바꿈
t_s1 = "Click \t start!"
t_s2 = "New Line \n Check!"

print(t_s1)
print(t_s2)
print()

# Raw String
raw_s = r'D:\python\test'
print(raw_s)
print()

# 멀티라인 입력
multi_str = \
'''
String
Multi Line
Test
'''

asdf = \
'asdfawef' \
'iuqpjwerf'
print(multi_str)
print(asdf)

# 문자열 연산
str_o1 = "Python"
str_o2 = "Apple!"
str_o3 = "How are you doing"
str_o4 = "Seoul Daejeon Busan Jinju"

print(str_o1 * 3)
print(str_o1 + str_o2)
print('y' in str_o1)
print('z' in str_o1)
print('P' in str_o2)

# 문자열 형 변환
print(str(66), type(str(66)))
print(str(10.1))
print(str(True), type(str(True)))


# 문자열 함수(upper, isalnum, startswith, count, endswitch, isalpha...)

print("Capitalize : ", str_o1.capitalize())
print("endswitch: ", str_o2.endswith("!"))
print("replace", str_o1.replace("thon", 'Good'))
print("sorted: ", sorted(str_o1))
print("split: ", str_o4.split(' '))


# 반복(시퀀스)
im_str = "Good Boy!"

print(dir(im_str)) # __iter__

# 출력
for i in im_str:
    print(i)

# 슬라이싱
str_s1 = "Nice Python"

print(len(str_s1))

# 슬라이싱 연습
print(str_s1[0:3]) # 0 1 2
print(str_s1[5:]) #[5:11]
print(str_s1[:len(str_s1)]) # str_s1[:11]
print(str_s1[:len(str_s1)-1]) # str_s1[:10]
print(str_s1[1:9:2])
print(str_s1[1:-2])
print(str_s1[::2])
print(str_s1[::-1])


# 아스키 코드(또는 유니코드)

a = 'z'

print(ord(a))
print(chr(122))
