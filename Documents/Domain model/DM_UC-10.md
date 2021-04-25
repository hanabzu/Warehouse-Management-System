# Domain Model for UC-10: StorekeeperOrder

**1) Extracting the Responsibilities**

| Responsibility Description                                   | Type | Concept Name |
| ------------------------------------------------------------ | ---- | ------------ |
| 콘셉트간의 작업을 결합시키고, 필요한 작업을 다른 콘셉트에게 요청한다.  |  D  | Controller   |
| 예측과 창고 재고를 바탕으로 자동으로 발주 데이터를 생성한다.        |  D  | OrderMaker    |
| 생성된 상품 발주 목록  | K  | OrderList    |
| 창고관리자가 신청한 자동 발주 날짜   | K    | OrderDate   |
| 날짜를 세어서 자동 발주 날짜 n일 전 임을 알려준다.       | D   | DateCounter   |
| 창고 관리자의 발주 목록 수정을 반영한다.  | D | OrderEditer |
| 발주 목록에 맞추어 재고 데이터 변경 및 창고 관리자 보유금액을 변경한다. | D | DatabaseConnection |



**2) Extracting the Associations**

| Concept pair | Association Description | Association Name |
| ------------------ | ----------------------- | ---------------- |
| Controller <-> OrderMaker  | 발주 날짜 기준으로 자동으로 상품 발주 목록을 만들 것을 요청한다.    | convey Request  |
| Controller <-> OrderEditer  | 창고관리자에게 발주목록에 대한 수정을 받을 것을 요청한다.  | convey Request  |
| Controller <-> DateCounter  | 발주 날짜 기준으로 n일 전에 창고관리자에게 발주 목록을 보여줄 것을 요청한다.     | convey Request   |
| Controller <-> DatabaseConnection  | 발주가 되면 데이터 변경을 하도록 요청한다. | convey Request     |
| OrderMaker <-> OrderList | 발주 목록을 생성하여 상품 발주 목록 데이터를 만든다. | create | 
| OrderEdit <-> OrderList  | 수정한 발주 목록을 상품 발주 목록에 반영한다.   | Update     |  
| OrderDate <-> DateCouner | 창고 관리자가 신청한 발주 날짜를 전달한다. | convey data |

**3) Extracting the Attributes**

| Concept | Attributes | Attribute Description |
| ------- | ---------- | --------------------- |
| DatabaseConnection  | 재고 데이터   | 창고의 재고 데이터     |
|                     | 보유 금액  | 창고 관리자의 계정에 보유하고 있는 금액     |
| DateCounter    | 설정 일수   | 발주 날짜 몇 일 전에 알려주는 지에 관한 데이터. (n)   |
| OrderList    | 상품 종류  | 발주하는 상품의 이름                    |
|              | 개수      | 발주하는 상품의 개수                    |
|              | 가격      | 발주하는 상품의 가격        |
