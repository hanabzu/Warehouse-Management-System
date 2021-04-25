# Use Case UC-06: AuthenticateUser

## **Related Requirements**

REQ-3, REQ-7, REQ-8, REQ-31, REQ-32

## **Initiating Actors**

유저 모듈

## **Actor's Goal**

암호화되어 전달된 아이디, 패스워드가 데이터 모듈에 존재하는 것을 인증한다.

## **Participating Actors**

 - 데이터 모듈

## **Preconditions**

+ 계정 정보의 아이디, 비밀번호는 암호화되어 있어야 한다.

## **Postconditions**

## Flow of Events for Main Success Scenario
| Direction | n    | Actor Action                                                 |
| --------- | ---- | ------------------------------------------------------------ |
| →         | 1    | 유저 모듈이 암호화된 아이디, 패스워드를 전달한다.            |
| ←         | 2    | 데이터 모듈에서 암호화된 아이디 계정을 찾아 계정 정보를 불러온다. |
| ←         | 3    | 암호화된 패스워드가 같다면 인증을 확인한다.                  |
|           | 4    | include UserData (UC-15)                                     |

## Flow of Events for Extensions (Alternate Scenarios)
2a. 암호화된 아이디와 같은 계정이 없을 경우

| Direction | n | Actor Action                                                                                                         |
| --------- | - | -------------------------------------------------------------------------------------------------------------------- |
| ←        | 1 | 인증을 거부한다. |

3a. 암호화된 아이디와 같은 계정은 있으나 비밀번호가 틀렸을 경우

| Direction | n    | Actor Action             |
| --------- | ---- | ------------------------ |
| ←         | 1    | 인증을 거부한다.         |
|           | 2    | include UserData (UC-15) |

