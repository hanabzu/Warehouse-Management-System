| Actor       | Actor's  Goal                                                | Use  case name                                               |
| ----------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 어드민      | 로그인 탭에서 자신의 아이디, 비밀번호를 입력해 로그인        | Login (UC-01)                                                |
| 어드민      | 로그아웃 버튼을 눌러 로그아웃                                | Logout (UC-02)                                               |
| 어드민      | 상품 데이터 추가/삭제/수정.                                  | ProductData (UC-07)                                          |
| 어드민      | 창고들의 상품 재고 확인                                      | ViewStock (UC-17)                                            |
| 어드민      | 리포트를 통한 각 상품에 대한 거래량 확인                     | ViewTransactions (UC-19)                                     |
| 어드민      | 창고관리자, 점주 계정 회원 가입 승인                         | AcceptUsers (UC-04)                                          |
| 어드민      | 모든 트랜잭션 내역 확인                                      | ViewTransactions (UC-19)                                     |
| 창고 관리자 | 어플리케이션에 계정 생성 신청                                | Register (UC-03)                                             |
| 창고 관리자 | 로그인 탭에서 자신의 아이디, 비밀번호를 입력해 로그인        | Login (UC-01)                                                |
| 창고 관리자 | 로그아웃 버튼을 눌러 로그아웃                                | Logout (UC-02)                                               |
| 창고 관리자 | 계정정보 수정                                                | ModifyProfile (UC-05)                                        |
| 창고 관리자 | 창고의 재고를 변경                                           | StockData (UC-08)                                            |
| 창고 관리자 | 창고의 상품들의 재고를 열람                                  | ViewStocks (UC-17)                                           |
| 창고 관리자 | 지점에게서 받은 발주를 자동으로 결재                         | ShopkeeperOrder (UC-09)                                      |
| 창고 관리자 | 필요한 상품을 자동으로 발주                                  | StorekeeperOrder (UC-10)                                     |
| 창고 관리자 | 자동 발주 날짜 이전에 발주할 목록 확인 후 수정               | StorekeeperOrder (UC-10)                                     |
| 창고 관리자 | 창고가 보낸 발주 내역 열람                                   | ViewTransactions (UC-19)                                     |
| 창고 관리자 | 근처 창고의 현재 재고 상황 확인                              | ViewStocks (UC-17)                                           |
| 창고 관리자 | 근처 창고의 차후 재고 예측 리포트 확인                       | ViewPredictionReports (UC-21)                                |
| 창고 관리자 | 창고의 재고 예측 리포트 확인                                 | ViewPredictionReports (UC-21)                                |
| 창고 관리자 | 창고의 과년도 동일 분기(계절)의 입출고 동향 리포트  확인     | ViewTrendsReports (UC-20)                                    |
| 창고 관리자 | 연결된 소매점 열람                                           | ViewBranches (UC-18)                                         |
| 창고 관리자 | 어드민에게 리퀘스트                                          | Request (UC-11)                                              |
| 점주        | 어플리케이션에 계정 생성 신청                                | Register (UC-03)                                             |
| 점주        | 로그인 탭에서 자신의 아이디, 비밀번호를 입력해 로그인        | Login (UC-01)                                                |
| 점주        | 로그아웃을 눌러 로그아웃.                                    | Logout (UC-02)                                               |
| 점주        | 계정정보 수정                                                | ModifyProfile (UC-05)                                        |
| 점주        | 판매 동향리포트 탭에서 주위 지역 판매 동향리포트를  확인한다. | ViewTrendsReports (UC-20)                                    |
| 점주        | 판매 동향리포트 탭에서 이전 달 상품들의 판매 동향  리포트를 확인한다. | ViewTrendsReports (UC-20)                                    |
| 점주        | 판매 동향리포트 탭에서 다음 달 상품들의 판매 예측  리포트를 확인한다. | ViewPredictionReports (UC-21)                                |
| 점주        | 판매 동향리포트 탭에서 과년도 동일 분기의 판매 동향  리포트를 확인한다. | ViewTrendsReports (UC-20)                                    |
| 점주        | 연결된 창고 탭에서 창고에 발주를 넣는다.                     | ShopkeeperOrder (UC-09)                                      |
| 점주        | 연결된 창고 탭에서 창고와의 트랜잭션 내역을 확인한다.        | ViewTransactions (UC-19)                                     |
| 점주        | 연결된 창고 탭에서 연결된 창고의 상품 재고를  확인한다.      | ViewStocks (UC-17)                                           |
| 점주        | 현재 지점 탭에서 현재 지점의 상품 재고 현황을 확인  한다.    | ViewStocks (UC-17)                                           |
| 점주        | 컴플레인 탭에서 필요한 상품/브랜드를 요청한다.               | Request (UC-11)                                              |
| 점주        | 컴플레인 탭에서 상품/브랜드에 대한 컴플레인을  신청한다.     | Request (UC-11)                                              |
| 점주        | 현재 지점 탭에서 현재 지점의 재고를 업데이트한다.  (상품 추가/수정/삭제) | StockData (UC-08)                                            |
| 점주        | 현재 지점 탭에서 판매 상품들에 대한 내역을 등록한다.         | SaleData (UC-12)                                             |
| 유저 모듈   | 유효한 계정 확인                                             | Login (UC-01), Register  (UC-03), AuthenticateUser (UC-06), UserData (UC-15) |
| 유저 모듈   | 임시 계정 저장                                               | Register (UC-03)                                             |
| 유저 모듈   | 새로운 계정 저장                                             | AcceptUsers (UC-04), UserData  (UC-15)                       |
| 유저 모듈   | 계정 정보 수정                                               | ModifyProfile (UC-05),  UserData (UC-15)                     |
| 데이터 모듈 | 상품 데이터 저장.                                            | ProductData(UC-07)                                           |
| 데이터 모듈 | 재고 데이터 저장.                                            | StockData(UC-08)                                             |
| 데이터 모듈 | 창고와 연결된 소매점 데이터 저장.                            | BranchData(UC-13)                                            |
| 데이터 모듈 | 트랜잭션 데이터를 저장.                                      | TransactionData(UC-14)                                       |
| 데이터 모듈 | 사용자에 대해 입력된 정보 저장.                              | UserData(UC-15)                                              |
| 데이터 모듈 | 리퀘스트 관련 정보 저장.                                     | RequestData(UC-16)                                           |
| 분석모듈    | 트랜잭션 내역을 날짜, 창고, 지점별로 수치화                  | ViewTransactions (UC-19)                                     |
| 분석모듈    | 지점별 판매 내역을 통해 판매량 데이터를 기간별로  그래프화   | ViewTrendReport (UC-20)                                      |
| 분석모듈    | 재고 상황을 확인할 때 거래량순, 브랜드별, 상품  유형별 그래프화 | ViewStocks (UC-17)                                           |
| 분석모듈    | 판매 동향 리포트를 수치화                                    | ViewTrendsReport (UC-20), WriteReport (UC-22)                |
| 분석모듈    | 판매 예측 리포트를 수치화                                    | ViewPredictionReport (UC-21), WriteReport (UC-22)            |
| 분석모듈    | 자동 발주될 상품들의 내역을 수치화                           | ViewTransactions (UC-19)                                     |

