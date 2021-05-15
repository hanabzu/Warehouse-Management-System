## Use Case UC-02: Logout
**1) Related Requirements** : REQ-3, REQ-7, REQ-32

**2) Initiating Actors** : Any of: 어드민 , 창고관리자, 점주

**3) Actor's Goal** : 로그아웃을 눌러 어플리케이션에서 로그아웃한다.

**4) Participating Actors** : 유저 모듈

**5) Preconditions** : 시스템에 계정이 로그인되어 있어야 한다.

**6) Postconditions** :  유저는 사용 권한을 잃는다.

**7) Flow of Events for Main Success Scenario**
| Direction | n    | Actor Action                        |
| --------- | ---- | ----------------------------------- |
| →         | 1    | 유저가 로그아웃 버튼을 클릭한다.    |
|           | 2    | include UserData (UC-15)            |
| ←         | 3    | 시스템은 유저의 사용 권한을 없앤다. |
| ←         | 4    | 로그인 창으로 이동한다.             |


