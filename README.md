This project was presented as a Midterm project for the Foundation of computer science bootcamp made by
SE Factory.
This project is about creating a program that simulates a lab printing system priority queue. The program features a login form that allows two types of users, Admin and User, to access different functions. The login form is created using Tkinter and has functions such as login(), admin(), and user() that handle the user input and display the respective windows for the Admin and User. The program also utilizes a queue, which is implemented using a linked list data structure. The linked list is made up of nodes that contain a "next" variable and a "Job" object to store information about the job. The "Job" class is composed of a constructor, a string format function, and variables for id, usern, date, and prio. The program also includes several sorting functions for the linked list, such as sortedMergeDate(), mergeSortDate(), and getMiddle(), which sort the list by date, priority, and id respectively. Each sorting function has a time complexity of O(nlog(n)). The linked list class also has several other methods such as isEmpty(), addHead(), addTail(), removeHead(), removeTail(), and printElements(), which have time complexities of O(1) and O(n) respectively. The "Queue" class is made up of a constructor with a linked list object and several methods such as isEmptyQueue(), enqueue(), and dequeue() to add and remove elements from the queue with time complexities of O(1).

ADMIN LOGIN:
username: admin
Paswword: admin123123

User login:
any username different than admin, with an empty password
