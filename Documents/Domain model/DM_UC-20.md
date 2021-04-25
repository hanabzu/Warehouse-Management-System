# Domain Model for UC-20: ViewTrendsReport

**1) Extraction the Responsibilities**

| Responsibility Description                                   | Type | Concept Name |
| ------------------------------------------------------------ | ---- | ------------ |
| 콘셉트간의 작업을 결합시키고, 필요한 작업을 다른 콘셉트에게 요청한다. | D | Controller   |
| 데이터 모듈에 저장되어 있는 판매 동향 데이터를 가져온다. | D | Database Connection |
| 판매 동향 데이터 | K | Trends Data |
| 사용자가 선택한 카테고리 | K | Category |
| 카테고리에 따른 판매 동향 데이터를 판매 동향 리포트로 만든다. | D | Trends Report Maker |
| 판매 동향 리포트 | K | Trends Report |
| 판매 동향 리포트를 페이지로 만든다. | D | Page Maker              |
| 사용자에게 판매 동향 리포트를 보여줄 페이지. | K | Interface Page          |

**2) Extracting the Associations**

| Concept pair | Association Description | Association Name |
| --------- | ----------------------- | ---------------- |
| Controller <-> Database Connection | 컨트롤러가 Database Connection에게 판매 동향 데이터를 가져올 것을 요청한다. | Convey Request |
| Trends Data <-> Trends Report Maker | 판매 동향 데이터를 Trends Report Maker에 넘겨준다. | Convey Data |
| Category <-> Trends Report Maker | 사용자가 선택한 카테고리를 Trends Report Maker에 넘겨준다. | Convey Data |
| Trends Report <-> Page Maker | 판매 동향 리포트를 Page Maker에 넘겨준다. | Convey Report |
| Page Maker <-> Interface Page | 사용자에게 보여줄 페이지를 준비한다. | Prepare |

**3) Extracting the Attributes**

| Concept        | Attributes               | Attribute Description                         |
| -------------- | ------------------------ | --------------------------------------------- |
| Trends Data    | 판매 동향 데이터         | 데이터모듈에서 가져온 판매 동향 데이터        |
| Category       | 사용자가 선택한 카테고리 | 상품별/지역별/기간별 중 하나                  |
| Trends Report  | 판매 동향 리포트         | 판매 동향 데이터와 카테고리로 만들어진 리포트 |
| Interface Page | 판매 동향 리포트 페이지  | 판매 동향 리포트로 만들어진 페이지            |
