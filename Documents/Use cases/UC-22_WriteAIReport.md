# Use Case UC-22: WriteReport

## **Related Requirements**
REQ-26, REQ-29, REQ-30 


## **Initiating Actors**

Any of: 분석모듈

## **Actor's Goal**
판매 예측 리포트를 작성한다.


## **Participating Actors**
-점주, 데이터 모듈

## **Preconditions**

- 판매량 데이터가 존재해야 한다.

## **Postconditions**

- 판매 동향 리포트 및 판매 예측 리포트를 작성한다.

## Flow of Events for Main Success Scenario
| Direction | n    | Actor Action                                                 |
| --------- | ---- | ------------------------------------------------------------ |
| ←         | 1    | 시스템은 데이터 모듈에 있는 판매량 데이터 모두를 분석모듈에 전달 한다. |
| →         | 2    | 분석모듈은 판매량 예측모델을 만들고 데이터베이스에 저장한다. |
| →         | 3    | 점주는 해당 매장의 판매량 데이터를 입력한다.                 |
| ←         | 4    | 시스템은 예측에 필요한 판매량 데이터 및 예측모델을 분석모듈에 전달 한다. |
| →         | 2    | 분석모듈은 판매량 예측모델을 통해 예측을 하고 데이터베이스에 저장한다. |
