# Domain Model for UC-10: StorekeeperOrder

## Extracting the Responsibilities

| Responsibility Description                                   | Type | Concept Name |
| ------------------------------------------------------------ | ---- | ------------ |
| 콘셉트간의 작업을 결합시키고, 필요한 작업을 다른 콘셉트에게 요청한다.  |  D  | Controller   |
| 예측과 창고 재고를 바탕으로 자동으로 발주 데이터를 생성한다.        |  D  | OrderMaker    |
| 생성된 상품 발주 목록  | K  | OrderList    |
| 창고관리자가 신청한 자동 발주 날짜   | D    | OrderDate   |
| 날짜를 세어서 자동 발주 날짜 n일 전 임을 알려준다.       | D   | DateCounter   |
| 창고 관리자의 발주 목록 수정을 반영한다.  | D | OrderEditer |


## Extracting the Associations

| Concept pair | Association Description | Association Name |
| ------------------ | ----------------------- | ---------------- |
|  |     |   |
|   |   |   |
|   |       |      |
|  |  |        |
|   |    |      |  

## Extracting the Attributes

| Concept | Attributes | Attribute Description |
| ------- | ---------- | --------------------- |
|   |    |      |
|   | |                       |
|         |            |                       |
|         |            |                       |
|         |            |                       |
