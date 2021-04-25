# Domain Model for UC-13 : BranchData 

**1) Extracting the Responsibilities**

| Responsibility Description                                   | Type | Concept Name |
| ------------------------------------------------------------ | ---- | ------------ |
| UseCase, UseCase의 논리적 집합 혹은 전체 시스템과 관련된 작업을 조정하고 다른 concept에 위임한다.  | D    | Controller   |
| 상품에 대한 정보가 변경(추가,수정,삭제) 될 수 있는지 판단한다.        | K    | Judging    |
| 데이터를 변경하기 위한 데이터베이스 쿼리를 준비한다  | D    | DatabaseConnection   |
| 요청된 데이터를 데이터베이스상에 저장한다.| D   | Archiver   |



**2) Extracting the Associations**

| Concept pair | Association Description | Association Name |
| ------------------ | ----------------------- | ---------------- |
| Controller  <->   Judging | Controller는 입력된 데이터에대해 작업을 해도 되는지 판단하도록 한다.    | convey request |
| Controller  <->  DatabaseConnection  | Controller는 변경할 데이터를 DatabaseConnection에게 넘긴다.   | convey request |
| Judging <-> Archiver | 판단이되면 Archiver에게 데이터를 저장여부를 전달한다.       |  convey request   |
| DatabaseConnection  <->  Archiver  | 입력된 데이터를 데이터베이스에 저장한다.   | request save |


**3) Extracting the Attributes**

| Concept | Attributes | Attribute Description |
| ------- | ---------- | --------------------- |
| Judging  | 변경가능여부 | 데이터를 변경해도 되는지 안되는지에 대한 정보 |
| Archiver | 매장명, 위치 | 변경될 데이터 |

