## Use Case UC-03: Register
**1) Related Requirements** : REQ-6, REQ-31

**2) Initiating Actors** : Any of: 창고관리자, 점주

**3) Actor's Goal** : 계정 정보를 입력하여 회원 가입을 신청한다.

**4) Participating Actors** : 유저 모듈

**5) Preconditions** : 

**6) Postconditions** :  입력한 계정 정보가 암호화되어 유저 모듈에 임시저장된다.

**7) Flow of Events for Main Success Scenario**

| Direction | n    | Actor Action                                                 |
| --------- | ---- | ------------------------------------------------------------ |
| →         | 1    | 유저가 회원가입 버튼을 클릭한다.                             |
| ←         | 2    | 시스템은 유저가 계정 정보를 입력할 수 있는 창을 띄운다       |
| →         | 3    | 유저가 계정 정보를 입력한다.                                 |
| ←         | 4    | 시스템은 유저 모듈에 유저가 입력한 계정 정보를 전달한다.     |
|           | 5    | include AuthenticateUser (UC-06)                             |
| →         | 6    | 유저 모듈은 계정 정보가 중복된 계정이 아님을 시스템에게 알린다. |
| ←         | 7    | 시스템은 유저에게 어드민의 승인을 기다리라는 메세지를 띄운다. |

**8) Flow of Events for Extensions (Alternate Scenarios)**

5a. 유저 모듈이 계정 정보가 중복된 계정이라고 알렸을 경우

| Direction | n    | Actor Action                                             |
| --------- | ---- | -------------------------------------------------------- |
| ←         | 1    | 유저에게 중복된 계정 정보의 수정을 요구하는 창을 띄운다. |
| →         | 2    | 유저가 계정 정보를 재입력한다.                           |
|           | 3    | Same as in Step 4 above                                  |

