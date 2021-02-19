from functools import reduce

# Functioal Programming


# What is Functioal Programming?


"""

Functional Programming is all about separation of concerns OOP does as well. It's all about packaging our code into seperate chunks so that everything is well organized in each part of our code and each part is organized in a way that makes sense based on functionality. But they also separate data and functions.

There is no correct definition for what is and isn't functional but generally functional prgramming have an emphasis on simplicity where data and functions are concerned. Because in most functional programming paradigms, we don't have this idea of classes and objects instead functions operate on well-defined data structures like lists and dictionaries that we saw rather than belonging that data structure to an object.


The goal of Functional Programming paradigm is:

Clean + Understandable
Easy to Extend
Easy to Maintain
Memory Efficient
DRY


Now, when we come to functional programming, we have a very important pillar and unlike OOP, where we had those four pillars of encapsulation, abstraction, inheritance and polymorphism. If you want to break things down in functional programming it all comes down to this concept of:

Pure Functions

The idea here is that there is a separation between data of a program and the behavior of a program.

"""


# What is a pure function?

# A pure function has two rules:

"""

1) Given the same input it will always return the same output.

2) This idea of a function should not produce any side effects.
For example if we were to print something inside of this function, it affects the outside world. Because we're printing something onto a screen and the screen is the outside world. Or for example if this function was touching a variable that lived outside of a different scope, that's a side effect.

Look at the bottom example:

"""


def multiply_by2(li):
    new_list = []
    for item in li:
        new_list.append(item*2)
    return new_list


print(multiply_by2([1, 2, 3]))


"""

Is our above function a pure function?

First rule: Given the same input that is 1, 2 and 3, it will always return the same output. No matter how many times we run this function, it always going to give me the same output. So Ok we pass the first rule.

Second rule: Does this produce any side effects? Does this touch anything in the outside world? No, it doesn't. Nothing in the outside world matters to this function, because everything is contained between lines 51 and 54. So our function is a pure funtion.

"""


"""

Now, look at the bottom function. Is this a pure function? Well, no. Because this function have side effects. It interacts with the outside world which is print statement in line 82. The print statement tells me hay I'm going to print on whatever the display this machine has. It interacts with the screen.

"""


def multiply_by3(li):
    new_list = []
    for item in li:
        new_list.append(item*3)
    return print(new_list)


multiply_by3([1, 2, 3])


"""

Another example is that what if we have a new_list here (Line 95) that we actually define outside. Is this a pure function? No. This function has side effects. It interacts with the outside world and what's outside of this world of a function which remember is the scope. Well it iteracts with this new_list. It appends to this new_list.

"""


new_list = []


def multiply_by4(li):
    for item in li:
        new_list.append(item*4)
    return new_list


print(multiply_by4([1, 2, 3]))


"""

So for example if a programmer comes along and say maybe before we run this function we decide to change our new_list to an empty string. Then if we run this function now, we get this error. AttributeError: 'str' object has no attribute 'append'. Because now this new_list is a string object. So the new_list that lives in the outside world of this fuction can be modified by another developer or by a programmer.

So ideally we contain our functions and make them pure. Because as you can see we're never going to have a bug or an error in our code unless we wrote something wrong here (Lines between 120 and 122). But because we don't care about outside world, because everything that we give as an input is always going to produce a good output. It's going to be pure.

"""


new_list = []


def multiply_by5(li):
    for item in li:
        new_list.append(item*5)
    return new_list


new_list = ""
# print(multiply_by5([1, 2, 3]))
# AttributeError: 'str' object has no attribute 'append'


"""

When you have have pure functions, you have less buggy code. You're able to test your code better. It's easier to understand your code and overall you have these benefits of not having different parts of your code touching each other and affecting each other which makes your life as a programmer so much easier.


Note that pure functions is more of a guideline than an absolute. It is impossible to have pure functions everywhere. Because if a function doesn't affect the outside world at all, Well we wouldn't have any programs. We wouldn't be able to display things. We wouldn't be able to save things such as our game profile. However when you can, wherever you can functional programming teaches us that your functions are good. Try to create pure functions and only have few non pure functions that maybe interact with the outside world.


If for example this was our Wizard from OOP, with functional programming, we would have a wizard object or wizard dictionary that have name and power and instead of containing these in a class, I we would have different methods such as attack and  this wouldn't be a method, it would be a function. Because it doesn't live inside of a class. In functional programming they say hey, we don't need to combine data with funtions. Let's keep those separated. Let's just create pure functions that can be passed anything like a character (Line 153). And this way we keep those two things (Data and Funtions) separate. So that we can focus on pure functions (Line 153) and we can focus on data (Line 147).

"""


wizard = {
    'name': 'Merlin',
    'power': 50
}


def attack(character):
    return f"Attack {character['name']} with power of {character['power']}."


print(attack(wizard))


print("#####################################")


"""

Some useful functions that actually allow us to think in a functional programming paradigm.

Name of these functions are map, filter, zip and reduce.


1) map()

map actually allows us to simplify the code that we here of multiply_by2 (Line 50). You see with map we have it available as a built in function and we see here that we give the first parameter a function and then the second parameter is an iterables (Syntax: map(func, *iterables)). So we want to take some some sort of action here (First parameter) so a function and then the data that we want to take action upon (Second parameter) Like this. -> map(action, [1, 2, 3]).


Look at the bottom example. We have multiply_by6 function and we want to take action upon this list that is [1, 2, 3]. So we use map built in function. and use it like this (Line 180). So if we run it we get this: <map object at 0x0000022109C99EB0>. So we get a map object at this memory location and map automatically gives us this objcet that it has created in this memory. So in order for us to actually view it, we have to turn it into a list like this (Line 183). So if we run this, we get this error: TypeError: 'int' object is not iterable.

"""


def multiply_by6(li):
    new_list = []
    for item in li:
        new_list.append(item*6)
    return new_list


print(map(multiply_by6, [1, 2, 3]))
# <map object at 0x0000022109C99EB0>

# print(list(map(multiply_by6, [1, 2, 3])))
# TypeError: 'int' object is not iterable


"""

It's because with map we no longer need to this creation of a list, new_list (Line 177) then appending to a list (Line 179). You see the neat thing about map is that we give it some data       ([1, 2, 3]) and then this data gets acted upon by this function (multiply_by7) and all we need to do with the map function is to have a function that returns this part (item*6 Line 179). So instead of having all of this code, all we need to do is say return item*6 for example and change this parameter to item instead of li (Line 203). Look at the bottom codes. Notice here that we don't even have the brackets for calling our function here (Line 207). Because we don't need to call it. map does it for us. So the map is going to call the function.

So we're just saying hey when we call map like this, we want you to use this function (multiply_by7) at this memory adress (for example <map object at 0x0000022109C99EB0>) and use this data ([1, 2, 3]). Remembeer our functional programming paradigm, We have data that gets acted upon. So we separate those two out. So by doing this map automatically runs this function for us and loops through all the items in the iterable and returns for us a new map object that we're going to convert into a list.

Now here is the neat part. If we create a list, for example my_list and then passed it to map fuctions as iterable that is our data and then print my_list after running the map built in function (Line 215), we'll see that my_list hasn't changed. Remember a pure function is a function that doesn't affect the outside world. And this way map allows us to create a whole new list that doesn't modify my_list. So now my_list is immuttable. We don't change it and all it does is map function takes care of it and returns a new list for us, but we don't affect the outside world and there's no side effects in this function (multiply_by7) and every time we give it the same input, it's going to result in the same output.

Also notice that we can convert this to what we need for example tuple or set like this(Line 209 and 210).

"""


def multiply_by7(item):
    return item*7


print(list(map(multiply_by7, [1, 2, 3])))

print(tuple(map(multiply_by7, [1, 2, 3])))
print(set(map(multiply_by7, [1, 2, 3])))

my_list = [1, 2, 3]

print(list(map(multiply_by7, my_list)))
print(my_list)


print("#####################################")


"""

2) filter()

It filters things for us. So with map we always got the same number of items back. With filter we can sometimes receive less than what we gave it. We're filtering some of our results.

Let's create only_odd function that return only odd numers. So only_odd function is going to receive an item and this item is going to be acted upon. And we have to return something. What are we going to return? Well, the filter function is going to try and receive a True and False value or a boolean value wheter it should be filtered or it should not. So this (Line 237) is going to evaluate into boolean expression and based on the boolean expression, filter is going to say if it's True I'm going to keep it in the list and if it's not I'm going to remove it or not add it to the new list.

Syntax: filter(func, *iterables). It's like map function.

So if we run bottom program, we've filtered and removed the 2, because that's an even number. Notice here we're not calling the function like map. Because filter accepts a function or what we call a function signature that's say, hey just tell me where I can find what memory space I should go to for what action to take. And also filter doesn't modify the original list (my_list). And then like map, filter can be converted by other types except list. Like tuple and set.

"""


def only_odd(item):
    return item % 2 != 0


print(filter(only_odd, my_list))
# <filter object at 0x000001E2B8250EB0>

print(list(filter(only_odd, my_list)))

print(my_list)

print(set(filter(only_odd, my_list)))
print(tuple(filter(only_odd, my_list)))


print("#####################################")


"""

3) zip()

The zip function works kind of like a zipper. We need two lists or iterables and we can zip them together.

Syntax: zip(*iterables).

So we can give zip as many iterable as we want.

zip like a zipper takes the two or more iterables and grabs the first item from each and zips them together into a tuple like a zipper. What if we we have li3 as a tuple (Line 270) and then zip it with li2 and li1? If we run this, it works. So it doesn't matter. It's an iterable. It's going to zip the items together. So zip iterates over each one of these lists or data structures and zips them together and Notice that we don't modify any of our current data, instead we create a whole new one. Note that like map and filter we can convert them to other types too.

"""

li1 = [1, 2, 3]
li2 = [10, 20, 30]
li3 = (5, 4, 3)

print(zip(li1, li2))
# <zip object at 0x0000019D80AF8100>

print(list(zip(li1, li2)))

print(zip(li1, li2, li3))
# <zip object at 0x0000019645E18140>

print(list(zip(li1, li2, li3)))

print(set(zip(li1, li2, li3)))
print(tuple(zip(li1, li2, li3)))


print(li1)
print(li2)
print(li3)


print("#####################################")


"""

4) reduce()

reduce doesn't come as part of the Python built in function. In order for us to use reduce we have to do something like this. from functools import reduce (Line 1). Now you've never seen this before and this is something we're going to get to in the modules. But essentially what's happening here is when we downloaded Python interpreter and the Python package, we can import something from these functools. And functools are what we call a tool belt that we can use for functional tools that comes with the Python installation. And from there, there's a specific function that we can import. So we're saying, hey form functools, from this tool belt, we want you to import the reduce function so that we can use it in our code.

Syntax: reduce(function, sequence, [initial])

So first we need the function and then the sequence or the data and then the initial that is for example in our bottom function what the acc is going to be (Line 321).

So where it gets really interestig is that when we first pass my_list from the reduce we'll get the first item in my_list. The first item will be in this parameter (item in Line 321). And the acc will be the initial. So our function is accumulator and our data is my_list and our initial is 0. So in here (Line 329) the first item will be the first item in my_list and then the acc is going to be 0 if we don't give it anything or in our case we have said that the acc is going to be 0 (Line 329). And then we retutned acc + item in Line 323.

Note that if we convert our reduce to list for example, we'll get this error: TypeError: 'int' object is not iterable (Line 326). And we actually don't need the list anymore. Because reduce is gonna do something interesting for us.

What's just happened? Let's have a look. reduce allows us to reduce something, some sort of value from the iterable that we give it (In here our iterable is my_list). So let's go step by step. And for that we print our acc and item values before returning. So we have my_list and my_list is going to be applied to accumulator through reduce. The accumulator is going to take my_list and the first thing is going to do in the first pass through is going to say, hey what's my acc going to be? We're going to set it to 0. So the first pass through acc is going to be 0 and item is going to be 1 which is the first item in my_list (Line 322 prints -> 0 1). And then we're going to add it (0 + 1) and then return it that is 1. So now we have returned 1. Now the second pass through the acc is going to be what this (Line 323 returned that is 1. And then our item is going to be 2 which is the second item in my_lsis (Line 322 prints -> 1 2). So the next pass through whatever this (Line 323 is returned is going to be filled into acc that is 3, because we returned 1 + 2 in Line 323 that is 3. and our item is going to be 3 which is the third item in my_lsit (Line 322 prints -> 3 3). And then it returns 3 + 3 that is 6 at the end. So reduce returns 6 here (Line 323) as our result. So we have reduced our our list into some sort of data that we've manipulated usin in our case accumulator. And it's how reduce works.

If for example we changed this initial to 10 (Line 338). And if we run this we'll get 16. Because we started my initial acc with 10.

And if we use reduce wihtout passing the initial parameter like this (Line 342). As we said above our default initial will be 0 and we got the same result as this (Line 329) that is 6. but if we print our acc and items, we'll see that it start from second item in my_list that is our acc is 1 and our item is 2. So the only difference is that it don't prints the first Line that is 0 1.

Note that we print our acc and item at Line 322, because we want to see what's happens to these parameters. So now this function is not pure, because it affect the outside world. But if we want our function be pure, we can simply remove this (line 322) like this function(Lines 355 and 356).

Now, reduce is really really flexible and actually functions like map and filter are using this reduce function. So you can build your own map and filter function using reduce.

"""


def accumulator(acc, item):
    print(acc, item)
    return acc + item


# print(list(reduce(accumulator, my_list, 0)))
# TypeError: 'int' object is not iterable

print(reduce(accumulator, my_list, 0))
print(my_list)


def accumulator1(acc, item):
    print(acc, item)
    return acc + item


print(reduce(accumulator1, my_list, 10))
print(my_list)


def accumulator2(acc, item):
    print(acc, item)
    return acc + item


print(reduce(accumulator2, my_list))
print(my_list)


def accumulator3(acc, item):
    return acc + item


print(reduce(accumulator3, my_list, 0))
print(my_list)


print("#####################################")


# 1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']


def capitalize_pets(string):
    return string.upper()


print(list(map(capitalize_pets, my_pets)))


# 2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5, 4, 3, 2, 1]

print(list(zip(my_strings, sorted(my_numbers))))


# 3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]


def is_smart_student(score):
    return score > 50


print(list(filter(is_smart_student, scores)))


# 4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?
def combiner(cmb, item):
    print(cmb, item)
    return cmb + item


print(reduce(combiner, (my_numbers + scores)))


print("#####################################")


"""

At the above exercise we see that, if we want to combine or sum two or more lists together with reduce, we can simply sum them together like this (Line 397) as our secuence or data in our reduce function. But if we print our cmb and item like Line 393 before returning, we'll see that the list of my_numbers sums together at first and after it ends then it sums with the list of scores. For better understanding, look at the bottom examples and the difference between each one of them and at the end note that our result are the same at all of them.

"""

li_first = [12, 5, 9, 7, 77, 56, 27]
li_second = [47, 14, 21, 39, 98]
li_third = [54, 17, 30, 87, 54, 76, 32, 13]


def sum_all_lists(sal, item):
    print(sal, item)
    return sal + item


print(reduce(sum_all_lists, (li_first + li_second + li_third)))

print("#####################################")

print(reduce(sum_all_lists, (li_second + li_first + li_third)))

print("#####################################")

print(reduce(sum_all_lists, (li_third + li_first + li_second)))


print("#####################################")


# lambda expressions


"""

lambda actually is a computer science term that really is compatible with this idea of functional programming. lambda expressions in Python are one time anonymous functions that you don't need more than once. They are really really useful when you're using them for functions that First: You only use once. So lambda functions are for those occasions where we have a function but we only need to use it once. And then the second: Is that they're anonymous functions. That is because we only use them once. We don't need to have a name for them, because we don't really need to store them anywhere on our machines. We just want to use it once. Just run it and then we're done with it. Just throw it away.

Syntax : lambda param: action(param)

For example, let's say we have multiply_by8 function and we want to use this funcion once and we don't need to save it to memory. So now if we use lambda like this (Line 454) and note that our item are the items in my_list, we can remove our multiply_by8 function entirely. So now we comment them (Lines 447,448, 451 and 452) and we'll see that we have still the same result as using as multiply_by8 function.

"""


# def multiply_by8(item):
#    return item*8


# print(list(map(multiply_by8, my_list)))
# print(my_list)

print(list(map(lambda item: item*8, my_list)))
print(my_list)


"""

Notice that we can use lambda in filter and reduce funcion as well. Look at the bottom examples. And with this we don't no longer need only_odd and accumulator functions. And at the end note that lambda makes your code really really small. However they do the code a little bit less readable. So be carful when you're using these lambda expressions.

"""


print(list(filter(lambda item: item % 2 != 0, my_list)))
print(my_list)


print(reduce(lambda acc, item: acc + item, my_list))
print(my_list)


print("#####################################")


# lambda exercise:


# 1) Square the_list using lambda expression:


the_list = [5, 4, 3]

the_new_list = list(map(lambda num: num**2, the_list))

print(the_new_list)
print(the_list)


# 2) Sort list a based on the second value of tuples in the list:


"""

So if we jsut simply use sort method and then print(a), we'll see that the sort method will sort the list with the first key (Fitst value of each tuples). So for solving this, we have a key parameter in our sort metod that determines the key of our sorting method and we want the key to be two or let's say we want to sort our list based on second item of our each tuples.

So we can use lambda and say we want to sort our list of tuples based on second item of each tuples that mean x[1] that is the second item. Because sort method sort our list based x[0] that is the first item.

Let's go over this. What we're saying is hey we want you to run the sort function. And the key for the sort when we're sorting through everything is we want it to iterate over each item that we're going to get that is x is going to be this tuple. And we want to use the value which we're going to return which is second one. So the key is always going to be by the second item

"""


a = [(0, 2), (4, 3), (10, -1), (9, 9)]

# a.sort()
# print(a)
# [(0, 2), (4, 3), (9, 9), (10, -1)]

a.sort(key=lambda x: x[1])
print(a)


print("#####################################")


# Look at the bottom example for better understanding.


b = [
    [2, 7, 6],
    [8, 3, 7],
    [4, 1, 5]
]

print(b)

b.sort()
print(b)

b.sort(key=lambda x: x[0])
print(b)

b.sort(key=lambda x: x[1])
print(b)

b.sort(key=lambda x: x[2])
print(b)


print("#####################################")


"""

List, Set and Dictionary Comprehensions:

What are these comprehensions? They're a quick way or shorthand for us to create lists or sets or dictionaries in Python instead of perhaps looping, or appending to a bunch of items to lists.


List Comprehensions: 

Instead of doing something like this (Lines between 574 to 577) that is creating our_list and equals it to an empty list and then we do a for loop through 'hello' that is our iterable (our string) and then appending the items in the iterables to our_list, we can use a faster and cleaner way of using this.

Syntax:

li = [param for param in iterable]

When we say param, it means parameter or a variable or an expression (param that is before the for loop). So we can name it whatever we want. And then iterable that is in our case a string. and with this syntax we can simply create our new list and appending all of items in the string without using for loop outside our list. So instead we use for loop inside our list and do it in just one line. So line 581 says that hey, create char variable and then for each variable in the iterable that is 'hello' here, added to the list(our_list2). Look at the other examples.

What if we wanted this (our_list3) but all the numbers should be multiplied by two? Well, this time we use the same for loop, but instead of just the variable, this (num before for loop) is now an expression of how we want to act upon each character or number just like we saw in lambda expresions. So we can now say num*2 instead of num for these items (Line 587).

So now, what if we wanted to have this (our_list4) but we want to have just even or odd numbers? So we can use this:

Syntax:

li = [param for param in iterable if condition]

So here, our condition can determine that our num are even or odd.
 
"""


our_list = []

for char in 'hello':
    our_list.append(char)

print(our_list)

our_list2 = [char for char in 'hello']
print(our_list2)

our_list3 = [num for num in range(100)]
print(our_list3)

our_list4 = [num*2 for num in range(100)]
print(our_list4)

our_list5 = [num**3 for num in range(100) if num % 2 == 0]
print(our_list5)

our_list6 = [num**3 for num in range(100) if num % 2 != 0]
print(our_list6)


print("#####################################")


"""

Set Comprehensions:

It's same like list comprehensions and we should just change this brackets notation([])  to this curly brackets notation ({}). And note that sets only allow numbers or characters that are not duplicate, only unique items. Look at the bottom examples.

"""


our_set = {char for char in 'hello'}
print(our_set)

our_set1 = {num for num in range(100)}
print(our_set1)

our_set2 = {num*2 for num in range(100)}
print(our_set2)

our_set3 = {num**3 for num in range(100) if num % 2 == 0}
print(our_set3)

our_set4 = {num**3 for num in range(100) if num % 2 != 0}
print(our_set4)


print("#####################################")


"""

Dictionary Comprehensions:

In here except a number or character, we have a key and value and this key and value can be acted upon. Look at the bottom syntax.

Syntax:

dict1 = [key:value for key,value in iterable]

Let's say we want value to power the power of two. So this (key:value before for loop) is what we want to create, a key value pair and the value gets acted upon here. And then we have a for loop that we iterate on an iterable with our key and value that have key and value pair. For example a dictionary like simple_dict. So we need to pass it an iterable like dictionary that has both key and value. Notic that we used simple_dict.item(), because we want to iterate on it and with this we can grab the key and value pair in a tuple. 

If we want to add an if statement, we can simply add it like what we have done with list and set comprehensions. Look at the bottom syntax.

Syntax:

dict1 = [key:value for key,value in iterable if condition]

Note that we can named our key and value to whatever we want. 

Look at this example. We want to iterate over an iterable that is a list with set comprehension. So in this case we want to have a dictionary that our items in lists are our keys and item*2 are our values. So we can simply do like this (Line 668).

"""

simple_dict = {
    'a': 4,
    'b': 9
}

our_dict = {key: value**2 for key, value in simple_dict.items()}
print(our_dict)

our_dict1 = {key: value**3 for key,
             value in simple_dict.items() if value % 2 == 0}
print(our_dict1)

our_dict2 = {key: value**3 for key,
             value in simple_dict.items() if value % 2 != 0}
print(our_dict2)

our_dict3 = {num: num**3 for num in [1, 2, 3]}
print(our_dict3)

our_dict4 = {num*6: num**3 for num in [1, 2, 3]}
print(our_dict4)


print("#####################################")


"""

Exercise Comprehensions:


some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = []
for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)

print(duplicates)
['n', 'b']


Find the duplicates in some_list using comprehcension and return them in a list just like line 692. And look. 

So now, for solving this problem, we can use list comprehcension and use the syntax that we used above. So if we do like that (Line 703), we'll see that our each duplicate items will be printed two times. For solving this problem we can convert our list to a set with set() and with this we can remove duplicate items in our duplicates variable (Line 708). And if we print this we will see that our duplicate items will be printed correctly, but they are in a set instead of a list. So for solving this problem too, we can simply convert that to a list with list() (Line 713). And if we print that now, we'll see that we have tha same result as we have using for loop at above. 

"""

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = [value for value in some_list if some_list.count(value) > 1]

print(duplicates)
# ['b', 'b', 'n', 'n']

duplicates1 = set([value for value in some_list if some_list.count(value) > 1])

print(duplicates1)
# {'n', 'b'}

duplicates2 = list(
    set([value for value in some_list if some_list.count(value) > 1]))

print(duplicates2)
# ['n', 'b']

print("#####################################")
