### **UC-01 Login

Home 페이지에서 로그인을 클릭하면 실행

ID와 PW를 입력하고 submit을 클릭하면 로그인 시도

**TestCase:**

1) 여백 입력 -> 에러메시지 출력 (You have to fill all blanks) -> OK

2) 입력한 아이디가 5글자 미만 -> 에러메세지 출력 (ID is too short (least : 5)) -> OK

3) 입력한 아이디에 알파벳, 숫자 외의 문자 포함 -> 에러메세지 출력 (invalid ID) -> OK

4) 입력한 패스워드에 공백 포함 -> 에러메세지 출력 (invalid password) -> OK

5) 입력한 패스워드가 8글자 미만  -> 에러메세지 출력 (password is too short (least : 8)) -> OK

6) 입력한 아이디와 일치하는 계정이 존재하지 않음 -> 에러메시지 출력 (No match ID) -> OK

7) 입력한 아이디는 일치하나 패스워드는 틀린 경우 -> 로그인 실패 로그 저장 후 에러 메세지 출력 (Wrong password) -> OK

8) 입력한 아이디, 패스워드가 일치하는 계정 존재 -> 로그인 성공 로그 저장 후 로그인 성공 페이지로 이동 -> OK

9) 로그인한 아이디가 admin계정일 경우 -> 회원가입 수락 기능 추가 -> OK







