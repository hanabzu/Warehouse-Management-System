**Requirements**

| Idetifier | Priority | F/NF | Requirement                                                  |
| --------- | -------- | ---- | ------------------------------------------------------------ |
| REQ-1     | 5        | F    | 시스템은 모든 판매 데이터를 수집하고 관리해야한다. |
| REQ-2     | 5        | F    | 시스템은 점주가 점주 주위 지역의 판매 동향 리포트를 확인할 수 있게 해야 한다. |
| REQ-3     | 4        | F    | 시스템은 점주가 다음 달 물품들의 판매 예측 리포트를 확인할 수 있게 해야 한다. |
| REQ-4     | 3        | F    | 시스템은 점주가 이전 달 물품들의 판매 동향 리포트를 확인할 수 있게 해야 한다. |
| REQ-5     | 3        | F    | 시스템은 점주가 과 년도 동일 분기(계절)의 판매 동향 리포트를 확인 할 수 있게 해야 한다.|
| REQ-6     | 3        | F    | 시스템은 창고관리자가 근처 창고의 현재 재고 상황을 확인할 수 있게 해야 한다. |
| REQ-7     | 5        | F    | 시스템은 창고관리자가 근처 창고의 차후 재고 예측 리포트를 확인할 수 있게 해야 한다. |
| REQ-8     | 4        | F    | 시스템은 창고관리자가 해당 창고의 다음 달 재고 예측 리포트를 확인할 수 있게 해야 한다. |
| REQ-9     | 4        | F    | 시스템은 창고관리자가 해당 창고의 이전 달 재고 예측 리포트를 확인할 수 있게 해야 한다. |
| REQ-10    | 3        | F    | 시스템은 창고관리자가 해당 창고의 과 년도 동일 분기(계절)의 입출고 동향 리포트를 확인할 수 있게 해야 한다. |
| REQ-11    | 5        | NF   | 시스템은 날짜가 변경될때마다 창고에 있는 총 재고상황을 업데이트한다. |
| REQ-12    | 5        | NF   | 시스템은 창고에 물품에 변경사항이 있을때마다 재고상황을 업데이트한다. |
| REQ-13    | 5        | NF   | 시스템은 창고 내 재고에대해 정확하게 카운팅해야한다. |
| REQ-14    | 5        | NF   | 시스템이 제공하는 동향,예측리포트는 수치화,그래프화 해야한다. |
| REQ-15    | 5        | NF   | 시스템은 점주,창고관리자로부터 리포트에 대한 피드백을 받을 수 있어야한다. |
| REQ-16    | 3        | NF   | 시스템은 판매 동향 리포트을 클릭을 통해 월을 선택할 수 있다. |
| REQ-17    | 5        | F    | 시스템은 어드민이 모든 트랜잭션 내역을 확인할 수 있도록 해야 한다. |
| REQ-18    | 5        | F    | 시스템은 창고 관리자가 현재 창고의 재고 상황을 알 수 있도록 제공해야 한다. |
| REQ-19    | 4        | F    | 시스템은 창고의 재고 상황과 트랜잭션 내역을 분석하여 물품을 각 브랜드에 자동으로 발주해야 한다. |
| REQ-20    | 3        | F    | 시스템은 창고 관리자가 창고의 물품과 연결된 브랜드 리스트를 확인하고 추가 등록/삭제를 어드민에게 요청할 수 있도록 해야 한다. |
| REQ-21    | 5        | F    | 시스템은 창고가 점주에게서 온 발주를 재고에 맞춰 자동으로 확인하여 결재하도록 해야 한다. |
| REQ-22    | 2        | NF   | 시스템은 창고 관리자가 추가 입고 신청 내역을 즉시 확인할 수 있게 해야 한다. |
| REQ-23    | 5        | F    | 시스템은 창고 관리자가 날짜시간별, 지점별로 발주한 상품들에 대한 영수증을 확인할 수 있게 해야 한다. |
| REQ-24    | 5        | F    | 시스템은 점주가 연결된 창고에 물품 발주를 넣을 수 있도록 해야 한다. |
| REQ-25    | 4        | F    | 시스템은 점주가 연결된 창고와의 트랜잭션 내역을 볼 수 있도록 해야 한다. |
| REQ-26    | 3        | F   | 시스템은 점주가 현재 연결된 창고의 남은 물품 재고를 확인할 수 있도록 해야 한다. |
| REQ-27    | 5        | F    | 시스템은 점주가 현재 지점의 남은 물품 재고 현황을 확인할 수 있도록 해야 한다. |
| REQ-28    | 4        | F    | 시스템은 점주가 어드민에게 필요한 물품/브랜드를 요청할 수 있도록 해야한다. |
| REQ-29    | 2        | F    | 시스템은 점주가 어드민에게 물품/브랜드에 대한 컴플레인을 넣을 수 있도록 해야 한다. |
| REQ-30    | 5        | F    | 시스템은 창고 관리자가 창고의 재고를 등록/삭제 할 수 있도록 해야 한다. |
| REQ-31    | 5        | F    | 시스템은 점주가 지점의 재고를 등록/삭제 할 수 있도록 해야 한다.  |
| REQ-32    | 5        | NF    | 시스템은 창고 관리자가 등록/삭제한 재고를 즉시 데이터에 반영 해야 한다. 물품의 양/브랜드 등. |
| REQ-33    | 5        | NF    | 시스템은 점주가 지점에 등록/삭제한 재고를 즉시 데이터에 반영 해야 한다. 물품의 양/브랜드 등. |
| REQ-34    | 2        | NF   | 시스템은 창고 관리자가 주로 거래되는 물품 데이터를 확인할 때, 거래량이 높은 물품을 상단에 노출시킨다.  |
| REQ-35    | 3        | F    | 시스템은 창고 관리자가 연결된 소매점 목록을 확인할 수 있도록 해야 한다.   |
| REQ-36    | 4        | F    | 시스템은 점주가 물품을 판매한 내역, 즉, 물품별 판매 내역을 등록할 수 있도록 해야한다.  |
| REQ-37    | 4        | NF   | 시스템은 지점별 판매 내역을 통해 월별 판매량을 데이터로 관리해야 한다.  |
| REQ-38    | 5        | F    | 시스템은 어드민이 해당 브랜드에 상품에 대한 컴플레인 혹은 의견을 보낼 수 있게 해야한다.  |
| REQ-39     | 5        | F   | 시스템은 어드민이 필요한 브랜드의 상품을 요청하거나 처리할 수 있게 해야한다. |
| REQ-40     | 4        | F    | 시스템은 어드민이 상품이 부족할 시 대체할 수 있게 창고를 확인 할 수 있게 해야한다. |
| REQ-41     | 3        | F   | 시스템은 어드민이 해당 창고의 제품 수량을 실시간으로 확인 할 수 있게 해야한다. |
| REQ-42     | 3        | NF   | 시스템은 어드민이 주문한 물품의 배송 이동경로를 확인 할 수 있게 해야한다. |
| REQ-43     | 3        | F   | 시스템은 어드민이 배송 상황을 확인 할 수 있게 해야한다. |
| REQ-44     | 5        | F    | 시스템은 어드민이 리포트를 통해 물품에 대한 구매량을 확인 할 수 있게 해야한다. |
| REQ-45     | 4        | NF    | 시스템은 어드민이 해당 브랜드의 제품을 수량을 직접 입력할 수 있게 해야한다. |