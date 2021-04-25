## Use Case UC-15: UserData
**1) Related Requirements** : REQ-3 ,REQ-5,REQ-6, REQ-7, REQ-8, REQ-31 REQ-32

**2) Initiating Actors** : 유저 모듈

**3) Actor's Goal** : 계정 정보를 저장, 수정한다.

**4) Participating Actors** : 데이터 모듈

**5) Preconditions** : 계정 정보의 아이디, 비밀번호는 암호화되어 있어야 한다.

**6) Postconditions** : 

**7) Flow of Events for Main Success Scenario**
| Direction | n    | Actor Action                                                 |
| --------- | ---- | ------------------------------------------------------------ |
| →         | 1    | 유저 모듈이 저장하려는 암호화된 계정 정보를 전달한다.        |
| ←         | 2    | 데이터 모듈에 암호화된 아이디와 같은 계정을 찾아 계정 정보를 저장한다. |

**8) Flow of Events for Extensions (Alternate Scenarios)**

2a. 암호화된 아이디와 같은 계정이 없을 경우

| Direction | n    | Actor Action                               |
| --------- | ---- | ------------------------------------------ |
| ←         | 1    | 데이터 모듈에 새로운 계정 정보를 저장한다. |