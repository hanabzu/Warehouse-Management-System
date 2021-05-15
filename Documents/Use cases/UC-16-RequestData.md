## Use Case UC-16: RequestData
**1) Related Requirements** : REQ-9

**2) Initiating Actors** : Any of: 창고관리자, 점주

**3) Actor's Goal** : 컴플레인이나 요구 관련 정보를 저장한다.

**4) Participating Actors** : 

**5) Preconditions** : 창고관리자, 점주가 시스템/상품에대해 의견을 내야한다. 

**6) Postconditions** : 데이터베이스에 리퀘스트에 대한 정보가 저장된다.

**7) Flow of Events for Main Success Scenario**
| Direction | n    | Actor Action                                               |
| --------- | ---- | ---------------------------------------------------------- |
| →         | 1    | 창고관리자,점주가 입력한 데이터는 데이터베이스에 저장된다. |
| ←         | 2    | 저장된 데이터는 권한을 갖는 계정만 접근이 가능하다.        |
