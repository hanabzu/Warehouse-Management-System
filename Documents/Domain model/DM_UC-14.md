# Domain Model for UC-14 : TransactionData 

**1) Extracting the Responsibilities**

| Responsibility Description                                   | Type | Concept Name |
| ------------------------------------------------------------ | ---- | ------------ |
| UseCase, UseCase의 논리적 집합 혹은 전체 시스템과 관련된 작업을 조정하고 다른 concept에 위임한다.  | D    | Controller   |
| 데이터를 변경하기 위한 데이터베이스 쿼리를 준비한다  | D    | DatabaseConnection   |
| 요청된 데이터를 데이터베이스상에 저장한다.| D   | Archiver   |



**2) Extracting the Associations**

| Concept pair | Association Description | Association Name |
| ------------------ | ----------------------- | ---------------- |
| Controller  <->  DatabaseConnection  | Controller는 변경할 데이터를 DatabaseConnection에게 넘긴다.   | convey request |
| DatabaseConnection  <->  Archiver  | 입력된 데이터를 데이터베이스에 저장한다.   | request save |


**3) Extracting the Attributes**

| Concept | Attributes | Attribute Description |
| ------- | ---------- | --------------------- |
| Archiver | 제품명,브랜드| 변경될 데이터 |

