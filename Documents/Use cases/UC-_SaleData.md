# Use Case: SaleData(Management)

## **Related Requirements**
- REQ-25, REQ-26

## **Initiating Actors**

Any of: 점주

## **Actor's Goal**

실제로 판매한 데이터를 저장한다.

## **Participating Actors**

 - StockData

## **Preconditions**

- 해당 상품이 지점의 재고에 남아있어야 한다.

## **Postconditions**

- 판매한 상품이 판매량 데이터에 저장이 되고, 지점의 재고에서 판매된 만큼 삭제된다.

## Flow of Events for Main Success Scenario
| Direction | n | Actor Action                                                                                                         |
| --------- | - | -------------------------------------------------------------------------------------------------------------------- |
| →         | 1 | 점주는 판매 내역을 입력한다. (상품/수량) (a) |
| ←         | 2 | 시스템은 입력받은 판매 내역을 판매량 데이터에 저장하고, 판매 된 만큼 지점의 재고를 수정한다.|



## Flow of Events for Extensions (Alternate Scenarios)
1a. 판매 내역을 잘못 입력했을 시.
| Direction | n | Actor Action                                                                                                         |
| --------- | - | -------------------------------------------------------------------------------------------------------------------- |
| →         | 1 | 점주는 자신이 입력한 판매 내역을 확인하고 잘못 되었을 시 수정/삭제 할 수 있다. |
| ←         | 2 | 시스템은 점주가 수정/삭제한 판매 내역을 즉시 반영해서 판매량 데이터를 업데이트하고, 지점의 재고를 수정한다. |

