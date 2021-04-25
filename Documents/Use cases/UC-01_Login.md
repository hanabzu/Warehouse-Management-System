# Use Case UC-01: Login

## **Related Requirements**

REQ-3, REQ-7, REQ-31, REQ-32

## **Initiating Actors**

Any of: 어드민, 창고관리자, 점주

## **Actor's Goal**

아이디, 패스워드를 입력하여 어플리케이션 사용 권한을 얻는다.

## **Participating Actors**

 - 유저 모듈

## **Preconditions**

- 로그인 하려는 계정 정보가 데이터베이스에 암호화되어 저장되어 있어야 한다.

## **Postconditions**

- 계정에 따른 어플리케이션 사용 권한을 얻는다.

## Flow of Events for Main Success Scenario
| Direction | n    | Actor Action                                                 |
| --------- | ---- | ------------------------------------------------------------ |
| ←         | 1    | 시스템은 유저가 아이디와 패스워드를 입력할 수 있는 로그인 창을 띄운다. |
| →         | 2    | 유저는 아이디와 패스워드를 입력한다.                         |
| →         | 3    | 유저는 로그인 버튼을 누른다.                                 |
| ←         | 4    | 시스템은 유저 모듈에 유저가 입력한 아이디와 패스워드를 전달한다. |
|           | 5    | include AuthenticateUser (UC-06)                             |
| →         | 6    | 유저 모듈이 계정 정보를 전달한다.                            |
| ←         | 7    | 유저에게 사용 권한을 부여한다.                               |


## Flow of Events for Extensions (Alternate Scenarios)
5a. 유저가 잘못된 아이디와 패스워드를 입력해 유저 모듈이 잘못된 계정이라고 알렸을 경우

| Direction | n    | Actor Action                                   |
| --------- | ---- | ---------------------------------------------- |
| ←         | 1    | 유저에게 잘못된 계정 정보임을 알린다.          |
| ←         | 2    | 유저에게 재입력을 요구하는 로그인 창을 띄운다. |
|           | 3    | Same as in Step 2 above                        |


