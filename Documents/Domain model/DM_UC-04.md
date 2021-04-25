# Domain Model for UC-04 : AcceptUsers

**1) Extracting the Responsibilities**

| Responsibility Description                                   | Type | Concept Name |
| ------------------------------------------------------------ | ---- | ------------ |
| UseCase, UseCase의 논리적 집합 혹은 전체 시스템과 관련된 작업을 조정하고 다른 concept에 위임한다.  | D    | Controller   |
| 유저 모듈과 커넥트하는 모듈 | D | UserModuleConnection |
| 어드민이 가입 거부 이유를 입력할 수 있도록 한다. | D | InputOperator |
| 임시 계정 정보를 보여준다. | D   | ViewPage |
| 수락 버튼, 입력 창등의 페이지 정보 | K | PageInfo |



**2) Extracting the Associations**

| Concept pair | Association Description | Association Name |
| ------------------ | ----------------------- | ---------------- |
| Controller  <->   UserModuleConnection | UserModuleConnection에서 임시 계정 정보를 받아온다. | convey data |
| Controller  <->   ViewPage | 임시 계정 정보를 ViewPage에 전달하여 띄운다. | provides data |
| InputOperator  <->  UserModuleConnection | 가입 거부 이유를 UserModuleConnection에 전달한다. | convey data |
| ViewPage <-> PageInfo | 수락, 거절 여부에 따라 Page를 보여준다.             | provides data |

**3) Extracting the Attributes**

| Concept | Attributes | Attribute Description |
| ------- | ---------- | --------------------- |
| UserModuleConnection | TempAccountInfo | 임시 계정 정보        |
| InputOperator | RejectInfo | 가입 거부 이유 |

