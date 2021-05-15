# Domain Model for UC-19: ViewTransaction

**1) Extracting the Responsibilities**

| Responsibility Description                                   | Type | Concept Name |
| ------------------------------------------------------------ | ---- | ------------ |
| 콘셉트간의 작업을 결합시키고, 필요한 작업을 다른 콘셉트에게 요청한다.  |  D  | Controller   |
| 사용자(어드민/점주/창고관리자)가 보고 싶은 Transaction data 정보 | K | TransactionInfo |
| 트랜잭션 데이터를 바탕으로 사용자에게 보여줄 화면을 만든다. | D | PageMaker |
| 사용자에게 보여 줄 만들어진 페이지 | K | TransactionPage | 
| 데이터베이스에서 해당하는 트랜잭션 데이터를 가져온다. | D | DatabaseConnection |


**2) Extracting the Associations**

| Concept pair | Association Description | Association Name |
| ------------------ | ----------------------- | ---------------- |
| TransactionInfo <-> Controller | 사용자가 보고싶어하는 트랜잭션 데이터에 대한 정보를 요청한다.    | request Data |
| Controller <-> DatabaseConnection | 해당하는 트랜잭션을 DB에서 가져올 것을 요구한다. | convey request |
| Controller <-> pageMaker | 가져온 트랜잭션 데이터를 바탕으로 출력할 페이지를 만들 것을 요구한다. | convey request |
| PageMaker <-> TransactionPage | 만들어진 페이지를 전달한다. | provide data(page) |

**3) Extracting the Attributes**

| Concept | Attributes | Attribute Description |
| ------- | ---------- | --------------------- |
| TransactionInfo  | Transaction pair  | 어디와 어디의 트랜잭션인지에 관한 정보. ( T1, T2 )     |
|         | TransactionPeriod | 보고 싶은 트랜잭션의 기간                      |
| DatabaseConnection  | 트랜잭션 데이터  |  사용자가 선택한 기간에 해당하는 트랜잭션 데이터    |
|         |            |                       |
|         |            |                       |
