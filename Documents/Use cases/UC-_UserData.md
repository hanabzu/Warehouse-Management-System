# Use Case: UserData

## **Related Requirements**

REQ-3 ,REQ-5, REQ-7, REQ-8

## **Initiating Actors**

Any of: 어드민 , 창고관리자, 점주

## **Actor's Goal**

사용자에 대해 입력된 정보(ID,PWD 등) 를 저장한다.

## **Participating Actors**

 - 

## **Preconditions**

- 어드민에게 가입요청 내역이 있어야한다.
- ID,PWD가 데이터베이스에 저장되어 있어야한다.

## **Postconditions**

- 

## Flow of Events for Main Success Scenario
| Direction | n | Actor Action                                                                                                         |
| --------- | - | -------------------------------------------------------------------------------------------------------------------- |
| ←         | 1 |  |
| →         | 2 | |
| →         | 3 | |
| →         | 4 |  |
| ←         | 5 |  |


## Flow of Events for Extensions (Alternate Scenarios)
3a. 추가 할 상품에 대한 정보를 입력칸에 입력한다.
| Direction | n | Actor Action                                                                                                         |
| --------- | - | -------------------------------------------------------------------------------------------------------------------- |
| ←         | 1 | 제품명,브랜드,수량에 대한 데이터가 입력되지 않은채 저장을 누르면 에러메세지를 출력한다. |


