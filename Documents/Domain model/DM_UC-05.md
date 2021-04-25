# Domain Model for UC-05 : ModifyProfile 

**1) Extracting the Responsibilities**

| Responsibility Description                                   | Type | Concept Name |
| ------------------------------------------------------------ | ---- | ------------ |
| 유저가 계정정보 수정 버튼을 클릭한다.  | D    | Controller   |
| 시스템이 패스워드 재입력을 요청한다.       |  K |  re-input |
| 유저가 패스워드를 입력한다.  | D    | DatabaseConnection  |
| 시스템은 유저 모듈에 계정의 아이디와 유저가 입력한 패스워드를 전달한다. | D | DatabaseConnection |
| 시스템이 유저에게 계정 정보를 수정할 수 있는 창을 띄운다. | K  | Interface |
| 유저가 계정 정보를 수정한다. | D  | DatabaseConnection   |
| 시스템이 새로운 계정 정보를 유저 모듈에 알린다. | D  | 유저모듈  |
| 시스템이 유저에게 계정 정보가 변경되었음을 알린다. | K | info  |



**2) Extracting the Associations**

| Concept pair | Association Description | Association Name |
| ------------------ | ----------------------- | ---------------- |
| DatabaseConnection  <->   유저 모듈 |  유저 계정 정보가 변경되었음을 알린다.   | convey request |
| Controller  <->  DatabaseConnection  |  유저 계정 정보 수정을 요청한다.  | convey request |

**3) Extracting the Attributes**

| Concept | Attributes | Attribute Description |
| ------- | ---------- | --------------------- |
|  info | 변경 사항 알림 | 유저에게 변경되었음을 알린다. |
| re-input | 재입력 알림 | 유저에게 패스워드 재입력을 요청한다. |
| interface | 수정 가능한 페이지 | 계정 정보 수정 페이지 |
