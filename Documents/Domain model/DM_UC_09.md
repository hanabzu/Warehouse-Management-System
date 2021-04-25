# Domain Model for UC-09: ShopkeeperOrder

## Extracting the Responsibilities

| Responsibility Description                                   | Type | Concept Name |
| ------------------------------------------------------------ | ---- | ------------ |
| 콘셉트간의 작업을 결합시키고, 필요한 작업을 다른 콘셉트에게 요청한다.  |  D  | Controller   |
| 점주가 신청한 발주 신청 목록        | K   | 발주신청목록    |
| 발주 신청목록을 창고관리자에게 전송한다.  | D  | 전송모듈     |
| 발주 신청목록을 보고 결재여부 판단   |  D   | 승인모듈   |
| 발주 목록에 따라 재고 데이터와 사용자 계정의 보유 금액을 변경한다.        | D    | 데이터베이스 모듈  |

## Extracting the Associations

| Concept pair | Association Description | Association Name |
| ------------------ | ----------------------- | ---------------- |
| 발주신청목록 <-> Controller | 발주 신청목록을 넘겨준다.     | 데이터 전달 |
| Controller <-> 전송모듈   | 전송모듈이 발주 신청목록을 창고관리자에게 전송할 것을 요청한다.   | 요청 전달 |
| Controoler <-> 승인모듈   | 승인모듈이 발주 신청목록을 확인하고 결재 선택을 요청한다.      | 요청 전달    |
| 승인모듈 <-> 데이터베이스 모듈  | 승인모듈이 승인여부를 돈 관리 모듈에 보낸다  | 데이터 전달      |
| Controller <-> 데이터베이스 모듈  | 발주 승인 된 상품들을 창고 재고 데이터 변경할 것을 요청한다. (상태변경) 또한 사용자 계정의 보유 금액을 변경한다.   |   요청 전달  |  

## Extracting the Attributes

| Concept | Attributes | Attribute Description |
| ------- | ---------- | --------------------- |
| 승인모듈  | 승인 여부  | 발주에 대한 승인을 T/F   |
|   | |                       |
|         |            |                       |
|         |            |                       |
|         |            |                       |
