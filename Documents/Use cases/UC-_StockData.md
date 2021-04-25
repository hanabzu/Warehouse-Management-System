# Use Case: StockData

## **Related Requirements**

REQ-2 ,REQ-3, REQ-11, REQ-12, REQ-22

## **Initiating Actors**

Any of: 어드민 , 창고관리자, 점주

## **Actor's Goal**

재고(상품수량)에 대한 데이터를 저장한다.

## **Participating Actors**

 - 

## **Preconditions**

- 제품이 존재해야만 한다.

## **Postconditions**

- 데이터베이스에 해당 상품에 대한 재고가 저장된다.

## Flow of Events for Main Success Scenario
| Direction | n | Actor Action                                                                                                         |
| --------- | - | -------------------------------------------------------------------------------------------------------------------- |
| →         | 1 | 재고를 파악할 상품을 입력칸에 입력한다. |
| ←         | 2 | 상품에 대한 정보와 재고를 화면에 출력하고, 수정을 원하면 수정할 수 있도록 한다(a). |


## Flow of Events for Extensions (Alternate Scenarios)
2a. 수정을 원하면 수정할 수 있도록 한다.
| Direction | n | Actor Action                                                                                                         |
| --------- | - | -------------------------------------------------------------------------------------------------------------------- |
| →         | 1 | 입력칸에 데이터를 입력하고 '저장'버튼을 누른다. |
| ←         | 2 | 데이터베이스상에 입력한 데이터를 업데이트한다. |
| →         | 3 | 수정이 완료되었다는 화면을 출력한다. |

