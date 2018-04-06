### Objective 
In this challenge, we're going to learn about the difference between a class and an instance;

### Task 
Write a Person class with an instance variable, , and a constructor that takes an integer, , as a parameter. The constructor must assign  to  after confirming the argument passed as  is not negative; if a negative argument is passed as , the constructor should set  to  and print ```Age is not valid, setting age to 0.```. 
In addition, you must write the following instance methods:

- ```yearPasses()``` should increase the  instance variable by .

- ```amIOld()``` should perform the following conditional actions:
    - If ```age < 13```, print ```You are young.```.
    - If  ```age >= 13``` and ```age < 18```, print ```You are a teenager.```.
    - Otherwise, print ```You are old.```.

### Constraints

#### Sample Input
```
4
-1
10
16
18
```

#### Sample Output
```
Age is not valid, setting age to 0.
You are young.
You are young.

You are young.
You are a teenager.

You are a teenager.
You are old.

You are old.
You are old.
Explanation
```
