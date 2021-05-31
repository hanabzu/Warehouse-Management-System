# Domain Model for UC-01 : Login

**1) Extracting the Responsibilities**

| Responsibility Description                                   | Type | Concept Name |
| ------------------------------------------------------------ | ---- | ------------ |
| UseCase, UseCase의 논리적 집합 혹은 전체 시스템과 관련된 작업을 조정하고 다른 concept에 위임한다.  | D    | Controller   |
| 유저가 입력한 아이디, 패스워드 | K    | UserInput |
| 유저가 로그아웃 입력 시 현재 시간을 가져온다 | D | TimeGetter |
| 유저 모듈과 커넥트하는 모듈 | D | UserModuleConnection |
| 로그인 페이지과 완료 페이지를 보여준다. | D   | Page Maker           |
| 로그인 버튼과 성공 여부 페이지에 대한 정보 | K | PageInfo |



**2) Extracting the Associations**

| Concept pair | Association Description | Association Name |
| ------------------ | ----------------------- | ---------------- |
| Controller  &lt;-&gt;   TimeGetter | 로그인 시의 time info를 가져온다. | convey data |
| Controller  <->   UserInput | 컨트롤러는 유저가 입력한 정보를 받아서 ID와 password로 전달한다. | convey data |
| Controller  <->  UserModuleConnection | 컨트롤러는 유저가 입력한 정보와 time info를 UserModuleConnection으로 옮긴다. | convey data |
| UserModuleConnection<->Pagemaker | UserModuleConnection이 로그인 성공여부와 계정정보를 ViewPage에 전달한다. |  convey data  |
| ViewPage <-> PageInfo | 로그인 성공 여부에 따라 Page를 보여준다.                     | provides data |

**3) Extracting the Attributes**

| Concept | Attributes | Attribute Description |
| ------- | ---------- | --------------------- |
| UserInput | ID, password | 유저가 입력한 정보를 아이디와 패스워드로 구분 |
| UserModuleConnection | AccessInfo   | 로그인 성공 여부 |
|  | AccountInfo | 계정 정보 |
| TimeGetter | time info | 로그인 시도 시의 시간 정보 |

