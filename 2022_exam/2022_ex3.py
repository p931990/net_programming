str = 'https://search.naver.com/search.naver?where=nexearch&ie=utf8&query=iot'

a=str.split('/')
b=a[3].split('&')

print(b)

d = {'where': 'nexearch', 'ie':'utf8', 'query':'iot'}


print(d)