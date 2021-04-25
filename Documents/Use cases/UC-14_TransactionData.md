# Use Case UC-14: TransactionData

## **Related Requirements**

REQ-3, REQ-10 ,REQ-18, REQ-19, REQ-21

## **Initiating Actors**

Any of: 어드민 , 창고관리자, 점주

## **Actor's Goal**

트랜잭션 데이터를 저장한다.

## **Participating Actors**

 - 

## **Preconditions**

- 창고와 매장사이에 트랜잭션 내역이나 요청한 데이터가 존재하야한다. 

## **Postconditions**

- 데이터베이스에 트랜잭션에 대한 데이터가 저장된다.

## Flow of Events for Main Success Scenario
| Direction | n | Actor Action                                                                                                         |
| --------- | - | -------------------------------------------------------------------------------------------------------------------- |
| →         | 1 | 트랜잭션 데이터가 추가될 때 마다 데이터베이스상 트랜잭션 데이터를 저장하는 테이블에 저장된다. |

## Flow of Events for Extensions (Alternate Scenarios)
2a. 이후 시스템에서 데이터 조회를 요청한 경우
| Direction | n | Actor Action                                                                                                         |
| --------- | - | -------------------------------------------------------------------------------------------------------------------- |
| ←         | 1 | 트랜잭션에 대한 데이터를 조회하고자 하는 요청이 들어오면 조건에 맞는 데이터를 골라 시스템으로 보낸다.|




