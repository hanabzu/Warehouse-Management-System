** Use case (Actor's Goal) **

| Actor | Actor's Goal                                                          | Use case name (넘버링은 완성 후에) |
| ------------| ----------------------------------------------------------------- | ----------  |
| 어드민 | 로그인 탭에서 자신의 아이디, 비밀번호를 입력해 로그인 | Login |
| 어드민 | 로그아웃 버튼을 눌러 로그아웃 | Logout |
| 어드민 | 가입 수락기능 |AdministerUsers|
| 어드민 | 모든 트랜잭션 내역을 확인             | ViewAllTransactions |
| 어드민 | 상품이 부족할 시 대체할 수 있게 창고를 확인 할 수 있다.     |   AdministerProduct   | <-이해 어려움. 창고/지점에 상품이 부족? 자동 발주 기능을 위한 것인가요?
| 어드민 | 해당 창고의 제품 수량을 실시간으로 확인 할 수 있다.       | AdministerProduct | REQ 어드민 파트 먼저 수정 보완 필요 (가입수락기능 등) |
| 어드민 | 리포트를 통해 물품에 대한 구매량을 확인 할 수 있다        | ViewTransactionReports       |<- 어떤 물품 구매량인지 모르겠어요. 창고에 입고하는 걸 말하는 건가요?
| 창고 관리자 | 어플리케이션에 계정 생성 신청                           | Register |
| 창고 관리자 | 로그인 탭에서 자신의 아이디, 비밀번호를 입력해 로그인  | Login |
| 창고 관리자 | 로그아웃 버튼을 눌러 로그아웃               | Logout |
| 창고 관리자 | 계정정보 수정                                           | ModifyProfile |
| 창고 관리자 | 창고에 상품을 등록                               | AddProduct |
| 창고 관리자 | 창고의 재고를 변경                                      | ManageStocks |
| 창고 관리자 | 창고의 물품들의 재고를 열람                             | ViewStocks |
| 창고 관리자 | 지점에게서 받은 발주를 자동으로 결재                           | ConfirmTransaction |
| 창고 관리자 | 필요한 물품을 자동으로 발주                            | Order, +(트랜잭션UC)|
| 창고 관리자 | 창고가 보낸 발주 내역 열람                                   | ViewTransactions |
| 창고 관리자 | 근처 창고의 현재 재고 상황 확인                         | ViewStocks |
| 창고 관리자 | 근처 창고의 차후 재고 예측 리포트 확인                  | ViewPredictionReports |
| 창고 관리자 | 창고의 재고 예측 리포트 확인                            | ViewPredictionReports | 
| 창고 관리자 | 창고의 과년도 동일 분기(계절)의 입출고 동향 리포트 확인 | ViewTransactionReports |
| 창고 관리자 | 연결된 소매점 열람                              | ViewBranches |
| 창고 관리자 | 어드민에게 리퀘스트                                     | Request |
| 점주 | 어플리케이션에 계정 생성 신청 | Register |
| 점주 | 로그인 탭에서 자신의 아이디, 비밀번호를 입력해 로그인      | Login |
| 점주 | 로그아웃을 눌러 로그아웃.      | Logout |
| 점주 | 계정정보 수정      | ModifyProfile |
| 점주 | 판매 동향리포트 탭에서 주위 지역 판매 동향리포트를 확인한다.             | ViewTransactionReports |
| 점주 | 판매 동향리포트 탭에서 이전 달 물품들의 판매 동향 리포트를 확인한다.      | ViewTransactionReports |
| 점주 | 판매 동향리포트 탭에서 다음 달 물품들의 판매 예측 리포트를 확인한다.   | ViewTransactionReports |
| 점주 | 판매 동향리포트 탭에서 과년도 동일 분기의 판매 동향 리포트를 확인한다.     | ViewTransactionReports |
| 점주 | 판매 동향리포트 탭에서 리포트에 대한 피드백을 한다. ( REQ-15 기반 )       | FeedbackReports | <- 리포트에 대한 피드백이 어떤 것인지 잘 모르겠어요.
| 점주 | 연결된 창고 탭에서 창고에 발주를 넣는다.           | Order |
| 점주 | 연결된 창고 탭에서 창고와의 트랜잭션 내역을 확인한다.           | ViewTransactions |
| 점주 | 연결된 창고 탭에서 연결된 창고의 물품 재고를 확인한다.        | ViewStocks |
| 점주 | 현재 지점 탭에서 현재 지점의 물품 재고 현황을 확인한다.               | ViewStocks - 창고와 분리할 것인지? |
| 점주 | 컴플레인 탭에서 필요한 물품/브랜드를 요청한다.             | Request |
| 점주 | 컴플레인 탭에서 물품/브랜드에 대한 컴플레인을 신청한다.              | Request |
| 점주 | 현재 지점 탭에서 현재 지점의 재고를 업데이트한다. (물품 추가/삭제)           | ManageStocks |
| 점주 | 현재 지점 탭에서 판매 되는 물품들에 대한 내역을 등록한다.      | sale dataManagement    |
| 유저 모듈 | 점주, 창고 관리자 가입 정보 어드민에 전달                    | Register , 수락기능(위에서 선추가 필요) |
| 유저 모듈 | 어드민이 승인한 계정 가입 후 데이터에 추가                     | Register |
| 유저 모듈 | 어드민이 승인한 계정 로그인 승인                     | Login |
| 유저 모듈 | 계정 정보 수정 반영                                          | Users의 데이터는 어디에 저장?? |
| 유저 모듈 | 권한 확인        | 위에서의 권한 필요한 UC들 |
| 데이터 모듈 | 제품에 대한 입력된 정보를 저장한다.                         | ManageProduct(input) |
| 데이터 모듈 | 제품에 대한 수정된 정보를 저장한다.                         | ManageProduct(modify) |
| 데이터 모듈 | 사용자에 대해 입력된 정보를 저장한다.                       | ManageUser(input)    |
| 데이터 모듈 | 사용자에 대해 수정된 정보를 저장한다.                       | ManageUser(modify)   |
| 데이터 모듈 | 날짜별로 판매된 제품의 수량을 저장한다.                    | Generalizations |
| 데이터 모듈 | 제품의 수량이 변경될 때마다 실시간으로 기록한다.             | UpdateStock     |
| 데이터 모듈 | 트렌젝션 데이터를 보여준다.                                | ShowTransactions  |
| 데이터 모듈 | 창고에 남아있는 재고데이터를 보여준다.                      | ShowStock(ViewStock과 통함?)   |
| 데이터 모듈 | 창고에 보관중인 물품에 대한 데이터를 보여준다.               | ShowProduct   |
| 데이터 모듈 | 어드민,점주,창고관리자가 열람 가능                          | 권한 확인인듯합니다  |
| 분석모듈 | 해당 점주의 주위 지역의 판매 동향 그래프화, 수치화          |               |
| 분석모듈 | 분기당 해당 브랜드 물품의 판매량 수치화                     |               |
| 분석모듈 | 데이터 모듈을 통해 예측리포트 수치화하여 사용자에게 제공     |               |
| 분석모듈 | 데이터 모듈을 통해 과년도 판매 동향을 제공                  |               |
| 분석모듈 | 데이터 모듈을 통해 현재 판매 동향을 제공                   |               |
| 분석모듈 | 창고의 동향리포트를 통해 현재 재고 리포트 수치화            |               |
| 분석모듈 | 창고의 동향리포트를 통해 재고 예측 리포트 수치화            |               |
| 분석모듈 | 과년도와 비교하여 제품의 재고 현황 예측 리포트 수치화        |                 |

