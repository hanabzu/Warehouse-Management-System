# Domain Model for UC-11: Request

**1) Extraction the Responsibilities**

| Responsibility Description                                   | Type | Concept Name |
| ------------------------------------------------------------ | ---- | ------------ |
| 콘셉트간의 작업을 결합시키고, 필요한 작업을 다른 콘셉트에게 요청한다. | D | Controller   |
| 데이터 베이스에 존재하는 컴플레인 목록을 가져온다. | D | Complaint List |
| 창고관리자가 승인/거부한 컴플레인. | K | Processed Complaints |
| 창고관리자가 승인한 컴플레인을 어드민에게 전달하고 상태를 바꾼다. | D | Approve Complaint |
| 창고관리자가 거부한 컴플레인을 삭제한다. | D | Reject Complaint |
| 점주가 신청한 요청 및 컴플레인. | K | Requested Complaints |
| 점주가 신청한 요청 및 컴플레인을 데이터 베이스에 추가한다. | D | Add Complaint |
| 변동된 컴플레인을 페이지로 만든다. | D | Page Maker |
| 사용자에게 변동된 컴플레인을 보여줄 페이지. | K | Interface Page |

**2) Extracting the Associations**

| Concept pair | Association Description | Association Name |
| --------- | ----------------------- | ---------------- |
| Controller <-> Complaint List | 컨트롤러가 컴플레인 리스트에게 컴플레인 목록을 가져올 것을 요청한다. | Convey Request |
| Processed Complaints <-> Approve Complaint | 창고관리자가 승인한 컴플레인을 Approve Complaint에 전달한다. | Convey Approved Complaint |
| Processed Complaints <-> Reject Complaint | 창고관리자가 거부한 컴플레인을 Reject Complaint에 전달한다. | Convey Rejected Complaint |
| Requested Complaints <-> Add Complaint | 점주가 신청한 요청 및 컴플레인을 Add Complaint에 전달한다. | Convey Added Complaint |
| Processed Complaints <-> Page Maker | 창고관리자가 처리한 컴플레인을 Page Maker에 전달한다. | Provide Processed Complaints |
| Requested Complaints <-> Page Maker | 점주가 신청한 요청 및 컴플레인을 Page Maker에 전달한다. | Provide Requested Complaints |
| Page Maker <-> Interface Page | 사용자에게 보여줄 페이지를 준비한다. | Prepare |

**3) Extracting the Attributes**

| Concept | Attributes | Attribute Description |
| ------- | ---------- | --------------------- |
| Processed Complaints | 승인/거부 컴플레인 데이터 | 창고관리자가 승언/거부한 컴플레인 ID |
| Requested Complaints | 요청/컴플레인 데이터 | 점주가 신청한 요청/컴플레인 ID |
| Interface Page | 변동된 컴플레인 데이터 | 창고관리자/점주가 수정한 컴플레인 |
