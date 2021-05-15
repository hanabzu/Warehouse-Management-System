## Use Case UC-07: ProductData
**1) Related Requirements** : REQ-1, REQ-16

**2) Initiating Actors** : Any of: 어드민

**3) Actor's Goal** : 상품에 대한 데이터를 저장한다.

**4) Participating Actors** : 데이터 모듈

**5) Preconditions** : 제품명,브랜드 대한 데이터는 필히 입력되어있어야한다.

​								  시스템에서 제품에 대한 정보를 입력/수정/삭제하는 화면이 출력되어야한다.

**6) Postconditions** :  데이터베이스에 상품에 대한 정보가 저장된다.

**7) Flow of Events for Main Success Scenario**

| Direction | n    | Actor Action                                                 |
| --------- | ---- | ------------------------------------------------------------ |
| →         | 1    | 상품에 대한 정보가 변경(추가, 수정, 삭제)요청이 들어온다.    |
| ←         | 2    | 해당 데이터베이스 테이블을 분석하여 변경가능한지 판단한다.(a) |
| ←         | 3    | 요청된 데이터들을 알맞은 테이블에 추가한다.                  |
| ←         | 4    | 데이터베이스에 변경된 정보가 저장여부의  시스템으로 보낸다.  |

**8) Flow of Events for Extensions (Alternate Scenarios)**

2a. 변경이 불가능하다고 판단되는 경우.

| Direction | n    | Actor Action                                                 |
| --------- | ---- | ------------------------------------------------------------ |
| ←         | 1    | 요청들어온 데이터의 Primary Key가 테이블에 존재하는지 확인한다. |
| ←         | 1a   | 추가를 할 경우 Primary Key가 존재하면 에러.                  |
| ←         | 1b   | 수정, 삭제를 할 경우 Primary Key가 존재하지 않으면 에러.     |