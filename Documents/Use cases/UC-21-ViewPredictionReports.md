## Use Case UC-21: ViewPredictionReports
**1) Related Requirements** : REQ-4, REQ-28, REQ-29, REQ-30

**2) Initiating Actors** : Any of: 창고관리자, 점주

**3) Actor's Goal** : 근처 창고의 차후 재고 예측 리포트 확인, 창고의 재고 예측 리포트 확인

**4) Participating Actors** : 데이터 모듈

**5) Preconditions** : 판매 예측 리포트가 생성되기 위해 판매 예측 데이터가 존재해야한다.

**6) Postconditions** :  판매 예측 리포트를 화면에 출력한다.

**7) Flow of Events for Main Success Scenario**

| Direction | n    | Actor Action                                                 |
| --------- | ---- | ------------------------------------------------------------ |
|           | 1    | include WriteReport(UC-#)                                    |
| →         | 2    | 사용자는 판매 예측 리포트를 선택한다.                        |
| ←         | 3    | 데이터 모듈의 판매 예측 데이터로 판매 예측 리포트를 생성한다. |
| ←         | 4    | 생성된 판매 예측 리포트를 화면에 출력한다.                   |
