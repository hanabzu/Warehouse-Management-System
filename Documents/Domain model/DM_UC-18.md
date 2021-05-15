# Domain Model for UC-18: ViewBranches

**1) Extraction the Responsibilities**

| Responsibility Description                                   | Type | Concept Name |
| ------------------------------------------------------------ | ---- | ------------ |
| 콘셉트간의 작업을 결합시키고, 필요한 작업을 다른 콘셉트에게 요청한다. | D | Controller   |
| 열람할 창고 데이터. | K | Warehouse |
| 데이터 베이스로부터 브랜치 정보를 가져온다. | D | Database Connection |
| 사용자가 보고 싶어하는 브랜치를 페이지로 만든다. | D | Page Maker |
| 사용자에게 보여줄 브랜치 페이지. | K | Interface Page |

**2) Extracting the Associations**

| Concept pair | Association Description | Association Name |
| --------- | ----------------------- | ---------------- |
| Controller <-> Database Connection | 컨트롤러가 데이터베이스에서 사용자가 원하는 창고 브랜치 정보를 가져올 것을 요청한다. | Convey Request |
| Controller <-> Page Maker | 컨트롤러가 페이지 메이커에게 사용자가 원하는 창고의 브랜치 페이지를 만들 것을 요청한다. | Convey Request |
| Warehouse <-> Controller | 요청한 창고에 대한 값을 컨트롤러에 넘겨준다. | Convey Data |
| Database Connection <-> Page Maker | 창고 브랜치 데이터를 Page Maker에게 넘겨준다. | Provide Data |
| Page Maker <-> Interface Page | 사용자에게 보여줄 페이지를 준비한다. | Prepare |

**3) Extracting the Attributes**

| Concept   | Attributes | Attribute Description             |
| --------- | ---------- | --------------------------------- |
| Warehouse | 창고 정보  | 사용자가 요청한 창고의 Name or ID |
