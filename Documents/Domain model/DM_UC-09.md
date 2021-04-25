# Domain Model for UC-09: ShopkeeperOrder

## Extracting the Responsibilities

| Responsibility Description                                   | Type | Concept Name |
| ------------------------------------------------------------ | ---- | ------------ |
| 콘셉트간의 작업을 결합시키고, 필요한 작업을 다른 콘셉트에게 요청한다.  |  D  | Controller   |
| 점주가 신청한 발주 신청 목록        | K   | 발주신청목록    |
| 발주 신청목록을 창고관리자에게 전송한다.  | D  | 전송모듈     |
| 발주 신청목록을 보고 결재여부 판단   |  D   | 승인모듈   |
| 사용자 계정의 돈을 발주 목록에 따라 계산한다.                   | D  | 돈 관리 |
| 발주 목록에 따라 재고 데이터를 변경한다.                        | D    | 데이터베이스 모듈  |
|                                                              |      |              |
|                                                              |      |              |
|                                                              |      |              |

## Extracting the Associations

| Concept pair | Association Description | Association Name |
| ------------------ | ----------------------- | ---------------- |
|  |      |  |
|    |    |  |
|    |       |     |
|    |   |       |
|   |             |                  |
|            |      |           |                         |                  |
|            |      |           |                         |                  |
|            |      |           |                         |                  |
|            |      |           |                         |                  |
|            |      |           |                         |                  |
|            |      |           |                         |                  |

## Extracting the Attributes

| Concept | Attributes | Attribute Description |
| ------- | ---------- | --------------------- |
|   |   |             |
|   | |                       |
|         |            |                       |
|         |            |                       |
|         |            |                       |
