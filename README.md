# README #

Presented set of simple programming training tasks in this repository is created by [tevtonez](mailto:tevtonez@gmail.com) for my own training writing programs in Python. You are welcomed to try your skills solving these tasks.
If you got stuck, you can find the answers in this repository.

I've moved this repo from my private repository but files have date stamps of creation.


### What is this repository for? ###

* This repository contains the simple programming training tasks for beginners who needs to get used to common functions and methods in the programming language they're learning.
* Version 0.0.1


## The list of tasks ##
### Task 1 ###
### Lists comparator ###
Create a function that takes one argument 'lists_length' which is equals 10 by default, creates 2 lists with length = 'lists_length', then shuffles list items in both lists and then compares list items one by one finding matching numbers and then prints number of occurred coincidences and numbers that matched.


*EXAMPLE*

For lists

a = [2, 0, 3, 4, 1, 7, 5, 6, 9, 8]

b = [7, 5, 2, 9, 1, 0, 3, 6, 4, 8]



output should be:
3 match(es) for number(s) 1, 6, 8


### Task 2 ###
### Lists comparator  OOP ###
Create a function that takes one argument 'litsts_length' which is equals
10 by default, creates 2 list with length = 'litsts_length', then shuffles list
items in both lists and then compares list items one by one finding matching numbers
and then prints number of occurred coincidences and numbers that matched.

USE OOP this time!
Make sure it works for uneven lists!

*EXAMPLE*

For lists

a = [2, 0, 3, 4, 1, 7, 5, 6, 9, 8]

b = [7, 5, 2, 9, 1, 0, 3, 6, 4, 8]

output should be:

3 match(es) for number(s) 1, 6, 8


### Task 3 ###
### Poll script + i/o ###
Create a script that asks user a question with 3 possible answers: "Yes", "No", "Maybe".
The results should be written in a log file with the date and time of line creation.
Once log file contains 10 or more lines script should show total number of voted users and percentage for every answer.
Do not use modules math or course or similar. Write everything you need manually


*OUTPUT EXAMPLE*

Question: Do you think it's a good script?

YES - 30%

NO - 20%

MAYBE - 50%

You may want to create a graphic representation of percentage using some UTF symbols (eg
u25A8 and u25A2)


### Task 4 ###
### Z-day ###
Write a function that takes three arguments:
- Number of citizens in the city
- The disease spreading speed from one person to another (in hours)
- The number of people that get infected from the one infected person

Then function should calculate in which time the whole population of the city will be infected.

For example, we have a city with 300,000 people and one infected person (which is called "patient zero") at the beginning.
Let's say the spreading speed of this disease is 24 hours and the number of people that will be infected by contacting the "patient zero" in 24 equals 2. Then each of the infected people will infect 2 more people in 24 hours and so one.
The function should say in how many hours the whole city will fall if no counter measures are taken.

*OUTPUT EXAMPLE*
"The city with the population of 300,000 people will be 100% infected in 96 hours if disease spreading speed is 2 persons in 24 hours"


### Task 5 ###
### Displaying x,y matrix ###
Create a function that takes three arguments 'x' (int), 'y' (int) and 'char' (str) and prints a play field 'x'-width, 'y'-high filled with 'char's

*EXAMPLE*
x = 4
y = 3
char = o

output:
```
oooo
oooo
oooo
```

### Task 6 ###
### Displaying a 'player' in x,y position in the matrix ###
Using function from the task 5 create a play field. Then create a function that places a "player" (any character that is different from the field's background) in a x, y position.
Note: the top left matrix cell has (1, 1) coordinates.

*EXAMPLE*
x = 2
y = 2
char = x

Possible output:
```
oooo
oxoo
oooo
```


### Task 7 ###
### Simple area calculator ###
Write area calculator function that takes number of arguments (1 arg. for circle, 2 for square or rectangle, 3 for triangle, 4 for trapeze), automatically detects which equation should it use and then calculates and shows the surface area result.

*Possible output:*
```
=========================
| AREA CALCULATOR v.0.1 |
=========================

For CIRCLE area enter radius length and hit enter.
For SQUARE/RECTANGLE area enter high and length separated by comma.
For TRIANGLE area enter 3 lengths of its sides separated by commas.
For TRAPEZE area enter 4 lengths of its sides separated by commas.
```
Your input: ```5, 4```

The area of RECTANGLE is 20 square units.


### Task 8 ###
### Tiles calculator ###
Write area calculator function that ask a user to provide the size of an area that should be covered with ceramic tiles and the size of a ceramic tile and then calculate the number of tiles needed to cover the area. Then prints the number.

*Possible output:*
```
=========================
| Tiles CALCULATOR v.0.1 |
=========================
Enter the area size in square units:
userinput - 20

Now provide the length of a tile sides in units comma separated:
userinput - 0.1, 0.1

You'll need 200 tiles to cover 20 square units area.

```

### Task 9 ###
### The parser  ###
TASK
Write a HTML parser using HTMLParser and urllib.request that parses the content from a given website and prints the content of all headers on the page and the URLs of all <a> tags.


*Possible output:*
```
=========================
website parser v.1
=========================

Enter website ULR (with http:// part):
http://razrisovki.ru/

The headers on the page are:
Hello World
How to learn Python
Contact me

The URLs on the page are:
http://google.com
http://gmail.com
http://yahoo.com
```

### Task 10 ###
### The Company and its workers  ###
TASK
Create a class 'Company' that contains objects of 2 classes of workers that derived from parent class 'Worker': 'Manager' and 'Engineer'.
Workers should have fields: 'name', 'job_title' 'office_number', 'project'.
'Company' class should have methods: 'ShowManagers', 'ShowEngineers', 'ShowAll'. These methods should print the lists of related objects.



### Task 11 ###
### Math exercise generator  ###
TASK
Write a script that generates text file with math exercises that contain random numbers.
The exercises should contain addition, subtraction and multiplication.
The exercises should be put into txt file in 3 columns: first col - addition, second - subtraction, third - multiplication.

The addition and subtraction exercises should look like:
[number from 1 to 99] + [number from 1 to 99] =
[number from 1 to 99] - [number from 1 to 99] =

The multiplication exercises should operate with numbers
[number from 1 to 99] * [number from 1 to 9] =
[number from 1 to 9] * [number from 1 to 99] =


EXTRAS:

1. generate a file with answers

2. avoid negative numbers in subtraction results


### Task 12 ###
### Work with paths  ###
TASK(s)

1. print full path of your working directory.
2. write a script that creates a directory 'test1' in your working directory. Make script to ignore if the directory exists.
3. write a script that creates a sub-directory in 'test1'. Name it 'test2'. Make script to ignore if the directory exists.
4. write a script that creates 5 files in sub-directory 'test1'. Name files test-1-[n].txt , where [n] is the number from 1 to 5.
5. write a script that prints the number of all items in 'test1' directory.
6. write a script that iterates through files only and changes their names to test-[n].txt , where [n] is the number from 1 to 5. Also print new names.
7. write a script that deletes all directories and files you've created during previous steps. Be careful when working on this task!

### Task 13 ###
### Name generator  ###
TASK
Write a function that asks user for desired name length and for quantity of names to be generated.
Print out the names at the end.

### Task 14 ###
### Work with JSON  ###
TASK
Write a function that creates a JSON file from a given dictionary that contains writers' names and their birthdays.
Then write another function that opens a JSON file and prints out all key/values pairs.

*Possible output:*
```
C. S. Lewis November 29, 1898
Marion Zimmer Bradley June 3, 1930
George Orwell June 25, 1903
J. R. R. Tolkien January 3, 1892
Ursula K. Le Guin October 21, 1929
Ray Bradbury August 22, 1920
Jules Verne February 8, 1828
Terry Pratchett April 28, 1948
Anne McCaffrey April 1, 1926
Roger Zelazny May 13, 1937
```

### Task 14 ###
### Work with JSON  ###
TASK
Update the code from TASK 14 so user would be able to add new pair 'Name' : 'birthday date'
and add it to existing JSON file.


### Who do I talk to? ###
* Repo [owner or admin](mailto:tevtonez@gmail.com)

