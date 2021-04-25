# Domain Model for UC-15: UserData

**1) Extracting the Responsibilities**

| Responsibility Description                                   | Type | Concept Name |
| ------------------------------------------------------------ | ---- | ------------ |
| 콘셉트간의 작업을 결합시키고, 필요한 작업을 다른 콘셉트에게 요청한다.  |  D  | 컨트롤러   |
| 계정 정보이다. |  K |  계정정보  |
| 회원가입, 승인된 회원 정보를 데이터베이스에 저장한다.   |  D   |  저장 모듈  |


**2) Extracting the Associations**

| Concept pair | Association Description | Association Name |
| ------------------ | ----------------------- | ---------------- |
| 컨트롤러 <-> 저장 모듈 | 컨트롤러는 저장 모듈이 계정 데이터를 저장하게 한다.  | 요청 전달  |
|  |  |        |
|   |    |      |  

**3) Extracting the Attributes**

| Concept | Attributes | Attribute Description |
| ------- | ---------- | --------------------- |
| 계정정보 |  계정 데이터  |  계정 데이터이다.   |
