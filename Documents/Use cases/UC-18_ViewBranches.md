# Use Case UC-18: ViewBranches

## **Related Requirements**

REQ-23, REQ-24

## **Initiating Actors**

Any of: 창고관리자

## **Actor's Goal**

연결된 소매점 열람

## **Participating Actors**

- 데이터 모듈

## **Preconditions**

- 데이터베이스에 연결된 소매점에 대한 정보가 저장되어 있어야 한다.

## **Postconditions**

- 연결된 소매점을 화면에 출력한다.

## Flow of Events for Main Success Scenario
| Direction | n    | Actor Action                                                 |
| --------- | ---- | ------------------------------------------------------------ |
|           | 1    | include BranchData(UC-#)                                     |
| →         | 2    | 사용자가 소매점 열람 버튼을 누른다.                          |
| ←         | 3    | 해당 데이터베이스 테이블을 분석하여 열람 가능한지 판단한다.(a) |
| ←         | 4    | 알맞은 테이블의 정보를 화면에 출력한다.                      |

## Flow of Events for Extensions (Alternate Scenarios)

2a. 열람이 불가능하다고 판단되는 경우.

| Direction | n    | Actor Action                                                 |
| --------- | ---- | ------------------------------------------------------------ |
| ←         | 1    | 요청들어온 데이터의 Primary Key가 테이블에 존재하는지 확인한다. |
| ←         | 1a   | Primary Key가 존재하지 않으면 에러.                          |

