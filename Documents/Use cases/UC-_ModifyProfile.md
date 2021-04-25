# Use Case: ModifyProfile

## **Related Requirements**

REQ-8

## **Initiating Actors**

Any of: 어드민 , 창고관리자, 점주

## **Actor's Goal**

계정 정보를 수정한다.

## **Participating Actors**

 - 유저 모듈

## **Preconditions**

- 어플리케이션에 로그인된 상태이다.

## **Postconditions**

+ 계정 정보가 변경된다.

## Flow of Events for Main Success Scenario
| Direction | n    | Actor Action                                                 |
| --------- | ---- | ------------------------------------------------------------ |
| →         | 1    | 유저가 계정정보 수정 버튼을 클릭한다.                        |
| ←         | 2    | 시스템이 패스워드 재입력을 요청한다.                         |
| →         | 3    | 유저가 패스워드를 입력한다.                                  |
| ←         | 4    | 시스템은 유저 모듈에 계정의 아이디와 유저가 입력한 패스워드를 전달한다. |
|           | 5    | include AuthenticateUser                                     |
| ←         | 6    | 시스템이 유저에게 계정 정보를 수정할 수 있는 창을 띄운다.    |
| →         | 7    | 유저가 계정 정보를 수정한다.                                 |
| ←         | 8    | 시스템이 새로운 계정 정보를 유저 모듈에 전달한다.            |
| →         | 9    | 유저 모듈이 유효한 계정 정보임을 시스템에게 알린다.          |
| ←         | 10   | 시스템이 유저에게 계정 정보가 변경되었음을 알린다.           |

## Flow of Events for Extensions (Alternate Scenarios)
5a. 유저 모듈이 패스워드가 잘못되었음을 알렸을 경우

| Direction | n    | Actor Action                                       |
| --------- | ---- | -------------------------------------------------- |
| ←         | 1    | 유저에게 패스워드의 재입력을 요구하는 창을 띄운다. |
| →         | 2    | 유저가 패스워드를 재입력한다.                      |
|           | 3    | Same as in Step 4 above                            |

9a. 유저 모듈이 새로운 계정 정보가 유효하지 않음을 알렸을 경우 

| Direction | n    | Actor Action                                             |
| --------- | ---- | -------------------------------------------------------- |
| ←         | 1    | 유저에게 새로운 계정 정보의 수정을 요구하는 창을 띄운다. |
| →         | 2    | 유저가 계정 정보를 재입력한다.                           |
|           | 3    | Same as in Step 8 above                                  |
