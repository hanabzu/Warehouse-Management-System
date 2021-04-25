# Domain Model for UC-03 : Register 

**1) Extracting the Responsibilities**

| Responsibility Description                                   | Type | Concept Name |
| ------------------------------------------------------------ | ---- | ------------ |
| 각 콘셉트간의 데이터를 조직화하고, 다른 콘셉트에 요청을 전달한다. | D    | Controller   |
| 사용자가 입력한 계정 정보                                      | K    | AccountData  |
| 사용자가 입력한 계정 정보에서 ID가 중복되는지 확인한다. | D | RedundancyChecker |
| 사용자에게 어드민의 승인을 기다리라는 메세지를 띄운다.  | K | Notifier  | 




**2) Extracting the Associations**

| Concept pair | Association Description | Association Name |
| ------------------ | ----------------------- | ---------------- |
| AccountData <-> Controller | 사용자가 입력한 계정 정보를 요청한다.    | Request Data |
| RedundancyChecker <-> Controller | ID가 중복되는 지 확인할 것을 요청한다.  | convey Request |
| Controller <-> Notifier | 사용자에게 메세지를 띄울 것을 요청한다. | convey Request |

**3) Extracting the Attributes**

| Concept | Attributes | Attribute Description |
| ------- | ---------- | --------------------- |
| AccountData  | ID/PW | 사용자가 입력한 ID와 패스워드 |
|              | 사용자 정보 | 사용자가 입력해야 하는 기타 정보 ( 점주/창고, 지역, 등..) |
| RedundancyChecker  | 등록된 ID | 이미 등록한 사용자들의 ID  |
