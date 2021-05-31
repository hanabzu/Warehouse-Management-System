### **UC-03 Register**

Home 페이지에서 회원가입을 클릭하면 실행

가입할 계정정보를 입력후 전송을 클릭하면 회원가입 요청

**TestCase:**

1) 여백 입력 -> 에러메시지 출력 (You have to fill all blanks) -> OK

2) 입력한 아이디가 5글자 미만   -> 에러메세지 출력 (ID is too short (least : 5)) -> OK

3) 입력한 아이디에 알파벳, 숫자 외의 문자 포함 -> 에러메세지 출력 (invalid ID) -> OK

4) 입력한 아이디가 이미 data_TempAccountInfo에 존재 -> 에러메세지 출력 (This ID waiting for accepting) -> OK

5) 입력한 패스워드에 공백 포함 -> 에러메세지 출력 (invalid password) -> OK

6) 입력한 패스워드가 8글자 미만  -> 에러메세지 출력 (password is too short (least : 8)) -> OK

7) 패스워드와 패스워드 확인이 서로 불일치 -> 에러메시지 출력 (You must type same passwords) -> OK

8) 입력한 아이디와 패스워드가 서로 같음 -> 에러메시지 출력 (Password and ID must differ) -> OK

9) 입력한 position, name, address에 특수문자 포함 -> 에러메시지 출력 (invalid position/name/address) -> OK

10)  입력한 아이디가 이미 data_AccountInfo에 존재 -> 에러메시지 출력 (already registered ID) -> OK

11) 모든 입력 데이터가 정상 -> data_TempAccountInfo에 저장 후 확인 페이지로 이동 -> OK









