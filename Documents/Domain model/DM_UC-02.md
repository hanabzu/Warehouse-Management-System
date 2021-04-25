# Domain Model for UC-02 : Logout

**1) Extracting the Responsibilities**

| Responsibility Description                                   | Type | Concept Name |
| ------------------------------------------------------------ | ---- | ------------ |
| UseCase, UseCase의 논리적 집합 혹은 전체 시스템과 관련된 작업을 조정하고 다른 concept에 위임한다.  | D    | Controller   |
| 계정 정보 | K | AccountInfo |
| 유저가 로그아웃 입력 시 현재 시간을 가져온다 | D | TimeGetter |
| 유저 모듈과 커넥트하는 모듈 | D | UserModuleConnection |
| 로그아웃 후 페이지를 보여준다. | D   | ViewPage |
| 로그아웃 시의 페이지 정보 | K | PageInfo |



**2) Extracting the Associations**

| Concept pair | Association Description | Association Name |
| ------------------ | ----------------------- | ---------------- |
| Controller  <->   TimeGetter | 로그아웃 시의 time info를 가져온다. | get time |
| Controller  <->  UserModuleConnection | 컨트롤러는 AccountInfo와 time info를 UserModuleConnection으로 옮긴다. | convey request |
| ViewPage <-> PageInfo | 로그아웃 후 페이지를 보여준다.    | provides data |

**3) Extracting the Attributes**

| Concept | Attributes | Attribute Description |
| ------- | ---------- | --------------------- |
| TimeGetter | time info | 로그아웃 시도 시의 시간 정보 |

