# Use Case UC-04 : AcceptUsers

## **Related Requirements**

REQ-3, REQ-5, REQ-6, REQ-31

## **Initiating Actors**

Any of: 어드민

## **Actor's Goal**

유저 모듈에 임시로 저장된 계정을 수락하여 회원으로 추가한다.

## **Participating Actors**

 - 유저 모듈

## **Preconditions**

+ 어드민 계정으로 로그인되어 있어야 한다.
+ 유저 모듈에 임시 계정 정보가 저장되어 있어야 한다.

## **Postconditions**

- 임시 계정 정보가 데이터 모듈에 저장된다.

## Flow of Events for Main Success Scenario
| Direction | n    | Actor Action                                      |
| --------- | ---- | ------------------------------------------------- |
| →         | 1    | 어드민이 회원가입 승인 항목을 클릭한다.           |
| ←         | 2    | 유저 모듈이 임시 계정 목록을 띄운다.              |
| →         | 3    | 어드민이 열람할 임시 계정을 클릭한다.             |
| ←         | 4    | 시스템이 어드민이 클릭한 임시 계정 정보를 띄운다. |
| →         | 5    | 어드민이 수락 버튼을 클릭한다.                    |
|           | 6    | include UserData (UC-15)                          |
| ←         | 7    | 시스템이 새로운 계정이 추가되었음을 알린다.       |


## Flow of Events for Extensions (Alternate Scenarios)
5a. 어드민이 거절 버튼을 클릭했을 경우

| Direction | n    | Actor Action                                          |
| --------- | ---- | ----------------------------------------------------- |
| ←         | 1    | 시스템이 어드민에게 거절 사유를 입력하는 창을 띄운다. |
| →         | 2    | 어드민이 거절 사유를 입력한다.                        |
| ←         | 3    | 시스템이 유저 모듈에게 거절 사유를 전달한다.          |


