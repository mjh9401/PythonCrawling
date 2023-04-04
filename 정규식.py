import re

s = 'how are you?'
print(re.match(r'how are you\?',s))

# A, B, C, F 등급
e = '이 영화는 F등급 입니다'

print(re.match(r'이 영화는 [ABCF]등급 입니다',e))                                           
print(re.findall(r'이 (.+)는 (.*)등급 입니다',e))  