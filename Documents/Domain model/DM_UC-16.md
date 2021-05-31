# Domain Model for UC-16: RequestData

**1) Extracting the Responsibilities**

| Responsibility Description                                   | Type | Concept Name |
| ------------------------------------------------------------ | ---- | ------------ |
| 콘셉트간의 작업을 결합시키고, 필요한 작업을 다른 콘셉트에게 요청한다.  |  D  | Controller   |
| 창고관리자, 점주가 컴플레인을 남길 수 있게 한다 .       |  D  |  InputOperator  |
| 컴플레인 정보이다. |  K |  ComplainData  |
| 점주에게 입력 받은 판매 내역을 데이터베이스에 저장한다.   |  D   |  Database Connection  |


**2) Extracting the Associations**

| Concept pair | Association Description | Association Name |
| ------------------ | ----------------------- | ---------------- |
| Controller <-> InputOperator | 컨트롤러는 입력 모듈이 컴플레인을 입력할 수 있게 한다.   |  conveys request |
| Controller <-> Database connection | 컨트롤러는 저장 모듈이 컴플레인을 저장하게 한다.  | conveys request  |
| InputOperator <-> Database connection | 입력모듈은 저장 모듈에게 컴플레인을 제공한다.      | provides data     |


**3) Extracting the Attributes**

| Concept | Attributes | Attribute Description |
| ------- | ---------- | --------------------- |
| ComplainData |  컴플레인 데이터  |  창고관리자, 점주로부터 입력 받은 컴플레인 데이터이다.   |

