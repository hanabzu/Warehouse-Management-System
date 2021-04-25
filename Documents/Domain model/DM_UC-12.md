# Domain Model for UC-12: SaleData

**1) Extracting the Responsibilities**

| Responsibility Description                                   | Type | Concept Name |
| ------------------------------------------------------------ | ---- | ------------ |
| 콘셉트간의 작업을 결합시키고, 필요한 작업을 다른 콘셉트에게 요청한다.  |  D  | Controller   |
| 점주가 판매 내역을 입력할 수 있게 한다 .       |  D  |  InputOperator  |
| 판매내역 데이터이다. |  K |   SalesData  |
| 점주에게 입력 받은 판매 내역을 데이터베이스에 저장한다.   |  D   |  SaveOperator  |


**2) Extracting the Associations**

| Concept pair | Association Description | Association Name |
| ------------------ | ----------------------- | ---------------- |
| Controller <-> InputOperator | 컨트롤러는 입력모듈이 판매 내역을 입력받을 수 있게 한다.   |  convey request |
| Controller <-> SaveOperator | 컨트롤러는 저장 모듈이 판매 내역을 저장하게 한다.  | convey request  |
| InputOperator <-> SaveOperator | 입력모듈은 저장 모듈에게 판매 내역을 제공한다.      | provides data     |
|  |  |        |
|   |    |      |  

**3) Extracting the Attributes**

| Concept | Attributes | Attribute Description |
| ------- | ---------- | --------------------- |
| SalesData  |  해당 지점의 판매 내역  |  판매량 예측을 위한 해당 지점의 판매 내역 데이터이다.    |

