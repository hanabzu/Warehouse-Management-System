## Use Case UC-20: ViewTrendsReport
**1) Related Requirements** : REQ-4, REQ-27, REQ-29, REQ-30

**2) Initiating Actors** : Any of: 어드민 , 창고관리자, 점주

**3) Actor's Goal** : 사용자는 시스템에서 제공해주는 판매 동향 리포트를 확인한다.

**4) Participating Actors** : 

**5) Preconditions** : 판매 동향리포트가 생성되기 위해 판매량 데이터가 존재해야한다.

**6) Postconditions** :  판매 동향 리포트를 화면에 출력한다.

**7) Flow of Events for Main Success Scenario**

| Direction | n    | Actor Action                                                 |
| --------- | ---- | ------------------------------------------------------------ |
| →         | 1    | 사용자는 판매 동향리포트를 선택한다.                         |
| →         | 2    | 사용자는 상품별/지역별/기간별 카테고리에서 보고 싶은 것을 선택한다. (어떤상품/어느지역/어느기간) |
| ←         | 3    | 시스템은 판매량 데이터를 기반으로 동향 리포트를 생성해서 화면에 출력한다. |
| ←         | 4    |                                                              |

