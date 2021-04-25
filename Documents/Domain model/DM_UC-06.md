# Domain Model for UC-06 : AuthenticateUser 

**1) Extracting the Responsibilities**

| Responsibility Description                                   | Type | Concept Name |
| ------------------------------------------------------------ | ---- | ------------ |
| 데이터 모듈에 암호화된 사용자 계정이 존재한다. | K | DatabaseConnection |
| 암호화된 아이디, 패스워드를 전달한다.  | D | Controller  |
| 암호화된 패스워드가 일치하면 인증을 요청한다.  | D    |  Agree |
| 암호화된 패스워드가 불일치하면 인증거부 요청한다. | D | Refuse |
| 암호화된 아이디가 존재하지 않는다. | K | Accounts |



**2) Extracting the Associations**

| Concept pair | Association Description | Association Name |
| ------------------ | ----------------------- | ---------------- |
| Controller  <->  DatabaseConnection  |  암호화된 아이디, 패스워드를 전달한다.  | convey data |
| DatabaseConnection  <->  Accounts  |  패스워드가 일치하는 지 요청한다. | request data |
| DatabaseConnection <-> Ageree | 입력된 데이터가 암호화된 데이터와 일치함을 요청한다. | request data |
| DatabaseConnection <-> Refuse | 입력된 데이터가 암호화된 데이터와 불일치함을 요청한다. | request data |

**3) Extracting the Attributes**

| Concept | Attributes | Attribute Description |
| ------- | ---------- | --------------------- |
|  Accounts | 암호화된 계정 정보 | 입력된 아이디와 패스워드가 데이터 모듈에 존재함을 알려준다. |
| Agree | 계정 입력 | 입력된 데이터가 데이터 모듈에 있는 데이터가 일치한다. |
| Refuse | 계정 입력 | 입력된 데이터가 데이터 모듈에 있는 데이터가 일치하지않는다. |
