\# SET OPERATIONS WITH EXAMPLE:

**1. add() :- adds element in set randomly**

s1 = {10,'Adesh'}

print(s1,type(s1)) ---------{10, 'Adesh'} <class 'set'>

s1.add(20)

print(s1,type(s1)) ---------{10, 20, 'Adesh'} <class 'set'>

s1.add("Harry")

s1.add(34.56)

s1.add(2+3j)

s1.add(10)

print(s1,type(s1)) ----------{34.56, 10, (2+3j), 20, 'Harry', 'Adesh'} <class 'set'>



**2. clear() :- clear all the set elements and makes set empty**

print(s1) ---------------{34.56, 10, (2+3j), 20, 'Harry', 'Adesh'}

len(s1) ------------------6

s2=s1

print(s2) --------------- {34.56, 10, (2+3j), 20, 'Harry', 'Adesh'}

print(s2.clear()) -------- None

print(s2) ---------------- set()



**3. remove(val) :- removes passed element from the set.**

print(s1) -------- set()

print(s2) -------- set()

s1 = {34.56, 10, (2+3j), 20, 'Harry', 'Adesh'}

print(s1,type(s1)) ------- {34.56, 20, 'Harry', 10, (2+3j), 'Adesh'} <class 'set'>

s1.remove("Harry")

print(s1)  --------- {34.56, 20, 10, (2+3j), 'Adesh'}

s1.remove(2+3j)

print(s1) ---------- {34.56, 20, 10, 'Adesh'}



**4. discard(val) :- delete passed value from set if set is empty it returns 'none' remove returns 'error'.**

s1 = {100,"Punit",45.67,'MH','Python'}

print(s1,type(s1)) ------- {'Punit', 100, 'MH', 45.67, 'Python'} <class 'set'>

print(id(s1)) ------------ 2511077872736

s2 = s1   **# deep/Alising copy** 

print(s2,type(s2),id(s2)) ---------- {'Punit', 100, 'MH', 45.67, 'Python'} <class 'set'> 2511077872736

s3= s1.copy **# shallow/cloning copy**

s1.discard('Punit')

print(s1) ----------- {100, 'MH', 45.67, 'Python'}

print(s2) ----------- {100, 'MH', 45.67, 'Python'}

**print(s1.discard('Punit')) -------- None (data not available)**

print(s1.remove('Punit')) ------------ Traceback (most recent call last):

&nbsp; 					File "<pyshell#43>", line 1, in <module>

&nbsp;					print(s1.remove('Punit'))  KeyError: 'Punit'



**5.pop() :- removes data from set randomly** 

s1.pop() ------- 100

s1.pop() ------- 'MH'

print(s1) ------- {45.67, 'Python'}

s1.pop() -------- 45.67

print(s1) -------- {'Python'}

s1.pop() --------- 'Python'

s1.pop() --------- Traceback (most recent call last):

&nbsp;			 File "<pyshell#51>", line 1, in <module>

&nbsp;   			s1.pop()   KeyError: 'pop from an empty set' 



**6. copy() :- copy one set objects in another.**

s1 = {100,'Gaurav',2+3j,'MP-09',"MH-28"}

print(s1,type(s1),id(s1)) ------- {'Gaurav', 100, (2+3j), 'MP-09', 'MH-28'} <class 'set'> 2511077878336

s2 = s1.copy()  **#shallow/ cloning copy** 

print(s2,type(s2),id(s2)) ---------- {'Gaurav', 100, (2+3j), 'MP-09', 'MH-28'} <class 'set'> **2511077880352**

s3 = s2  **# deep/Alising copy**

print(s3,type(s3),id(s3)) --------- {'Gaurav', 100, (2+3j), 'MP-09', 'MH-28'} <class 'set'> **2511077880352**

s2.add('Maharashtra')

print(s3,id(s3)) ---------{'Gaurav', 100, 'Maharashtra', (2+3j), 'MP-09', 'MH-28'} **2511077880352** 



**7. isdisjoint( val ) :- checks whether both set are different or not.**

s1 = {10,20,30}

s2 = {10,40,50}

s3 = {'MP','MH','RJ'}

print(s1,id(s1)) -------- {10, 20, 30} 2511077879232

print(s2,id(s2)) -------- {40, 10, 50} 2511072768544

print(s3,id(s3)) -------- {'RJ', 'MH', 'MP'} 2511077878336

s1.isdisjoint(s2) ------- False

s1.isdisjoint(s3) ------- True

s2.isdisjoint(s3) ------- True

set().isdisjoint({10,20,30}) ------ True



**8. issuperset( val ) :- checks whether all elements of (2nd) set is present in 1st set or not.**

s1 = {10,20,30}

s2 = {10,20,30,40,50,60}

s3 = {40,50,60,70,80,90}

s1.issuperset(s2) ------------ False

s2.issuperset(s1) ------------ True

s3.issuperset(s2) ------------ False

s2.issuperset(s3) ------------ False

s1.disjoint(s2) -------------- Traceback (most recent call last):

&nbsp;			       File "<pyshell#106>", line 1, in <module>

&nbsp;   					s1.disjoint(s2)

&nbsp;					AttributeError: 'set' object has no attribute 						'disjoint'. Did you mean: 'isdisjoint'?

s1.isdisjoint(s2) ----------- False

s3.isdisjoint(s1) ----------- True

print(s1,s2,s3) ----------- {10, 20, 30} {50, 20, 40, 10, 60, 30} {80, 50, 70, 40, 90, 60}



**9. issubset(val) :- checks all the elements of (1st) is present in the second or not.**

s1 = {10,20,30}

s2 = {10,20,30,40,50,60}

s3 = {40,50,60,70,80,90}

s1.issubset(s2) ----------- True

s1.issubset(s3) ----------- False



**10. union():- combines the elements of both set.**

s1 = {10,20,30,40}

s2 = {40,20,50,60}

s3 = s1.union(s2)

print(s3) ----- {40, 10, 50, 20, 60, 30}

s4 = s2.union(s1) 

print(s4) ------ {40, 10, 50, 20, 60, 30}



**11. intersection() :- takes all the common elements of both set and insert in the 3rd set**

s1 = {10,20,30,40}

s2 = {40,20,50,60}

s3 = s1.intersection(s2)

print(s3) ---------- {40, 20}



**12. intersection_update() :- takes all common elements from both the list and update to 1st set.** 

print(s1,s2) ------------ {40, 10, 20, 30} {40, 50, 20, 60}

s3 = s1.intersection_update(s2)

print(s3) --------------- None

print(s1,s2) ------------ {40, 20} {40, 50, 20, 60}

print(s2.intersection_update(s1)) --------- None

s2 --------- {40, 20}



**13. difference() :- takes all the unique elements of 1st set and insert in the 3rd set**

s1 = {10,20,30,40}

s2 = {40,20,50,60}

s3 = s1.difference(s2)

print(s3) ---------- (10, 30} 

s4 = s2.difference(s1)

print(s4) ---------- {50, 60}



**14. difference_update() :- takes all unique elements from both the list and update to 1st set.**

s1 = {10,20,30,40}

s2 = {40,20,50,60}

print(s1 , s2) ------------ {40, 10, 20, 30} {40, 50, 20, 60}

s3 = s1.difference
_update(s2)

print(s3) ----------------- None

print(s1) ---------------- {10, 30}





**15. symmetric\_difference() :- takes all unique elements from both the list and update to 3rd set.**

s1 = {10,20,30,40}

s2 = {40,20,50,60}

s3 = s1.symmetric\_difference(s2)

print(s3) ------------ {10, 50, 60, 30}

s4 = s2.symmetric\_difference(s1)

print(s4) ------------ {10, 50, 60, 30}





**16. symmetric\_difference\_update():- takes all unique elements from both the list and update to 1st set.**

s1 = {10,20,30,40}

s2 = {40,20,50,60}

s3 = s1.symmetric\_difference\_update(s2)

print(s3) ------------- None

print(s1) ------------- {10, 50, 60, 30} 



**17. update() :- combines both the sets and stores in 1st set.**

s1 = {10,20}

s2 = {30,40}

s1.update(s2)

print(s1) ------- {40, 10, 20, 30}

s3 = s1.update(s2)

print(s3) ------- None

