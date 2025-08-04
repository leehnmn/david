from flask import Flask #flask는 웹서버 만들기 위한 파이썬 라이브러리 , Flask는 그중에 웹서버 생성틀

app = Flask(__name__) #app는 변수 Flask(__name__)은 웹서버 만드는 명령어, __name__은 실행중인 파일 이름

@app.route("/") #의문. 왜 "/" 가 루트로 정해질수있는가. #웹에서 주소입력시 함수 실행 
def hello_world(): #위 실행시에 호출함수는 hello_world이다.
    return "Hello, DevOps!"  #함수실행시 문자를 반환.

if __name__ == "__main__": #파이썬 파일이 실행될때 파이썬 자체에서 name을 만듦 그리고 직접실행된 경우에 파이썬에서 변환한 것이 main이다.
    # 즉 직접실행한경우에는 name이 main으로 바뀌면서 변화한다. 그때 if실행문 실횅
    app.run(host="0.0.0.0", port=5004) #app 변수를 호출함 flask 앱실행명령 이때 호스트 -외부컴퓨터 포트번호 -문번호 
    #80진행시 엑세스 거절.
    
