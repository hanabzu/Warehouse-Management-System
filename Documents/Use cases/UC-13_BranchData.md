# Use Case UC-13: BranchData

## **Related Requirements**

REQ-23, REQ-24

## **Initiating Actors**

Any of: 창고관리자

## **Actor's Goal**

창고와 연결된 소매점 데이터 저장.

## **Participating Actors**

 - 

## **Preconditions**

- 시스템에 창고와 연결된 매장의 정보가 저장되어 있어야한다.

## **Postconditions**

- 데이터베이스에 매장에 대한 정보가 저장된다.

## Flow of Events for Main Success Scenario
| Direction | n | Actor Action                                                                                                         |
| --------- | - | -------------------------------------------------------------------------------------------------------------------- |
| →         | 1 | 에 대한 정보가 변경(추가, 수정, 삭제)요청이 들어온다. |
| ←         | 2 | 해당 데이터베이스 테이블을 분석하여 변경가능한지 판단한다.(a)|
| ←         | 3 | 요청된 데이터들을 알맞은 테이블에 추가한다.|
| ←         | 4 | 데이터베이스에 변경된 정보가 저장되었는지에 대한 쿼리를 시스템으로 보낸다. |


## Flow of Events for Extensions (Alternate Scenarios)
2a. 변경이 불가능하다고 판단되는 경우.
| Direction | n | Actor Action                                                                                                         |
| --------- | - | -------------------------------------------------------------------------------------------------------------------- |
| ←         | 1 | 요청들어온 데이터의 Primary Key가 테이블에 존재하는지 확인한다. |
| ←         | 1a | 추가를 할 경우 Primary Key가 존재하면 에러. |
| ←         | 1b | 수정, 삭제를 할 경우 Primary Key가 존재하지 않으면 에러. |
