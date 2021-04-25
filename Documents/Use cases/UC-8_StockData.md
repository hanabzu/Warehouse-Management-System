# Use Case UC-8: StockData

## **Related Requirements**

REQ-2 ,REQ-3, REQ-11, REQ-12, REQ-22, REQ-33

## **Initiating Actors**

Any of: 어드민 , 창고관리자, 점주

## **Actor's Goal**

재고(상품수량)에 대한 데이터를 저장한다.

## **Participating Actors**

 - 

## **Preconditions**

- 제품이 존재해야만 한다.

## **Postconditions**

- 데이터베이스에 해당 상품에 대한 재고가 저장된다.

## Flow of Events for Main Success Scenario
| Direction | n | Actor Action                                                                                                         |
| --------- | - | -------------------------------------------------------------------------------------------------------------------- |
| →         | 1 | 재고에 대한 정보가 변경(추가, 수정, 삭제)요청이 들어온다. |
| ←         | 2 | 해당 데이터베이스 테이블을 분석하여 변경가능한지 판단한다.(a)|
| ←         | 3 | 요청된 데이터들을 알맞은 테이블에 추가한다.|
| ←         | 4 | 데이터베이스에 변경된 정보가 저장여부의 결과를 시스템으로 보낸다. |


## Flow of Events for Extensions (Alternate Scenarios)
2a. 변경이 불가능하다고 판단되는 경우.
| Direction | n | Actor Action                                                                                                         |
| --------- | - | -------------------------------------------------------------------------------------------------------------------- |
| ←         | 1 | 요청들어온 데이터의 Primary Key가 테이블에 존재하는지 확인한다. |
| ←         | 2 | Primary Key가 존재하지 않으면 에러. |


