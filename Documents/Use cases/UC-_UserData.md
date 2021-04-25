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
| ←         | 1 | 어드민이 가입요청내역을 확인하고 승인,거부를 결정한다. |
| →         | 2 | 승인이되면 데이터베이스에 입력된 정보들을 저장한다.|
| →         | 3 | 승인된 계정은 각 actor에 따라 권환이 부여된다. |



