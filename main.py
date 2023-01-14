"""
Created on Sat Aug 20 13:02:35 2022

@author: Joe Souaid

Presented to Tech Lead and Instructor Charbel Daoud
"""


#this project is about writing a program that simulates a Lab Printing System Priority Queue 
#that consists of a login form, with 2 types of users, Admin, and User.
#There are 2 functions list that can be displayed as a window after login, one for the User and one for The Admin

#The login Form is made using Tkinter:
#Functions Used for Tkinter:
#   login(): It is responsible for taking the input of the login window and then calling the second window either the Admin window or the User window
#   admin(): It displays the admin window, which includes a list of functions name that the admin can call
#   user() : It displays the user window, which includes a list of functions name that the user can call
#   userList() : It takes the selection number from the user window and executes the corresponding function   #O(n) n, being the highest n of the functions
#   adminList(): It takes the selection number from the admin window and executes the corresponding function  #O(x) x, being from the function exitUser()


#The queue is made from a LinkedList, the  LinkedList is made from nodes, these Nodes are made of constructor with a variable next and an object Job to store 
#the job information for each Node

#Class Job is formed of a constructor a string format function and the variables: id, usern, date, prio
#The current date is taken from the library datetime at the beginning of the code

#Class LinkedList methods: (part of the code is from Manuealla Class)
#   for Sorting the Linked list using Time:
#       sortedMergeDate(self,a,b)
#       mergeSortDate(self,h)
#       getMiddle(self,head)
#   for Sorting the Linked list using Priority:
#       sortedMergePrio(self,a,v)
#       mergeSortPrio(self,h)
#       getMiddle(self,head)
#   for Sorting the Linked list using id:
#       sortedMergePrio(self,a,b)
#       mergeSortPrio(self,h)
#       getMiddle(self,head)
#   each sorting of a LinkedList takes a time complexity of                      O(nlog(n))
#
#   isEmpty(self): to check if the LinkedList has no nodes                           #O(1)
#   addHead(self,Job) : to add a node from the head of the LinkedList                    #O(1)
#   addTail(self,Job) : to add a node from the tail of the LinkedList                    #O(1)
#   removeHead(self) : to remove a node from the head of the LinkedList              #O(1)
#   removeTail(self) : to remove a node from the tail of the LinkedList              #O(n) n being the size of the LinkedList
#   printElements(self) : to print all the nodes of the LinkedList                   #O(n) n being the elements in the LinkedList
#   nbJobsToday(self)   : to print the number of jobs due by the printer today       #O(n) n being the number of elements in the LinkedList
#   displayAllJobs(self): to print all the jobs of the current day and above ordered  by date   #O(nlog(n)) n being the number of elements in the LinkedList
#   reverse(self)       : to reverse the order of elements in the LinkedList                    #O(n) n being the number of elements in the LinkedList
#   changeJobPriority(self,jobId,newPr): to change the priority of a current job in a node                  #O(n) n being the number of elements in the LinkedList
#   removeJob(self,jobId)        : to remove a current node from the LinkedList                       #O(n) n being the number of elements in the LinkedList


#Class Queue is made from a constructor with a LinkedList object and a list of methods:
#   isEmptyQueue(self): to check if the LinkedList object is empty                   #O(1)
#   enqueue(self, item)     : to add a Node from the tail of the Linked list               #O(1)
#   dequeue(self)     : to remove a Node from the head of the Linked list. I made it this way because it takes O(1) to remove the head while O(n) to remove the tail


#Other functions:
#   printListDate(head): Used in function displayAllJobs() to print the elements of the sorted LinkedList by date                                          #O(n) n being the number of elements in the LinkedList of Queue  
#   printListPrio(queue2): Used in function todayRun to print the elements of the sorted LinkedList by priority and dequeue them one by one                #O(m) m being the number of queue2 LinkedList nodes
#   todayRun(queue)    : to sort the LinkedList and dequeue the current day jobs by priority                                                               #O(nlog(n)) #n being the size of the LinkedList of queue
#   addJobAd  ()   : called by the adminList() and allow the admin to add a user by entering the username and priority                                 #O(n) n being the number of input of the user until the conditions are met
#   addJobUser  (username,date,priority = 0) : called by the userList() and automatically add the login username of the user to a new job with the current date and priority 0   #O(1)
#   exitAd(): to exit the program when the admin wants                                                                                                 #O(1)
#   exitUser(): to exit the program and save changes when the user wants                                                                               #O(nm) n being  the number of elements in the queue and m the number of bytes to be written
#main code:
#   The current date is taken from the library datetime at the beginning of the code
#   reading the file #O(nm) n being the number of lines and  m being the number of ', '
#   printing the login window


from tkinter import *

#getting current date in format yymmdd
#source: https://phoenixnap.com/kb/get-current-date-time-python
global date
import datetime
e = datetime.datetime.now()
if e.month<10:
    month = "0"+ str(e.month)
else: month = e.month
date = "%s%s%s" % (e.year, month, e.day)




       
    

#Creating a class Job to fit all Jobs info to objects
#The class objects is used in the Class Node        
class Job:
    counter = 0
    def __init__(self,Id,username,priority,date=date ):
        Job.counter +=1
        self.id = Id
        self.usern=username
        self.date=date
        self.prio=priority
    

    
    def __str__(self): 
        return "%s, %s, %s, %s\n" % (self.id, self.usern, self.date, self.prio)    
    


#The Class Node is used as an element and a relation in a linkedlist
class Node:
    def __init__(self, next, Job):

        self.next = next
        self.Job = Job


#A linked list, is a series of Nodes. Linked list is used to enhance the time complexity instead of using a regular  to form a queue
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    
    
    
     #mergeSort source: https://www.geeksforgeeks.org/merge-sort-for-linked-list/
     #Time Complexity: O(n*log n) 
    def sortedMergeDate(self, a, b):
        result = None
          
        # Base cases
        if a == None:
            return b
        if b == None:
            return a
              
        # pick either a or b and recur..
        if a.Job.date <= b.Job.date:
            result = a
            result.next = self.sortedMergeDate(a.next, b)
        else:
            result = b
            result.next = self.sortedMergeDate(a, b.next)
        return result
    
    def sortedMergePrio(self, a, b):
        result = None
          
        # Base cases
        if a == None:
            return b
        if b == None:
            return a
              
        # pick either a or b and recur..
        if int(a.Job.prio) <= int(b.Job.prio):
            result = a
            result.next = self.sortedMergePrio(a.next, b)
        else:
            result = b
            result.next = self.sortedMergePrio(a, b.next)
        return result
    
    def sortedMergeId(self, a, b):
        result = None
          
        # Base cases
        if a == None:
            return b
        if b == None:
            return a
              
        # pick either a or b and recur..
        if a.Job.id <= b.Job.id:
            result = a
            result.next = self.sortedMergeId(a.next, b)
        else:
            result = b
            result.next = self.sortedMergeId(a, b.next)
        return result
      
    def mergeSortDate(self, h):
          
        # Base case if head is None
        if h == None or h.next == None:
            return h
    
        # get the middle of the list 
        middle = self.getMiddle(h)
        nexttomiddle = middle.next
    
        # set the next of middle node to None
        middle.next = None
    
        # Apply mergeSort on left list 
        left = self.mergeSortDate(h)
          
        # Apply mergeSort on right list
        right = self.mergeSortDate(nexttomiddle)
    
        # Merge the left and right lists 
        sortedlist = self.sortedMergeDate(left, right)
        return sortedlist
    
    def mergeSortPrio(self, h):
          
        # Base case if head is None
        if h == None or h.next == None:
            return h
    
        # get the middle of the list 
        middle = self.getMiddle(h)
        nexttomiddle = middle.next
    
        # set the next of middle node to None
        middle.next = None
    
        # Apply mergeSort on left list 
        left = self.mergeSortPrio(h)
          
        # Apply mergeSort on right list
        right = self.mergeSortPrio(nexttomiddle)
    
        # Merge the left and right lists 
        sortedlist = self.sortedMergePrio(left, right)
        
        return sortedlist
    
    def mergeSortId(self, h):
          
        # Base case if head is None
        if h == None or h.next == None:
            return h
    
        # get the middle of the list 
        middle = self.getMiddle(h)
        nexttomiddle = middle.next
    
        # set the next of middle node to None
        middle.next = None
    
        # Apply mergeSort on left list 
        left = self.mergeSortId(h)
          
        # Apply mergeSort on right list
        right = self.mergeSortId(nexttomiddle)
    
        # Merge the left and right lists 
        sortedlist = self.sortedMergeId(left, right)
        
        return sortedlist
      
    # Utility function to get the middle 
    # of the linked list 
    def getMiddle(self, head):
        if (head == None):
            return head
    
        slow = head
        fast = head
    
        while (fast.next != None and 
               fast.next.next != None):
            slow = slow.next
            fast = fast.next.next
              
        return slow
    

    def isEmpty(self):
        # O(1)
        if self.size == 0:
            return True
        else:
            return False

    # add head: takes info, adds a node containing info to the beginning of the list
    def addHead(self, Job):
        #O(1)
        n = Node(None, Job)
        if self.isEmpty():  # the LL is empty
            self.head = n
            self.tail = n
            self.size += 1
        else:  # LL contains elements, I need to add at head
            n.next = self.head
            self.head = n
            self.size += 1

    # add Tail: takes info, add a node containing info to the end of the LL
    # O(1)
    def addTail(self, Job):
        n = Node(None, Job)
        if self.isEmpty():  # the LL is empty
            self.head = n
            self.tail = n
            self.size += 1

        else:  # the LL contains nodes
            self.tail.next = n
            self.tail = n
            self.size += 1

    # remove head: removes the first node in the LL and returns its value
    def removeHead(self):
        #O(1)
        if self.isEmpty():
            return None

        if self.size == 1:  # the LL contains a single node
            temp = self.head
            self.head = None
            self.tail = None
            self.size = 0
            return temp

        else:  #the LL contians more than one element
            temp = self.head
            self.head = self.head.next
            self.size -= 1
            return temp

    # remove tail: removes the last node in the LL and returns its value
    #O(n), n being the size of the linkedList
    def removeTail(self):
        if self.isEmpty():
            return None
        elif self.size == 1:
            value = self.head.car.name
            self.head = None
            self.tail = None
            self.size = 0
            return value
        else:
            value = self.tail.Job.id
            temp = self.head  # 1 jump
            for i in range(self.size - 2):  #O(n)
                temp = temp.next
                print("temp", temp.info)
            temp.next = None
            self.tail = temp
            self.size -= 1
            return value

    
    def printElements(self):
        #O(n), n being the number of elements in the linkedList
        temp = self.head
        while temp != None:
            print(temp.Job, end="")
            temp = temp.next
        print()
    
    def nbJobsToday(self):
        #O(n), n being the number of elements in the linkedList
        countJbs=0
        temp = self.head
        while temp != None:
            if(temp.Job.date == date ):
                countJbs += 1
            temp = temp.next
        print(countJbs)
        
        
    #Display Jobs equal to date or greater
    def displayAllJobs(self):
        #O(n), n being the number of elements in the linkedList
         print("The Jobs of today and the upcomings by date order are:")
         
         queue2 = LinkedList()
         temp =self.head
         while temp != None:
             
             if int(temp.Job.date) >= int(date):
                 
                 queue2.addTail(temp.Job)
                 
             temp=temp.next
         
         
         
         
         #sorting by date
         queue2.head = queue2.mergeSortDate(queue2.head) #O(nlog(n))
         print ("Sorted Linked List is:")
         printListDate(queue2.head)
         #O(nlog(n))
         
         
    #Reverse source: https://www.geeksforgeeks.org/reverse-a-linked-list/     
    def reverse(self):
        prev = None
        current = self.head
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev    
    
    def changeJobPriority(self,jobId,newPr):
        #O(n), n being the number of elements in the linkedList
        temp = self.head
        while temp != None:
            if(temp.Job.id == jobId):
                temp.Job.prio = newPr
            temp = temp.next
            
    def removeJob(self,jobId):
        #O(n), n being the number of elements in the linkedList
        temp = self.head
        temp1 =self.head.next
        while temp1 != None:
            if(temp1.Job.id == jobId):
                temp.next = temp1.next
            temp = temp.next
            temp1 = temp1.next
            
            
            

        
    
class Queue:
    def __init__(self):
        self.elements = LinkedList()

    #O(1)
    def isEmptyQueue(self):
        return self.elements.isEmpty()

    #O(1)
    def enqueue(self, item):
        self.elements.addTail(item)

    #O(1)
    def dequeue(self):
        return self.elements.removeHead()



    
    
def printListDate(head):
    lista=[]
    if head is None:
        print(' ')
        return
    #Looping through the LinkedList
    curr_node = head
    while curr_node:
        listb = ["",""]
        listb[0] = curr_node.Job.id
        listb[1] = curr_node.Job.date
        lista.append(listb)
        curr_node = curr_node.next
    #printing the array of jobs elements that is sorted by date    
    for i in lista:
        print(i)
    print(' ')    
    
def printRemoveListPrio(queue2): 
    queue2.elements.reverse()   #O(m) m being the number of queue2 LinkedList nodes
    #looping through queue2 LinkedList
    
    queue2.elements.printElements() #O(m), m being the number of queue2 LinkedList nodes
    for i in range(queue2.elements.size):  #O(m), m being the number of queue2 LinkedList nodes
        queue2.dequeue()        #O(1)
 #O(m) m being the number of queue2 LinkedList nodes  

    
def todayRun(queue):    
    
    #I order my queue by date than I remove the current date and put it in queue2, queue2 is than ordered by prio than it's dequeued
    
    #order queue by date
    queue.elements.head = queue.elements.mergeSortDate(queue.elements.head) #O(nlog(n))
    
    break1 = 0
    queue2 = Queue()

    
    ##Looping queue LinkedList
    temp = queue.elements.head
    tempTail = queue.elements.head
    tempHead = queue.elements.head
    while temp != None:                                                      #O(n), n being the size of the queue
        if(temp.Job.date != date and break1 == 0):
            temptail = temp
            #the place where I would start skipping Nodes
            
        
            
        if(temp.Job.date == date): #node date is equal to current date
            break1 = 1
            queue2.enqueue(temp.Job) #the skipped nodes are stored in another queue2       #O(1)
            tempHead = temp.next
            #the place where I would start not to skip Nodes 
        temp =  temp.next
        
    temptail.next = tempHead
    
    #order queue by Id 
    queue.elements.head = queue.elements.mergeSortId(queue.elements.head)     #O(nlog(n))

        
    #reversing the dates now so i can have an ordered by date and priority later, it will again be reversed wwith priority in the function printRemoveListPrio 
    queue2.elements.reverse()                                                 #O(n)
    #order queue2 by prio
    queue2.elements.head = queue2.elements.mergeSortPrio(queue2.elements.head) #O(nlogn)
    print ("Sorted Linked List is:")

    printRemoveListPrio(queue2)    #O(m) m being the number of queue2 LinkedList nodes
#O(nlog(n)) #n being the size of the LinkedList of queue
    


#add job functions for the user and admin below


def addJobAd():
    newUserName=""
    while newUserName == "":                              #O(n), n being the number of tries made by the user to input a correct form
        newUserName = input("Please enter the username: ")#O(1)
    newPrio =""                                           #O(1)
    while newPrio =="":                                   #O(m), n being the number of tries made by the user to input a correct form
        newPrio     = input("Please enter the priority: ")#O(1)
    newUserId = "Job" + str(int(jobIdmax) + Job.counter)  #O(1)
    Jobss.enqueue(Job(newUserId,newUserName,newPrio))     #O(1)
#if O(x) x being n or m, with  n>m then it's O(n) else if m>n it's O(m)


def addJobUser(username,date,priority = 0):
    newUserId = "Job" + str(int(jobIdmax) + Job.counter) #O(1)
    Jobss.enqueue(Job(newUserId,username,priority,date)) #O(1)
 #O(1) 
    




#exit functions for the admin and user below

import sys
def exitAd():
    sys.exit() 
#O(1)

    
def exitUser():
    
    #Cleaning the File
    file_to_delete = open("jobs.txt",'w') #O(1)
    file_to_delete.close()                #O(1)
    
    myFile = open("jobs.txt", "a")        #O(1)
    
    #Looping the LinkedList
    temp = Jobss.elements.head          #O(1)
    while temp != None:                   #(n), n  being the number of elements in queue Jobss
            strr = str(temp.Job)          #O(1)
            #writing the Node to the file
            myFile.write(strr)            #O(m), where n is the number of bytes to be written.
            temp = temp.next              #O(1)

    
    
    myFile.close()                        #O(1)
    sys.exit()                            #O(1)
#if n>m then it's O(n) else if m>n it's O(m)
    










#The Code below is related to the part of the User experience 








    

#this is the adminList function that takes a selection from the admin window and executes the corresponding function
def adminList():
    global selection
    value = selection.get()
    
    
    if value == '1':
        Jobss.elements.nbJobsToday()        #O(n)
        print("\n")
    elif value == '2':
        addJobAd()                          #O(n)
        print("User successfully saved")
        print("\n")
    elif value == '3':
        Jobss.elements.displayAllJobs()    #O(n)
        print("\n")
    elif value == '4':
        changeJobid=""
        while changeJobid == "":
            changeJobid = input("please enter the JobId to change its priority: ")
        changeJobprio=""
        while changeJobprio == "":
            changeJobprio = input("please enter the new Job Prio: ")
        Jobss.elements.changeJobPriority(changeJobid, changeJobprio)                #O(n)
        print("\n")
    elif value == '5':
        removeId = ""
        while removeId == "":
            removeId = input("please enter the JobId to remove it: ")
        Jobss.elements.removeJob(removeId)                                          #O(n)
        print("\n")
    elif value == '6':
        todayRun(Jobss)                                                             #O(n)
        print("\n")
    elif value == '7':
        exitAd()                                                                    #O(1)
    elif value == '8':
        Jobss.elements.printElements()                                              #O(n)
        print("\n")
        
#O(n) n, being the highest n of the functions






#this is the userList function that takes a selection from the user window and executes the corresponding function      
def userList():
    global selection
    value = selection.get()
    
    
    if value == '1':
        newuser= username.get()
        addJobUser(newuser, date)           #O(1)
        print("User successfully saved")
        
    elif value == '2':
        exitUser()                          #O(x)
    #O(x) x, being from the function exitUser()
    
    
    elif value == '3':
         Jobss.elements.printElements()      
         print("\n")
 





#top level idea from https://www.geeksforgeeks.org/python-tkinter-toplevel-widget/
#this is the user window
def user():
         global selection
         selection = StringVar()
         
         display = Toplevel()
         display.title("USER")
         display.geometry("300x250")
         label = Label(display,width="300", text ="Welcome User", bg="orange",fg="white")
         label.pack()

         label = Label(display,width="300", text ="Please Select a Number", bg="white",fg="black")
         label.pack()
       
         label = Label(display,width="300", text ="\n1.Add a new Job \n\
 2.Exit  \n\
  ", bg="orange",fg="white")
       
         label.pack()
         Entry(display, textvariable=selection).place(x=20,y=180, width = "260")
        
         
         Button(display, text="submit", width=10, height=1, bg="orange", command = userList).place(x=105,y=210)
         print("\n",selection.get())
         display.mainloop        
         
         
         
#top level idea from https://www.geeksforgeeks.org/python-tkinter-toplevel-widget/       
#this is the admin window
def admin():
         global selection
         selection = StringVar()
         
         
         
         display = Toplevel()
         display.title("ADMIN")
         display.geometry("300x250")
         label = Label(display,width="300", text ="Welcome Admin", bg="orange",fg="white")
         label.pack()

         label = Label(display,width="300", text ="Please Select a Number", bg="white",fg="black")
         label.pack()
       
         label = Label(display,width="300", text ="1.Display number of Jobs due Today\n\
 2.Add a Job \n\
 3.Display all Jobs (Today and after)\n\
 4.Change Job's Priority \n\
 5.Remove Job\n\
 6.Run Printer \n\
 7.Exit \n\
 8.Display All Time Jobs  ", bg="orange",fg="white")
       
         label.pack()
         
         # Label(self, text="Selection: ").place(x=20,y=180)
         Entry(display, textvariable=selection).place(x=20,y=180, width = "260")
         #selection = entry.get()
         
         Button(display, text="submit", width=10, height=1, bg="orange", command = adminList).place(x=105,y=210)
         print("\n",selection.get())
         display.mainloop  





#login function source https://www.krazyprogrammer.com/2020/11/create-window-login-form-in-python.html
incorrect = 0
def login():
    #getting form data
    # Admin(login_screen)
    # User(login_screen)
    global incorrect
    uname=username.get()
    pwd=password.get()
    
    
    #applying empty validation
    if uname=='' :
        message.set("fill the Usernamed!!!")
    else:
      if uname=="admin" and pwd=="admin123123":
       # NewWindow(login_screen)
       message.set("Login success")
       admin()
       
    
      elif uname and pwd=="":
       message.set("Login success")
       user()
       
      else:
       if(incorrect<3):
         incorrect +=1
         message.set("Wrong username or password! \nIncorrect: "+ str(incorrect))
         
       else:
         message.set("To many wrong credentials \nfrom now on \nyou will be out")
         incorrect +=1
         if incorrect > 4:
          sys.exit()



        
        
        


#The code below is for:   
#reading the file to get the last JobId   
#adding the txt file Jobs to a queue   



file1 = open('jobs.txt', 'r')
Jobss = Queue()
list = []
# Using for loop to read each line by line instead of the whole file at once, incase the file is to big and doesnt fit in a list
for line in file1:  #O(n) n being the number of lines

    line = line.strip()
    list = line.split(', ') #O(m) m being the number of ', '
    
    jobId = list[0].split('b')
    jobIdmax = jobId[1]
    
    Jobss.enqueue( (Job(list[0],list[1],list[3],list[2]))) #O(1)
    
Job.counter = 1    
file1.close() 
  
#O(nm)









# the Code below is the the lanching and creation of the login window



login_screen = Tk()
#Setting title of screen
login_screen.title("Login Form")
#setting height and width of screen
login_screen.geometry("300x250")
#declaring variable

global  message
global username
global password

username = StringVar()
password = StringVar()
message=StringVar()
#Creating layout of login form
Label(login_screen,width="300", text="Please enter details below", bg="orange",fg="white").pack()
#Username Label
Label(login_screen, text="Username * ").place(x=20,y=40)
#Username textbox

Entry(login_screen, textvariable=username).place(x=90,y=42)
#Password Label
Label(login_screen, text="Password * ").place(x=20,y=80)
#Password textbox
Entry(login_screen, textvariable=password ,show="*").place(x=90,y=82)
#Label for displaying login status[success/failed]

#Login button
Button(login_screen, text="Login", width=10, height=1, bg="orange",command=login).place(x=105,y=160)
Label(login_screen, text="" ,textvariable=message).place(x=95,y=100)
login_screen.mainloop()


