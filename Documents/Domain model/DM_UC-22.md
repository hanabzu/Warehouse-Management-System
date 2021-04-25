# Domain Model for UC-22: WriteAIReport

**1) Extracting the Responsibilities**

| Responsibility Description                                   | Type | Concept Name |
| ------------------------------------------------------------ | ---- | ------------ |
| 데이터 모듈로부터 전체 판매 내역 데이터를 가져와 예측 모델을 만들고, 점주가 판매 내역을 입력하면 그 데이터를 가지고 예측을 한다. |  D   | Controller      |
| 판매량 예측 모델을 만들기 위해 수집된 데이터이다.                       |  K   | AllSalesData   |
| 데이터를 활용해 판매량을 예측한다.                                                             |  D    |   AnalysisOperator             |
| 데이터 베이스에 존재하는 판매 내역을 가져온다.                                 |  D    |   Database Connection          |
| 판매량 예측값을 얻기 위해 점주가 입력한 판매 내역이다.                |  K   | SalesInputData| 


**2) Extracting the Associations**

| Concept pair | Association Description | Association Name |
| ------------------ | ----------------------- | ---------------- |
| Controller <-> AnalysisOperator     | 컨트롤러는 분석 모듈이 예측모델을 만들고 예측을 하도록 한다.  |  conveys request  |
| Controller <->    Database Connection   | 컨트롤러는 데이터 모듈이 분석 모듈에게 모델을 만들기 위한 데이터를 전달하도록 한다.  | conveys request  |
| AnalysisOperator <->   AllSalesdata | 분석모듈은 전체 판매 내역 데이터를 활용해 판매량 예측 모델을 만든다.      |    provides data     |
| AnalysisOperator  <-> SalesInputData     |   점주가 입력한 판매 내역 데이터를 활용해 해당 지점의 판매량을 예측한다.        |     provides data           |



**3) Extracting the Attributes**

| Concept | Attributes | Attribute Description |
| ------- | ---------- | --------------------- |
|   AllSalesData       |  전체 판매 내역 데이터          |   예측 모델을 만들기 위해 수집한                     |
|  SalesInputData       |  해당 지점 판매 내역 데이터          | 점주가 예측을 위해 넣은 데이터                      |

