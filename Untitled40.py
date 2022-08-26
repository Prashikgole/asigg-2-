#!/usr/bin/env python
# coding: utf-8

# # 1.What are the two values of the Boolean data type? How do you write them?

# boolean type data is data which only can be true or false .
# 
# a= True ,
# b= False 
# 
# a = 1<=2 (true)
# b = 1>= 2 (false)

# # 2. What are the three different types of Boolean operators?

#  There are two type of boolean operatpors 1. True , 2. False 
#  logical operators like "and" , "or" are also can be boolean data 

# 3. Make a list of each Boolean operator&#39;s truth tables (i.e. every possible combination of Boolean
# values for the operator and what it evaluate ).

# In[ ]:


FOR AND :-

A         B    A and B
True    True    True
False   True    False
True    False   False
False   False   False
  
FOR OR :-
A       B       A or B
True    True     True
False   True     True
True    False    True
False   False    False


# 4. What are the values of the following expressions?

# In[ ]:


1.(5 >4) and (3 == 5)
   False

2. not (5 > 4)
   False

3. (5 > 4) or (3 == 5)
   True

4.not ((5 > 4) or (3 == 5))
    False

5.(True and True) and (True == False)
   False

6.(not False) or (not True)
   True


# 5. What are the six comparison operators?

# In[ ]:


< , > , <= , >= , == , !=
   


# 6. How do you tell the difference between the equal to and assignment operators?Describe a
# condition and when you would use one.

# In[ ]:


##if there a conditions are attach to equal to sigh it means it is assignment operators like

Operator Example   Same As
+=       x += 3    x = x + 3
-=       x -= 3    x = x - 3
*=       x *= 3    x = x * 3
(=, x, /=, 3, x, =, x, /, 3)


# 7. Identify the three blocks in this code:

# In[21]:


spam = 0
if spam == 10:
     print("eggs")        #this is first block
if spam > 5:
    print("bacon")        # this is second block
else:
    print("ham")          
    print("spam")         # this is third block of program
    print("spam")


# In[ ]:


8. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints
Greetings! if anything else is stored in spam.


# spam = 3 
# 
# if spam == 1:
#     print("Hello")
# if spam == 2:
#     print("Howdy")
# else:
#     print("Greetings!")

# 9.If your programme is stuck in an endless loop, what keys you’ll press?

# you press ctrl-c key or you can just restart kernal .

# 10. How can you tell the difference between break and continue?

# break we use when we got the value by program and wanted to stop the program . 
# continue we use when when we get the value but it didn't statisfy our condition then by using continue we can use program again and again 

# 11. In a for loop, what is the difference between range(10), range(0, 10), and range(0, 10, 1)?

# in genral range(10) , range(0,10)  and range(0,10,1) those give same value but in range(10) we give just upper bound ,
# in range(0 ,10 ) we give lower bound as well as upper bound , 
# in range(0,10,1) we give lower bound , upper bound and we give jump between numbers 

# In[ ]:


12. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent
program that prints the numbers 1 to 10 using a while loop.


# In[54]:


for i in range(1 , 11):
    print(i)


# In[51]:


while True:
    for i in range(1,11):
        print(i)
    break


# 13. If you had a function named bacon() inside a module named spam, how would you call it after
# importing spam?

# import spam as sp
# sp.bacon()

# In[ ]:




