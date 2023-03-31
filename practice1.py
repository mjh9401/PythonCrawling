import requests as req

res = req.get('https://finance.naver.com/marketindex/?tabSel=exchange#tab_section')

html = res.text

pos = html.find('감나무')

print(pos)

# find값이 존재하지 않으면 -1을 리턴, 존재하면 해당 위치값을 리턴

s = html.split('<span class="value">')[1].split('</span>')[0]
# s = html.split('<span class="value">')[1]
print(s)