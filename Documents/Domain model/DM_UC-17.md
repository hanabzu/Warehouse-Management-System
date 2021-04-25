# Domain Model for UC-17 : ViewStock

**1) Extracting the Responsibilities**

| Responsibility Description                                   | Type | Concept Name |
| ------------------------------------------------------------ | ---- | ------------ |
| Use case에 관련된 모든 콘센트 작업을 조정하고 작업을 다른 콘셉트에게 위임한다. | D    | Controller   |
| 사용자가 보고 싶어하는 재고 데이터를 페이지로 만든다.        | D    | PageMaker    |
| 데이터 베이스에 존재하는 재고 데이터에서 사용자가 원하는 데이터를 가져온다.  | D   | Database Connection    |
| 사용자의 입력을 받아 어떤 창고/지점을 선택했는지에 대한 값   | K    | UserEntry    |
| 사용자에게 보여줄 재고 데이터 페이지.                           | K    | InterfacePage |


**2) Extracting the Associations**

| Concept pair | Association Description | Association Name |
| ------------------ | ----------------------- | ---------------- |
| Controller  <->   PageMaker | 컨트롤러가 페이지 메이커에게 사용자가 원하는 재고 데이터 페이지를 만들 것을 요청한다.      | convey request |
| Controller  <->   DatabaseConnection  | 데이터베이스에서 사용자가 원하는 창고/지점의 재고 데이터를 가져올 것을 요청한다.   | convey request |
| UserEntry  <->  Controller | 사용자가 선택한 창고/지점에 대한 값을 컨트롤러에 넘겨준다.       |   request data  |
| PageMaker   <->   InterfacePage | 사용자에게 보여 줄 페이지를 준비한다.              |  Prepare                |


**3) Extracting the Attributes**

| Concept | Attributes | Attribute Description |
| ------- | ---------- | --------------------- |
| UserEntry  | search parameter | 사용자가 선택한 창고/지점의 Name or id        |
| DatabaseConnection  | 재고 데이터 | 사용자가 선택한 창고/지점의 현재 재고 데이터      |
|         |            |                       |
|         |            |                       |
|         |            |                       |
