url = 'https://search.naver.com/search.naver?where=nexearch&ie=utf8&query=iot'

# 파라미터 추출
params = url.split('?')[1].split('&')

# 딕셔너리 생성
result = {}
for param in params:
    key, value = param.split('=')
    result[key] = value

# 결과 출력
print(result)