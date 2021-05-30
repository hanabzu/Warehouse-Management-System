### **UC-04 AcceptUsers**

Admin이 AcceptUsers() 함수를 call하면 실행

tempAccounts의 목록을 보여줌 (SDD에선 UserModule에서 가져오지만 DatabaseModule에서 가져오는 것으로 변경)

(이때 tA 정보에는 pw 미포함)

tA를 선택하면 수락, 거절 , 취소를 선택할 수 있음.

수락을 누르면 tA가 저장되고, 거절을 누르면 거절 사유를 입력하게 됨, 취소를 두르면 다시 tA목록을 보여줌.



**TestCase:**

1) AcceptUsers()함수를 콜

​	-> tAs의 목록을 보여주고, 어드민은 선택할 수 있어야 함

2) tA 선택

​	-> tA의 계정 정보를 보여주고, 수락, 거절, 취소 버튼 중 선택할 수 있어야 함

3) 수락 선택

​	-> 계정정보가 UserData()를 통해 저장되도록 UserModule에 전달,  수락되었음을 알리고 다시 tA 목록 페이지로 돌아감

4) 거절 선택

​	-> 거절 사유를 입력하는 창 띄움, (입력칸과 제출, 취소 버튼) 입력 후 제출 선택하면 UserModule로 전달 후 다시 tA목록 페이지로 돌아감

5) 취소 선택

​	-> 다시 tA 목록으로 돌아감.







