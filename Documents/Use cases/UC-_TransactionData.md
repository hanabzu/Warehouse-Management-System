# Use Case: TransactionData

## **Related Requirements**

REQ-3, REQ-4, REQ-10 ,REQ-18, REQ-21

## **Initiating Actors**

Any of: 어드민 , 창고관리자, 점주

## **Actor's Goal**

트랜잭션 데이터를 저장한다.

## **Participating Actors**

 - 

## **Preconditions**

- 창고와 매장사이에 트랜잭션 내역이나 요청한 데이터가 존재하야한다. 

## **Postconditions**

- 

## Flow of Events for Main Success Scenario
| Direction | n | Actor Action                                                                                                         |
| --------- | - | -------------------------------------------------------------------------------------------------------------------- |
| ←         | 1 | 사용자가 '트랜잭션' 탭에 들어가면 관리(a),조회(b)를 고를 수 있는 화면이 나온다. |
| →         | 2 | 사용자가 원하는 동작을 선택한다. |



## Flow of Events for Extensions (Alternate Scenarios)
1a. 사용자가 '관리'탭에 들어간다.
| Direction | n | Actor Action                                                                                                         |
| --------- | - | -------------------------------------------------------------------------------------------------------------------- |
| ←         | 1 | 기본값으로는 상품명이 오름차순으로 정렬된 트랜잭션 내역이 출력된다. |
| →         | 2 | 점주는 자동발주를 활성화(a)/비활성화(b)로 선택 할 수 있다. |
| →         | 2a | 점주는 자동발주를 활성화한 경우 날짜를 입력해야 한다. |
| →         | 2b | 점주는 자동발주를 비활성화한 경우 수량을 입력하고 '요청'버튼을 눌러야 발주가 된다.|

1b. 사용자가 '조회'탭에 들어간다.
| Direction | n | Actor Action                                                                                                         |
| --------- | - | -------------------------------------------------------------------------------------------------------------------- |
| ←         | 1 | 기본값으로는 최신순으로 트랜잭션 내역이 출력이 된다. |
| →         | 2 | 사용자는 필터링 할 수 있는 구역에 특정제품, 특정기간, 특정창고/매장을 입력한다. |
| →         | 3 | 사용자는 정렬을 오름차순, 내림차순으로 선택할 수 있다. |
| ←         | 4 | 조건에 맞는 데이터가 화면에 출력된다.|



