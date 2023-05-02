url = 'https://search.daum.net/search?w=tot&q=bigdata'
url2 = 'https://search.daum.net/search?w=tot&q=iot'
# 파라미터 추출
params = url.split('?')[1].split('&')

# 딕셔너리 생성
result = {}
for param in params:
    key, value = param.split('=')
    result[key] = value

# 결과 출력
print(result)

#반복
params = url2.split('?')[1].split('&')
for param in params:
    key, value = param.split('=')
    result[key] = value

#두번째 결과 출력
print(result)