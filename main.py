import requests as req

###
# GET : 요청, 값 가져오는 역할
# POST : 생성, 요청
# PUT : 수정, 덮어쓰기
# DELETE : 삭제

res = req.get('https://www.naver.com/')
print(res.request.headers)

# 응답시간https://github.com/mjh9401/PythonCrawling.git
print(res.elapsed)

# 응답값이 byte으로 나옴
print(res.raw)