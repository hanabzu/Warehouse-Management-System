** Use case (Actor's Goal) **

| Actor | Actor's Goal                                                          | Use case name (넘버링은 완성 후에) |
| ------------| ----------------------------------------------------------------- | ----------  |
| 어드민 | 로그인 탭에서 자신의 아이디, 비밀번호를 입력해 로그인  | Login |
| 어드민 | 로그아웃 버튼을 눌러 로그아웃               | Logout |
| 어드민 | 상품 데이터 추가/삭제/수정. | DataManagement |
| 어드민 | 창고들의 상품 재고 확인 | CheckStock |
| 어드민 | 리포트를 통한 각 상품에 대한 거래량 확인|	ViewTransactionAmount|
| 어드민 | 창고관리자, 점주 계정 회원 가입 승인 |AcceptUsers|
| 어드민 | 모든 트랜잭션 내역 확인   | ViewAllTransactions |
| 창고 관리자 | 어플리케이션에 계정 생성 신청                           | Register |
| 창고 관리자 | 로그인 탭에서 자신의 아이디, 비밀번호를 입력해 로그인  | Login |
| 창고 관리자 | 로그아웃 버튼을 눌러 로그아웃               | Logout |
| 창고 관리자 | 계정정보 수정                                          | ModifyProfile |
| 창고 관리자 | 창고에 상품을 등록                               | AddProduct |
| 창고 관리자 | 창고의 재고를 변경                                      | ManageStocks |
| 창고 관리자 | 창고의 상품들의 재고를 열람                        | ViewStocks |
| 창고 관리자 | 지점에게서 받은 발주를 자동으로 결재                           | ConfirmTransaction |
| 창고 관리자 | 필요한 상품을 자동으로 발주                          | Order, +(트랜잭션UC)|
| 창고 관리자 | 자동 발주 날짜 이전에 발주할 목록 확인 후 수정 | Order |
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
| 점주 | 판매 동향리포트 탭에서 이전 달 상품들의 판매 동향 리포트를 확인한다.      | ViewTransactionReports |
| 점주 | 판매 동향리포트 탭에서 다음 달 상품들의 판매 예측 리포트를 확인한다.   | ViewTransactionReports |
| 점주 | 판매 동향리포트 탭에서 과년도 동일 분기의 판매 동향 리포트를 확인한다.     | ViewTransactionReports |
| 점주 | 연결된 창고 탭에서 창고에 발주를 넣는다.           | Order |
| 점주 | 연결된 창고 탭에서 창고와의 트랜잭션 내역을 확인한다.           | ViewTransactions |
| 점주 | 연결된 창고 탭에서 연결된 창고의 상품 재고를 확인한다.        | ViewStocks |
| 점주 | 현재 지점 탭에서 현재 지점의 상품 재고 현황을 확인 한다.          | ViewStocks - 창고와 분리할 것인지? |
| 점주 | 컴플레인 탭에서 필요한 상품/브랜드를 요청한다.             | Request |
| 점주 | 컴플레인 탭에서 상품/브랜드에 대한 컴플레인을 신청한다.              | Request |
| 점주 | 현재 지점 탭에서 현재 지점의 재고를 업데이트한다. (상품 추가/수정/삭제)           | ManageStocks |
| 점주 | 현재 지점 탭에서 판매 상품들에 대한 내역을 등록한다.      | sale dataManagement    |
| 유저 모듈 | 점주, 창고 관리자 가입 정보 어드민에 전달                    | Register , 수락기능(위에서 선추가 필요) |
| 유저 모듈 | 어드민이 승인한 계정 가입 후 데이터에 추가                     | Register |
| 유저 모듈 | 어드민이 승인한 계정 로그인 승인                     | Login |
| 유저 모듈 | 계정 정보 수정 반영                                          | Users의 데이터는 어디에 저장?? |
| 유저 모듈 | 권한 확인        | 위에서의 권한 필요한 UC들 |
| 데이터 모듈 | 상품 데이터 저장.                         | ProductData(DataManagement, AddProduct) |
| 데이터 모듈 | 재고 데이터 저장.                         | StockData(CheckStock, ManageStocks, ViewStocks)|
| 데이터 모듈 | 창고와 연결된 소매점 데이터 저장.                       | BranchData(ViewBranches)   |
| 데이터 모듈 | 트랜잭션 데이터를 저장.                         | TransactionData(ViewTransactionAmount , ViewAllTransactions, ViewTransactionReports, ConfirmTransaction, ViewTransactions) |
| 데이터 모듈 | 사용자에 대해 입력된 정보 저장.                       | UserData(AcceptUsers, Register, Login, ModifyProfile)   |
| 데이터 모듈 | 리퀘스트 관련 정보 저장.                        | RequestData(Request)   |
| 분석모듈 | 트랜잭션 내역을 날짜, 창고, 지점별로 수치화	| AnalysisTransaction |
| 분석모듈 | 지점별 판매 내역을 통해 판매량 데이터를 기간별로 그래프화 |	AnalysisData |
| 분석모듈 | 재고 상황을 확인할 때 거래량순, 브랜드별, 상품 유형별 그래프화 |	AnalysisStock |
| 분석모듈 |	판매 동향 리포트를 수치화 |	AnalysisTrend |
| 분석모듈 |	판매 예측 리포트를 수치화 |	AnalysisPrediction |
| 분석모듈 |	자동 발주될 상품들의 내역을 수치화	 | AnalysisAuto |


