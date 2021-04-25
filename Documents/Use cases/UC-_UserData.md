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
| →         | 1 | User Data에 변경요청이 들어온다. |
| →         | 2 | 해당 테이블에 요청 들어온 Data의 존재여부를 판단한다.|
| →         | 3 | 팓단이 끝나면 원하는 작업에 맞게 데이터를 추가한다. |

## Flow of Events for Extensions (Alternate Scenarios)
2a. 로그인을 하는 경우.
| Direction | n | Actor Action                                                                                                         |
| --------- | - | -------------------------------------------------------------------------------------------------------------------- |
| →         | 1 | 데이터가 이미 존재하는지 판단 |
| ←         | 1a | 존재하고 일치하면 로그인 성공 |
| ←         | 1b | 존재하지않거나, 일치하지 않으면 로그인 실패 |


