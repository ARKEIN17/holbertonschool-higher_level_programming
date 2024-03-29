# 0x13. JavaScript - Objects, Scopes and Closures
## Details
 By: Guillaume Weight: 1Project will startAug 16, 2022 12:00 AM, must end byAug 17, 2022 12:00 AMwas released atAug 16, 2022 12:00 PM An auto review will be launched at the deadline## Resources
Read or watch :
* [JavaScript object basics](https://intranet.hbtn.io/rltoken/OJ4pU6uHwfCrAclbZsk_Hg) 

* [Object-oriented JavaScript](https://intranet.hbtn.io/rltoken/vLr7QS9h4-nGFKVn5vsrvQ) 
 (read all examples!)
* [Class - ES6](https://intranet.hbtn.io/rltoken/zMWxOmGWEsOCldCKeDswCA) 

* [super - ES6](https://intranet.hbtn.io/rltoken/DTMKogwFYEgUnpLrNvTcfQ) 

* [extends - ES6](https://intranet.hbtn.io/rltoken/fh2JHfNNa-HLnmfSdOo9TA) 

* [Object prototypes](https://intranet.hbtn.io/rltoken/lrlwnQMM82RimJJcfLao5w) 

* [Inheritance in JavaScript](https://intranet.hbtn.io/rltoken/vLr7QS9h4-nGFKVn5vsrvQ) 

* [Closures](https://intranet.hbtn.io/rltoken/qDa7F8060Jlhe3DZZitY4A) 

* [this/self](https://intranet.hbtn.io/rltoken/ockP7FQKKmTRvfeAHw-XSw) 

* [Modern JS](https://intranet.hbtn.io/rltoken/22mdHf9KeFhRQrLP-e1hPw) 

## Learning Objectives
At the end of this project, you are expected to be able to  [explain to anyone](https://intranet.hbtn.io/rltoken/wrvgHnS5IYuzEVUUixnzJQ) 
 ,  without the help of Google :
### General
* Why JavaScript programming is amazing
* How to create an object in JavaScript
* What  ` this `  means
* What  ` undefined `  means 
* Why the variable type and scope is important
* What is a closure
* What is a prototype
* How to inherit an object from another
## Requirements
### General
* Allowed editors:  ` vi ` ,  ` vim ` ,  ` emacs ` 
* All your files will be interpreted on Ubuntu 20.04 LTS using node (version 14.x)
* All your files should end with a new line
* The first line of all your files should be exactly  ` #!/usr/bin/node ` 
* A  ` README.md `  file, at the root of the folder of the project, is mandatory
* Your code should be  ` semistandard `  compliant. [Rules of Standard](https://intranet.hbtn.io/rltoken/LzTXpt_3kwzaaEQFTvq2UQ) 
 + [semicolons on top](https://intranet.hbtn.io/rltoken/_6jQeRtew2qeam8OzERXPw) 
. Also as reference: [AirBnB style](https://intranet.hbtn.io/rltoken/D8wEPwvtilCjNqotmoSruw) 

* All your files must be executable
* The length of your files will be tested using  ` wc ` 
* You are not allowed to use  ` var ` 
## More Info
### Install Node 14
 ` $ curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
$ sudo apt-get install -y nodejs
 ` ### Install semi-standard
[Documentation](https://intranet.hbtn.io/rltoken/_6jQeRtew2qeam8OzERXPw) 

 ` $ sudo npm install semistandard --global
 ` ### Quiz questions
Great!          You've completed the quiz successfully! Keep going!          (Show quiz)#### 
        
        Question #0
    
 Quiz question Body What is the output of this code?
 ` function myFunction(a) {
    console.log(a);
}

myFunction(12);
 `  Quiz question Answers * 1

* 12

* 2

 Quiz question Tips #### 
        
        Question #1
    
 Quiz question Body What is the output of this code?
 ` const number = 12;
function myFunction(a) {
    console.log(a);
}

myFunction(number);
 `  Quiz question Answers * 1

* 12

* 2

 Quiz question Tips #### 
        
        Question #2
    
 Quiz question Body What is the output of this code?
 ` function myFunction(a) {
    console.log(a);
}

const number = 12;
myFunction(number);
 `  Quiz question Answers * 1

* 12

* 2

 Quiz question Tips #### 
        
        Question #3
    
 Quiz question Body What is the output of this code?
 ` const a = 12;

function myFunction(a) {
    console.log(a);
}

myFunction(89);
 `  Quiz question Answers * 1

* 12

* 2

* 89

 Quiz question Tips #### 
        
        Question #4
    
 Quiz question Body What is the output of this code?
 ` function myFunction(a) {
    console.log(a);
}

const a = 12;
myFunction(89);
 `  Quiz question Answers * 1

* 12

* 2

* 89

 Quiz question Tips #### 
        
        Question #5
    
 Quiz question Body What is the output of this code?
 ` const b = 79;
function myFunction(a) {
    console.log(a + b);
}

myFunction(10);
 `  Quiz question Answers * 89

* 10

* 79

 Quiz question Tips #### 
        
        Question #6
    
 Quiz question Body What is the output of this code?
 ` function myFunction(a) {
    console.log(a + b);
}

const b = 79;
myFunction(10);
 `  Quiz question Answers * 10

* 79

* 89

 Quiz question Tips #### 
        
        Question #7
    
 Quiz question Body What is the output of this code?
```bash
let b = 1;

function myFunction(a) {
    console.log(a + b);
    b = a;
}

myFunction(3);
myFunction(4);

```
 Quiz question Answers * 3, 4

* 4, 7

* 3, 7

* 4, 3

 Quiz question Tips ## Tasks
### 0. Rectangle #0
          mandatory         Progress vs Score  Task Body Write an empty class   ` Rectangle `   that defines a rectangle:
* You must use the  ` class `  notation for defining your class 
```bash
guillaume@ubuntu:~/0x13$ cat 0-main.js
#!/usr/bin/node
const Rectangle = require('./0-rectangle');

const r1 = new Rectangle();
console.log(r1);
console.log(r1.constructor);

guillaume@ubuntu:~/0x13$ ./0-main.js
Rectangle {}
[Class: Rectangle]
guillaume@ubuntu:~/0x13$ 

```
 Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-higher_level_programming ` 
* Directory:  ` 0x13-javascript_objects_scopes_closures ` 
* File:  ` 0-rectangle.js ` 
 Self-paced manual review  Panel footer - Controls 
### 1. Rectangle #1
          mandatory         Progress vs Score  Task Body Write a class   ` Rectangle `   that defines a rectangle:
* You must use the  ` class `  notation for defining your class
* The constructor must take 2 arguments  ` w `  and  ` h ` 
* Initialize the instance attribute  ` width `  with the value of  ` w ` 
* Initialize the instance attribute  ` height `  with the value of  ` h ` 
```bash
guillaume@ubuntu:~/0x13$ cat 1-main.js
#!/usr/bin/node
const Rectangle = require('./1-rectangle');

const r1 = new Rectangle(2, 3);
console.log(r1);
console.log(r1.width);
console.log(r1.height);

const r2 = new Rectangle(2, -3);
console.log(r2);
console.log(r2.width);
console.log(r2.height);

const r3 = new Rectangle(2);
console.log(r3);
console.log(r3.width);
console.log(r3.height);

guillaume@ubuntu:~/0x13$ ./1-main.js
Rectangle { width: 2, height: 3 }
2
3
Rectangle { width: 2, height: -3 }
2
-3
Rectangle { width: 2, height: undefined }
2
undefined
guillaume@ubuntu:~/0x13$ 

```
 Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-higher_level_programming ` 
* Directory:  ` 0x13-javascript_objects_scopes_closures ` 
* File:  ` 1-rectangle.js ` 
 Self-paced manual review  Panel footer - Controls 
### 2. Rectangle #2
          mandatory         Progress vs Score  Task Body Write a class   ` Rectangle `   that defines a rectangle:
* You must use the  ` class `  notation for defining your class
* The constructor must take 2 arguments  ` w `  and  ` h ` 
* Initialize the instance attribute  ` width `  with the value of  ` w ` 
* Initialize the instance attribute  ` height `  with the value of  ` h ` 
* If  ` w `  or  ` h `  is equal to 0 or not a positive integer, create an empty object
```bash
guillaume@ubuntu:~/0x13$ cat 2-main.js
#!/usr/bin/node
const Rectangle = require('./2-rectangle');

const r1 = new Rectangle(2, 3);
console.log(r1);
console.log(r1.width);
console.log(r1.height);

const r2 = new Rectangle(2, -3);
console.log(r2);
console.log(r2.width);
console.log(r2.height);

const r3 = new Rectangle(2);
console.log(r3);
console.log(r3.width);
console.log(r3.height);

const r4 = new Rectangle(2, 0);
console.log(r4);
console.log(r4.width);
console.log(r4.height);

guillaume@ubuntu:~/0x13$ ./2-main.js
Rectangle { width: 2, height: 3 }
2
3
Rectangle {}
undefined
undefined
Rectangle {}
undefined
undefined
Rectangle {}
undefined
undefined
guillaume@ubuntu:~/0x13$ 

```
 Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-higher_level_programming ` 
* Directory:  ` 0x13-javascript_objects_scopes_closures ` 
* File:  ` 2-rectangle.js ` 
 Self-paced manual review  Panel footer - Controls 
### 3. Rectangle #3
          mandatory         Progress vs Score  Task Body Write a class   ` Rectangle `   that defines a rectangle:
* You must use the  ` class `  notation for defining your class
* The constructor must take 2 arguments:  ` w `  and  ` h ` 
* Initialize the instance attribute  ` width `  with the value of  ` w ` 
* Initialize the instance attribute  ` height `  with the value of  ` h ` 
* If  ` w `  or  ` h `  is equal to 0 or not a positive integer, create an empty object
* Create an instance method called  ` print() `  that prints the rectangle using the character  ` X ` 
```bash
guillaume@ubuntu:~/0x13$ cat 3-main.js
#!/usr/bin/node
const Rectangle = require('./3-rectangle');

const r1 = new Rectangle(2, 3);
r1.print();

const r2 = new Rectangle(10, 5);
r2.print();

guillaume@ubuntu:~/0x13$ ./3-main.js
XX
XX
XX
XXXXXXXXXX
XXXXXXXXXX
XXXXXXXXXX
XXXXXXXXXX
XXXXXXXXXX
guillaume@ubuntu:~/0x13$ 

```
 Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-higher_level_programming ` 
* Directory:  ` 0x13-javascript_objects_scopes_closures ` 
* File:  ` 3-rectangle.js ` 
 Self-paced manual review  Panel footer - Controls 
### 4. Rectangle #4
          mandatory         Progress vs Score  Task Body Write a class   ` Rectangle `   that defines a rectangle:
* You must use the  ` class `  notation for defining your class
* The constructor must take 2 arguments:  ` w `  and  ` h ` 
* Initialize the instance attribute  ` width `  with the value of  ` w ` 
* Initialize the instance attribute  ` height `  with the value of  ` h ` 
* If  ` w `  or  ` h `  is equal to 0 or not a positive integer, create an empty object
* Create an instance method called  ` print() `  that prints the rectangle using the character  ` X ` 
* Create an instance method called  ` rotate() `  that exchanges the  ` width `  and the  ` height `  of the rectangle
* Create an instance method called  ` double() `  that multiples the  ` width `  and the  ` height `  of the rectangle by 2
```bash
guillaume@ubuntu:~/0x13$ cat 4-main.js
#!/usr/bin/node
const Rectangle = require('./4-rectangle');

const r1 = new Rectangle(2, 3);
console.log('Normal:');
r1.print();

console.log('Double:');
r1.double();
r1.print();

console.log('Rotate:');
r1.rotate();
r1.print();

guillaume@ubuntu:~/0x13$ ./4-main.js
Normal:
XX
XX
XX
Double:
XXXX
XXXX
XXXX
XXXX
XXXX
XXXX
Rotate:
XXXXXX
XXXXXX
XXXXXX
XXXXXX
guillaume@ubuntu:~/0x13$ 

```
 Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-higher_level_programming ` 
* Directory:  ` 0x13-javascript_objects_scopes_closures ` 
* File:  ` 4-rectangle.js ` 
 Self-paced manual review  Panel footer - Controls 
### 5. Square #0
          mandatory         Progress vs Score  Task Body Write a class   ` Square `   that defines a square and inherits from   ` Rectangle `   of   ` 4-rectangle.js `  :
* You must use the  ` class `  notation for defining your class and  ` extends ` 
* The constructor must take 1 argument:  ` size ` 
* The constructor of  ` Rectangle `  must be called (by using  ` super() ` )
```bash
guillaume@ubuntu:~/0x13$ cat 5-main.js
#!/usr/bin/node
const Square = require('./5-square');

const s1 = new Square(4);
s1.print();
s1.double();
s1.print();

guillaume@ubuntu:~/0x13$ ./5-main.js
XXXX
XXXX
XXXX
XXXX
XXXXXXXX
XXXXXXXX
XXXXXXXX
XXXXXXXX
XXXXXXXX
XXXXXXXX
XXXXXXXX
XXXXXXXX
guillaume@ubuntu:~/0x13$ 

```
 Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-higher_level_programming ` 
* Directory:  ` 0x13-javascript_objects_scopes_closures ` 
* File:  ` 5-square.js ` 
 Self-paced manual review  Panel footer - Controls 
### 6. Square #1
          mandatory         Progress vs Score  Task Body Write a class   ` Square `   that defines a square and inherits from   ` Rectangle `   of   ` 4-rectangle.js `  :
* You must use the  ` class `  notation for defining your class and  ` extends ` 
* Create an instance method called  ` charPrint(c) `  that prints the rectangle using the character  ` c ` * If  ` c `  is  ` undefined ` , use the character  ` X ` 

```bash
guillaume@ubuntu:~/0x13$ cat 6-main.js
#!/usr/bin/node
const Square = require('./6-square');

const s1 = new Square(4);
s1.charPrint();

s1.charPrint('C');

guillaume@ubuntu:~/0x13$ ./6-main.js
XXXX
XXXX
XXXX
XXXX
CCCC
CCCC
CCCC
CCCC
guillaume@ubuntu:~/0x13$ 

```
 Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-higher_level_programming ` 
* Directory:  ` 0x13-javascript_objects_scopes_closures ` 
* File:  ` 6-square.js ` 
 Self-paced manual review  Panel footer - Controls 
### 7. Occurrences
          mandatory         Progress vs Score  Task Body Write a function that returns the number of occurrences in a list:
* Prototype:  ` exports.nbOccurences = function (list, searchElement) ` 
```bash
guillaume@ubuntu:~/0x13$ cat 7-main.js
#!/usr/bin/node
const nbOccurences = require('./7-occurrences').nbOccurences;

console.log(nbOccurences([1, 2, 3, 4, 5, 6], 3));
console.log(nbOccurences([3, 2, 3, 4, 5, 3, 3], 3));
console.log(nbOccurences(["S", 12, "c", "S", "School", 8], "S"));

guillaume@ubuntu:~/0x13$ ./7-main.js
1
4
2
guillaume@ubuntu:~/0x13$ 

```
 Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-higher_level_programming ` 
* Directory:  ` 0x13-javascript_objects_scopes_closures ` 
* File:  ` 7-occurrences.js ` 
 Self-paced manual review  Panel footer - Controls 
### 8. Esrever
          mandatory         Progress vs Score  Task Body Write a function that returns the reversed version of a list:
* Prototype:  ` exports.esrever = function (list) ` 
* You are not allow to use the built-in method  ` reverse ` 
```bash
guillaume@ubuntu:~/0x13$ cat 8-main.js
#!/usr/bin/node
const esrever = require('./8-esrever').esrever;

console.log(esrever([1, 2, 3, 4, 5]));
console.log(esrever(["School", 89, { id: 12 }, "String"]));

guillaume@ubuntu:~/0x13$ ./8-main.js
[ 5, 4, 3, 2, 1 ]
[ 'String', { id: 12 }, 89, 'School' ]
guillaume@ubuntu:~/0x13$ 

```
 Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-higher_level_programming ` 
* Directory:  ` 0x13-javascript_objects_scopes_closures ` 
* File:  ` 8-esrever.js ` 
 Self-paced manual review  Panel footer - Controls 
### 9. Log me
          mandatory         Progress vs Score  Task Body Write a function that prints the number of arguments already printed and the new argument value. (see example below)
* Prototype:  ` exports.logMe = function (item) ` 
* Output format:  ` <number arguments already printed>: <current argument value> ` 
```bash
guillaume@ubuntu:~/0x13$ cat 9-main.js
#!/usr/bin/node
const logMe = require('./9-logme').logMe;

logMe("Hello");
logMe("Best");
logMe("School");

guillaume@ubuntu:~/0x13$ ./9-main.js
0: Hello
1: Best
2: School
guillaume@ubuntu:~/0x13$ 

```
 Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-higher_level_programming ` 
* Directory:  ` 0x13-javascript_objects_scopes_closures ` 
* File:  ` 9-logme.js ` 
 Self-paced manual review  Panel footer - Controls 
### 10. Number conversion
          mandatory         Progress vs Score  Task Body Write a function that converts a number from base 10 to another base passed as argument:
* Prototype:  ` exports.converter = function (base) ` 
* You are not allowed to import any file
* You are not allowed to declare any new variable ( ` var ` ,  ` let ` , etc..)
```bash
guillaume@ubuntu:~/0x13$ cat 10-main.js
#!/usr/bin/node
const converter = require('./10-converter').converter;

let myConverter = converter(10);

console.log(myConverter(2));
console.log(myConverter(12));
console.log(myConverter(89));


myConverter = converter(16);

console.log(myConverter(2));
console.log(myConverter(12));
console.log(myConverter(89));

guillaume@ubuntu:~/0x13$ ./10-main.js
2
12
89
2
c
59
guillaume@ubuntu:~/0x13$ 

```
 Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-higher_level_programming ` 
* Directory:  ` 0x13-javascript_objects_scopes_closures ` 
* File:  ` 10-converter.js ` 
 Self-paced manual review  Panel footer - Controls 
[Done with the mandatory tasks? Unlock 3 advanced tasks now!](https://intranet.hbtn.io/projects/304/unlock_optionals) 

×#### Recommended Sandbox
[Running only]() 
### 1 image(0/5 Sandboxes spawned)
### Ubuntu 20.04 - NodeJS 14
Ubuntu 20.04 with NodeJS 14
[Run]() 