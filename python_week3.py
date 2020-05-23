from bs4 import BeautifulSoup
import urllib.request

html=urllib.request.urlopen("http://www.swu.ac.kr/www/swuniversity.html")
result = BeautifulSoup(html.read(),"html.parser")

major=result.findAll("a") #a태그 내용을 major변수에 담음

print("""*** 서울여자대학교 학과 및 홈페이지 정보 ***
학과 \t\t\t 홈페이지""")

for s in major:#major내용으로 for문을 돌린다
    if  "대학원"in s.text or "교육원"in s.text: #대학원, 교육원 제외
        continue
    if s.text == "자율전공학부"or s.text == "공동기기실": #자율전공학부, 공동기기실 제외
        continue
    else: #이외 다른 학부
        page=urllib.request.urlopen("http://www.swu.ac.kr"+s["href"])#각 과의 전공페이지로 연결
        home=BeautifulSoup(page.read(),"html.parser")
        pageUrl=home.find("a",{"class","btn btn_xl btn_blue_gray"})#학과 홈페이지 url읽음

        if pageUrl is None :
            print(s.text+"\t\t홈페이지가 존재하지 않음")#주소가 없을 때 메세지
        elif "홈페이지" in pageUrl.text:
            print(s.text+"\t\t"+pageUrl["href"])#텍스트에 홈페이지가 있을 때 주소 출력(요람출력 방지)
        else:
            print(s.text+"\t\t홈페이지가 존재하지 않음")#홈페이지가 아닐 시 메세지
