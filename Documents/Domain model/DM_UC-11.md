# ㄴDomain Model for UC-11: Request

**1) Extraction the Responsibilities**

| Responsibility Description                                   | Type | Concept Name |
| ------------------------------------------------------------ | ---- | ------------ |
| 콘셉트간의 작업을 결합시키고, 필요한 작업을 다른 콘셉트에게 요청한다. | D | Controller   |
| 데이터 베이스에 존재하는 컴플레인 목록을 가져온다. | D | Database Connection |
| 창고관리자가 승인한 컴플레인을 어드민에게 전달하고 거부한 컴플레인을 삭제한다. | D | Process Complaint |
| 점주가 컴플레인을 신청한다. | D | Request Complaint |
| 점주가 신청한 컴플레인을 데이터 베이스에 추가한다. | D | Add Complaints |
| 변동된 컴플레인을 페이지로 만든다. | D | Page Maker |
| 사용자에게 변동된 컴플레인을 보여줄 페이지. | K | Interface Page |

**2) Extracting the Associations**

| Concept pair | Association Description | Association Name |
| --------- | ----------------------- | ---------------- |
| Controller <-> Database Connection | 컨트롤러가 데이터 베이스에서 컴플레인 목록을 가져올 것을 요청한다. | Convey Request |
| Controller <-> Process Complaint | 컨트롤러가 창고 관리자에게 컴플레인 처리를 요청한다. | Convey Request |
| Controller <-> Request Complaint | 컨트롤러가 점주에게 컴플레인 추가를 요청한다. | Convey Request |
| Controller <-> Page Maker | 컨트롤러가 변동된 컴플레인 페이지를 만들 것을 요청한다. | Convey Request |
| Database Connection <-> Process Complaint | 데이터 베이스에서 가져온 목록을 넘겨준다. | Convey Data |
| Request Complaint <-> Add Complaints | 점주가 신청한 컴플레인을 넘겨준다. | Convey Complaint |
| Process Complaint  <-> Page Maker | 처리된 컴플레인을 페이지 메이커에 넘겨준다. | Convey Complaint |
| Request Complaint <-> Page Maker | 신청한 컴플레인을 페이지 메이커에 넘겨준다. | Convey Complaint |
| Page Maker <-> Interface Page | 사용자에게 보여줄 페이지를 준비한다. | Prepare |

**3) Extracting the Attributes**

| Concept | Attributes | Attribute Description |
| ------- | ---------- | --------------------- |
| Interface Page | 변동된 컴플레인 데이터 페이지 | 창고관리자/점주가 수정한 컴플레인 페이지 |
