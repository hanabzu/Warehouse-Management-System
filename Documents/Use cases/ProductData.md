# Use Case: ProductData

## **Related Requirements**

REQ-1 ,REQ-15

## **Initiating Actors**

Any of: 어드민 , 창고관리자

## **Actor's Goal**

상품에 대한 데이터를 저장한다.

## **Participating Actors**

 - 

## **Preconditions**

- 제품명,브랜드,수량에 대한 데이터는 필히 입력되어있어야한다.
- 시스템에서 제품에 대한 정보를 입력/수정/삭제하는 화면이 출력되어야한다.

## **Postconditions**

- 데이터베이스에 상품에 대한 정보가 저장된다.

## Flow of Events for Main Success Scenario
| Direction | n | Actor Action                                                                                                         |
| --------- | - | -------------------------------------------------------------------------------------------------------------------- |
| ←         | 1 | System shows 'login' page with radio button and input fields for selecting User's type and entering ID and password. |
| →         | 2 | User selects whether he/she is Manager or Guest. |
| →         | 3 | User inputs valid ID and password in the blank. |
| →         | 4 | User clicks the 'Login’ button. |
| ←         | 5 | System prepares a database query that perfectly matches the actor's ID and retrieves the record from the Database. |
| →         | 6 | Database returns the matching record. |
| ←         | 7 | System checks that the ID and password entered by the actor are valid. |
| ←         | 8 | System passes the log to Database. |
| →         | 9 | Database records the log as successful login. |
| ←         | 10 | System redirects User to the ‘Add Book’ page if he/she is valid Manager or to the ‘Search Book’ page if he/she is valid Guest. |


## Flow of Events for Extensions (Alternate Scenarios)
3a. User inputs invalid ID and password in the blank.
| Direction | n | Actor Action                                                                                                         |
| --------- | - | -------------------------------------------------------------------------------------------------------------------- |
| →         | 1 | User clicks the 'Login’ button. |
| ←         | 2 | System prepares a database query that perfectly matches the actor's ID and retrieves the record from the Database. |
| →         | 3 | Database returns the matching record. |
| ←         | 4 | System checks that the ID and password entered by the actor are invalid. |
| ←         | 5 | System (a) detects error, (b) passes the log to the database, and (c) shows a login fail message. |
| →         | 6 | Database (a) records the log as failed login and (b) returns the login fail count to System. |
| ←         | 6a | System (a) detects that the count of failed attempts exceeds the maximum allowed number, (b) signals to the actor, and (c) blocks the login action for 10 minutes. |
| →         | 7 | Same as in Step 3 above. |
