# Domain Model for UC-21: ViewPredictionReports

**1) Extraction the Responsibilities**

| Responsibility Description                                   | Type | Concept Name |
| ------------------------------------------------------------ | ---- | ------------ |
| 콘셉트간의 작업을 결합시키고, 필요한 작업을 다른 콘셉트에게 요청한다. | D | Controller   |
| 데이터 모듈에 저장되어 있는 판매 예측 데이터를 가져온다. | D | Database Connection |
| 판매 예측 데이터 | K | Prediction Data |
| 판매 예측 데이터를 판매 예측 리포트로 만든다. | D | Prediction Report Maker |
| 판매 예측 리포트 | K | Prediction Report |
| 판매 예측 리포트를 페이지로 만든다. | D | Page Maker              |
| 사용자에게 판매 예측 리포트를 보여줄 페이지. | K | Page Info  |

**2) Extracting the Associations**

| Concept pair | Association Description | Association Name |
| --------- | ----------------------- | ---------------- |
| Controller <-> Database Connection | 컨트롤러가 Database Connection에게 판매 예측 데이터를 가져올 것을 요청한다. | Convey Request |
| Controller <-> Page Maker | 컨트롤러가 Page Maker에게 판매 예측 리포트 페이지를 만들 것을 요청한다. | Convey Request |
| Database Connection <-> Prediction Report Maker | 판매 예측 데이터를 Prediction Report Maker에 넘겨준다. | Convey Data |
| Prediction Report Maker <-> Page Maker | 판매 예측 리포트를 Page Maker에 넘겨준다. | Convey Report |
| Page Maker <-> Page Info | 사용자에게 보여줄 페이지를 준비한다. | Prepare |

**3) Extracting the Attributes**

| Concept           | Attributes              | Attribute Description                  |
| ----------------- | ----------------------- | -------------------------------------- |
| Prediction Data   | 판매 예측 데이터        | 데이터모듈에서 가져온 판매 예측 데이터 |
| Prediction Report | 판매 예측 리포트        | 판매 예측 데이터로 만들어진 리포트     |
| Page Info         | 판매 예측 리포트 페이지 | 판매 예측 리포트로 만들어진 페이지     |