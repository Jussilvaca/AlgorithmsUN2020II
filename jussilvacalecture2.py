#!/usr/bin/env python
# coding: utf-8

# # Introduction to Python
# by Maxwell Margenot
# 
# Part of the Quantopian Lecture Series:
# 
# * [www.quantopian.com/lectures](https://www.quantopian.com/lectures)
# * [github.com/quantopian/research_public](https://github.com/quantopian/research_public)
# 
# 
# ---
# 
# All of the coding that you will do on the Quantopian platform will be in Python. It is also just a good, jack-of-all-trades language to know! Here we will provide you with the basics so that you can feel confident going through our other lectures and understanding what is happening.

# ## Code Comments
# 
# A comment is a note made by a programmer in the source code of a program. Its purpose is to clarify the source code and make it easier for people to follow along with what is happening. Anything in a comment is generally ignored when the code is actually run, making comments useful for including explanations and reasoning as well as removing specific lines of code that you may be unsure about. Comments in Python are created by using the pound symbol (`# Insert Text Here`). Including a `#` in a line of code will comment out anything that follows it.

# In[1]:


# This is a comment
# These lines of code will not change any values
# Anything following the first # is not run as code


# In[2]:


# This is another comment


# You may hear text enclosed in triple quotes (`""" Insert Text Here """`) referred to as multi-line comments, but this is not entirely accurate. This is a special type of `string` (a data type we will cover), called a `docstring`, used to explain the purpose of a function.

# In[3]:


""" This is a special string """


# In[4]:


""" This is like a comment, but it's diferent"""


# Make sure you read the comments within each code cell (if they are there). They will provide more real-time explanations of what is going on as you look at each line of code.

# ## Variables
# 
# Variables provide names for values in programming. If you want to save a value for later or repeated use, you give the value a name, storing the contents in a variable. Variables in programming work in a fundamentally similar way to variables in algebra, but in Python they can take on various different data types.
# 
# The basic variable types that we will cover in this section are `integers`, `floating point numbers`, `booleans`, and `strings`. 
# 
# An `integer` in programming is the same as in mathematics, a round number with no values after the decimal point. We use the built-in `print` function here to display the values of our variables as well as their types!

# In[5]:


my_integer = 50
print my_integer, type(my_integer)


# In[6]:


my_string = "Hello world"
print my_integer, type(my_string)


# Variables, regardless of type, are assigned by using a single equals sign (`=`). Variables are case-sensitive so any changes in variation in the capitals of a variable name will reference a different variable entirely.

# In[7]:


one = 1
print One


# In[9]:


one=1
print one


# A `floating point` number, or a `float` is a fancy name for a real number (again as in mathematics). To define a `float`, we need to either include a decimal point or specify that the value is a float.

# In[10]:


my_float = 1.0
print my_float, type(my_float)
my_float = float(1)
print my_float, type(my_float)


# In[16]:


float_2=float(2)
print float_2

float_2= 2
print float_2/1

float_2=2.0
print float_2


# A variable of type `float` will not round the number that you store in it, while a variable of type `integer` will. This makes `floats` more suitable for mathematical calculations where you want more than just integers.
# 
# Note that as we used the `float()` function to force an number to be considered a `float`, we can use the `int()` function to force a number to be considered an `int`.

# In[17]:


my_int = int(3.14159)
print my_int, type(my_int)


# In[40]:



int_2 = int(3.95)
print int_2

int_2 = int(3.97)
print int_2

int_2 = int(3.98)
print int_2

int_2 = int(3.99)
print int_2

int_2 = int(3.991)
print int_2

int_2 = int(3.995)
print int_2

int_2 = int(3.999)
print int_2

int_2 = int(3.9995)
print int_2

int_2 = int(3.9999)
print int_2

int_2 = int(3.99995)
print int_2

int_2 = int(3.99999)
print int_2

int_2 = int(3.999995)
print int_2

int_2 = int(3.9999999999999999)
print int_2


# The `int()` function will also truncate any digits that a number may have after the decimal point!
# 
# Strings allow you to include text as a variable to operate on. They are defined using either single quotes ('') or double quotes ("").

# In[41]:


my_string = 'This is a string with single quotes'
print my_string
my_string = "This is a string with double quotes"
print my_string


# In[42]:


my_string_2 = 'This is another string with single quotes'
print my_string_2
my_string_2 = "This is another string with double quotes"
print my_string_2


# Both are allowed so that we can include apostrophes or quotation marks in a string if we so choose.

# In[43]:


my_string = '"Jabberwocky", by Lewis Carroll'
print my_string
my_string = "'Twas brillig, and the slithy toves / Did gyre and gimble in the wabe;"
print my_string


# In[45]:


my_str = '"String with quotation"'
print my_str
my_str = "'String with apostrophes'"
print my_str


# Booleans, or `bools` are binary variable types. A `bool` can only take on one of two values, these being `True` or `False`. There is much more to this idea of truth values when it comes to programming, which we cover later in the [Logical Operators](#id-section5) of this notebook.

# In[46]:


my_bool = True
print my_bool, type(my_bool)


# In[47]:


my_bool = False
print my_bool, type(my_bool)


# There are many more data types that you can assign as variables in Python, but these are the basic ones! We will cover a few more later as we move through this tutorial.

# ## Basic Math
# 
# Python has a number of built-in math functions. These can be extended even further by importing the **math** package or by including any number of other calculation-based packages.
# 
# All of the basic arithmetic operations are supported: `+`, `-`, `/`, and `*`. You can create exponents by using `**` and modular arithmetic is introduced with the mod operator, `%`.

# In[48]:


print 'Addition: ', 2 + 2
print 'Subtraction: ', 7 - 4
print 'Multiplication: ', 2 * 5
print 'Division: ', 10 / 2
print 'Exponentiation: ', 3**2


# In[49]:


print 'Addition: ', 1 + 0
print 'Subtraction: ', 1 - 0
print 'Multiplication: ', 2 * (1/2)
print 'Division: ', 10 / 10
print 'Exponentiation: ', 3**0


# If you are not familiar with the the mod operator, it operates like a remainder function. If we type $15 \ \% \ 4$, it will return the remainder after dividing $15$ by $4$.

# In[50]:


print 'Modulo: ', 15 % 4


# In[53]:


print "Mod: ", 5%2


# Mathematical functions also work on variables!

# In[55]:


first_integer = 4
second_integer = 5
print first_integer * second_integer


# In[54]:


a = 2
b = 100
print a * b


# Make sure that your variables are floats if you want to have decimal points in your answer. If you perform math exclusively with integers, you get an integer. Including any float in the calculation will make the result a float.

# In[56]:


first_integer = 11
second_integer = 3
print first_integer / second_integer


# In[57]:


a = 2
b = 100
print a / b


# In[58]:


first_number = 11.0
second_number = 3.0
print first_number / second_number


# In[59]:


a = float(2)
b = float(100)
print a / b


# Python has a few built-in math functions. The most notable of these are:
# 
# * `abs()`
# * `round()`
# * `max()`
# * `min()`
# * `sum()`
# 
# These functions all act as you would expect, given their names. Calling `abs()` on a number will return its absolute value. The `round()` function will round a number to a specified number of the decimal points (the default is $0$). Calling `max()` or `min()` on a collection of numbers will return, respectively, the maximum or minimum value in the collection. Calling `sum()` on a collection of numbers will add them all up. If you're not familiar with how collections of values in Python work, don't worry! We will cover collections in-depth in the next section. 
# 
# Additional math functionality can be added in with the `math` package.

# In[60]:


import math


# The math library adds a long list of new mathematical functions to Python. Feel free to check out the [documentation](https://docs.python.org/2/library/math.html) for the full list and details. It concludes some mathematical constants

# In[61]:


print 'Pi: ', math.pi
print "Euler's Constant: ", math.e


# In[66]:


print 'factorial of 10: ',math.factorial(10)
print 'log(10) of 100: ',math.log10(100)


# As well as some commonly used math functions

# In[67]:


print 'Cosine of pi: ', math.cos(math.pi)


# In[68]:


print "Sine of pi: ", math.sin(math.pi)


# ## Collections
# ### Lists
# 
# A `list` in Python is an ordered collection of objects that can contain any data type. We define a `list` using brackets (`[]`).

# In[69]:


my_list = [1, 2, 3]
print my_list


# In[70]:


another_list = [3, 2, 1,0]
print another_list


# We can access and index the list by using brackets as well. In order to select an individual element, simply type the list name followed by the index of the item you are looking for in braces.

# In[71]:


print my_list[0]
print my_list[2]


# In[74]:


print another_list[0]
print another_list[3]


# Indexing in Python starts from $0$. If you have a list of length $n$, the first element of the list is at index $0$, the second element is at index $1$, and so on and so forth. The final element of the list will be at index $n-1$. Be careful! Trying to access a non-existent index will cause an error.

# In[75]:


print 'The first, second, and third list elements: ', my_list[0], my_list[1], my_list[2]
print 'Accessing outside the list bounds causes an error: ', my_list[3]


# In[76]:


another_list[4]


# We can see the number of elements in a list by calling the `len()` function.

# In[77]:


print len(my_list)


# In[78]:


print len(another_list)


# We can update and change a list by accessing an index and assigning new value.

# In[79]:


print my_list
my_list[0] = 42
print my_list


# In[80]:


print another_list
another_list[2] = 69
print another_list


# This is fundamentally different from how strings are handled. A `list` is mutable, meaning that you can change a `list`'s elements without changing the list itself. Some data types, like `strings`, are immutable, meaning you cannot change them at all. Once a `string` or other immutable data type has been created, it cannot be directly modified without creating an entirely new object.

# In[86]:


my_string = "Strings never change"
my_string[0] = 'Z'


# As we stated before, a list can contain any data type. Thus, lists can also contain strings.

# In[87]:


my_list_2 = ['one', 'two', 'three']
print my_list_2


# In[89]:


my_list_2 = ['1', "2", '3']
print my_list_2


# Lists can also contain multiple different data types at once!

# In[91]:


my_list_3 = [True, 'False', 42]


# In[94]:


my_list_3 = [True, 'False', 86]
print my_list_3


# If you want to put two lists together, they can be combined with a `+` symbol.

# In[95]:


my_list_4 = my_list + my_list_2 + my_list_3
print my_list_4


# In[101]:


list1=[False, True, 2]
list2=["three", "four", "five"]
list3=[6,7,8]
list4= list1 + list2 + list3
print list4
list5=[list1,list2,list3]
print list5


# In addition to accessing individual elements of a list, we can access groups of elements through slicing.

# In[ ]:


my_list = ['friends', 'romans', 'countrymen', 'lend', 'me', 'your', 'ears']


# #### Slicing
# 
# We use the colon (`:`) to slice lists. 

# In[104]:


print my_list[2:4]


# In[103]:


print list4[1:3]


# Using `:` we can select a group of elements in the list starting from the first element indicated and going up to  (but not including) the last element indicated.
# 
# We can also select everything after a certain point

# In[105]:


print my_list[1:]


# In[106]:


print list4[3:]


# And everything before a certain point

# In[107]:


print my_list[:4]


# In[108]:


print list4[:5]


# Using negative numbers will count from the end of the indices instead of from the beginning. For example, an index of `-1` indicates the last element of the list.

# In[130]:


print my_list[-1]


# In[111]:


print list4[-2]


# You can also add a third component to slicing. Instead of simply indicating the first and final parts of your slice, you can specify the step size that you want to take. So instead of taking every single element, you can take every other element.

# In[118]:


print my_list[0:7:2]


# In[119]:


print list4[0:7:2]


# Here we have selected the entire list (because `0:7` will yield elements `0` through `6`) and we have selected a step size of `2`. So this will spit out element `0` , element `2`, element `4`, and so on through the list element selected. We can skip indicated the beginning and end of our slice, only indicating the step, if we like.

# In[120]:


print my_list[::2]


# In[122]:


print list4[::3]


# Lists implictly select the beginning and end of the list when not otherwise specified.

# In[123]:


print my_list[:]


# In[126]:


print list4[::]


# With a negative step size we can even reverse the list!

# In[127]:


print my_list[::-1]


# In[128]:


print list4[::-2]


# Python does not have native matrices, but with lists we can produce a working fascimile. Other packages, such as `numpy`, add matrices as a separate data type, but in base Python the best way to create a matrix is to use a list of lists.

# We can also use built-in functions to generate lists. In particular we will look at `range()` (because we will be using it later!). Range can take several different inputs and will return a list.

# In[129]:


b = 10
my_list = range(b)
print my_list


# In[135]:


print my_list[0]
print my_list[5]
print my_list[9]


# Similar to our list-slicing methods from before, we can define both a start and an end for our range. This will return a list that is includes the start and excludes the end, just like a slice.

# In[136]:


a = 0
b = 10
my_list = range(a, b)
print my_list


# In[137]:


print my_list[0]
print my_list[5]
print my_list[9]


# We can also specify a step size. This again has the same behavior as a slice.

# In[138]:


a = 0
b = 10
step = 2
my_list = range(a, b, step)
print my_list


# In[142]:


print my_list[0]
print my_list[1]
print my_list[3]


# ### Tuples
# 
# A `tuple` is a data type similar to a list in that it can hold different kinds of data types. The key difference here is that a `tuple` is immutable. We define a `tuple` by separating the elements we want to include by commas. It is conventional to surround a `tuple` with parentheses.

# In[143]:


my_tuple = 'I', 'have', 30, 'cats'
print my_tuple


# In[145]:


my_tuple_2 = ('I',"don't" ,'have', 30, 'cats')
print my_tuple_2


# As mentioned before, tuples are immutable. You can't change any part of them without defining a new tuple.

# In[146]:


my_tuple[3] = 'dogs' # Attempts to change the 'cats' value stored in the the tuple to 'dogs'


# In[147]:


my_tuple[0] = 'You' # Attempts to change the 'I' value stored in the the tuple to 'you'


# You can slice tuples the same way that you slice lists!

# In[148]:


print my_tuple[1:3]


# In[149]:


print my_tuple_2[:3]


# And concatenate them the way that you would with strings!

# In[150]:


my_other_tuple = ('make', 'that', 50)
print my_tuple + my_other_tuple


# In[151]:


print my_tuple_2+my_tuple_2


# We can 'pack' values together, creating a tuple (as above), or we can 'unpack' values from a tuple, taking them out.

# In[152]:


str_1, str_2, int_1 = my_other_tuple
print str_1, str_2, int_1


# Unpacking assigns each value of the tuple in order to each variable on the left hand side of the equals sign. Some functions, including user-defined functions, may return tuples, so we can use this to directly unpack them and access the values that we want.

# ### Sets
# 
# A `set` is a collection of unordered, unique elements. It works almost exactly as you would expect a normal set of things in mathematics to work and is defined using braces (`{}`).

# In[158]:


things_i_like = {'dogs', 7, 'the number 4', 4, 4, 4, 42, 'lizards', 'man I just LOVE the number 4'}
print things_i_like, type(things_i_like)


# In[160]:


things_i_like_2 = {"coffee", "more coffee"}
print things_i_like_2, type(things_i_like_2)


# Note how any extra instances of the same item are removed in the final set. We can also create a `set` from a list, using the `set()` function.

# In[161]:


animal_list = ['cats', 'dogs', 'dogs', 'dogs', 'lizards', 'sponges', 'cows', 'bats', 'sponges']
animal_set = set(animal_list)
print animal_set # Removes all extra instances from the list


# In[164]:


list_example = [1,2,3,3,3,3,4,4,4,5,6,7,7,7]
set_example = set(list_example)
print set_example


# Calling `len()` on a set will tell you how many elements are in it.

# In[165]:


print len(animal_set)


# In[166]:


print len(set_example)


# Because a `set` is unordered, we can't access individual elements using an index. We can, however, easily check for membership (to see if something is contained in a set) and take the unions and intersections of sets by using the built-in set functions.

# In[167]:


'cats' in animal_set # Here we check for membership using the `in` keyword.


# In[170]:


print 3 in set_example
print 8 in set_example


# Here we checked to see whether the string 'cats' was contained within our `animal_set` and it returned `True`, telling us that it is indeed in our set.
# 
# We can connect sets by using typical mathematical set operators, namely `|`, for union, and `&`, for intersection. Using `|` or `&` will return exactly what you would expect if you are familiar with sets in mathematics.

# In[172]:


print animal_set | things_i_like # You can also write things_i_like | animal_set with no difference


# In[175]:


print set_example | set_example 
print set_example & set_example


# Pairing two sets together with `|` combines the sets, removing any repetitions to make every set element unique.

# In[177]:


print animal_set & things_i_like # You can also write things_i_like & animal_set with no difference


# Pairing two sets together with `&` will calculate the intersection of both sets, returning a set that only contains what they have in common.
# 
# If you are interested in learning more about the built-in functions for sets, feel free to check out the [documentation](https://docs.python.org/2/library/sets.html).

# ### Dictionaries
# 
# Another essential data structure in Python is the dictionary. Dictionaries are defined with a combination of curly braces (`{}`) and colons (`:`). The braces define the beginning and end of a dictionary and the colons indicate key-value pairs. A dictionary is essentially a set of key-value pairs. The key of any entry must be an immutable data type. This makes both strings and tuples candidates. Keys can be both added and deleted.
# 
# In the following example, we have a dictionary composed of key-value pairs where the key is a genre of fiction (`string`) and the value is a list of books (`list`) within that genre. Since a collection is still considered a single entity, we can use one to collect multiple variables or values into one key-value pair.

# In[180]:


my_dict = {"High Fantasy": ["Wheel of Time", "Lord of the Rings"], 
           "Sci-fi": ["Book of the New Sun", "Neuromancer", "Snow Crash"],
           "Weird Fiction": ["At the Mountains of Madness", "The House on the Borderland"]}


# In[182]:


menu = {1:["a","b","c"],2:["d","e","f"],3:["g","h","i"]}


# After defining a dictionary, we can access any individual value by indicating its key in brackets.

# In[181]:


print my_dict["Sci-fi"]


# In[184]:


print menu[2]


# We can also change the value associated with a given key

# In[186]:


my_dict["Sci-fi"] = "I can't read"
print my_dict["Sci-fi"]


# In[188]:


menu[1]="No hay"
print menu[1]


# Adding a new key-value pair is as simple as defining it.

# In[189]:


my_dict["Historical Fiction"] = ["Pillars of the Earth"]
print my_dict["Historical Fiction"]


# In[190]:


print my_dict


# In[191]:


print menu


# ## String Shenanigans
# 
# We already know that strings are generally used for text. We can used built-in operations to combine, split, and format strings easily, depending on our needs.
# 
# The `+` symbol indicates concatenation in string language. It will combine two strings into a longer string.

# In[193]:


first_string = '"Beware the Jabberwock, my son! /The jaws that bite, the claws that catch! /'
second_string = 'Beware the Jubjub bird, and shun /The frumious Bandersnatch!"/'
third_string = first_string + second_string
print third_string


# Strings are also indexed much in the same way that lists are.

# In[194]:


print "Oh"+" "+"maiga"


# In[195]:


my_string = 'Supercalifragilisticexpialidocious'
print 'The first letter is: ', my_string[0] # Uppercase S
print 'The last letter is: ', my_string[-1] # lowercase s
print 'The second to last letter is: ', my_string[-2] # lowercase u
print 'The first five characters are: ', my_string[0:5] # Remember: slicing doesn't include the final element!
print 'Reverse it!: ', my_string[::-1]


# In[196]:


my_string_3 = 'Anitalavalatina'
print 'The first letter is: ', my_string_3[0] # Uppercase S
print 'The last letter is: ', my_string_3[-1] # lowercase s
print 'The second to last letter is: ', my_string_3[-2] # lowercase u
print 'The first five characters are: ', my_string_3[0:5] # Remember: slicing doesn't include the final element!
print 'Reverse it!: ', my_string_3[::-1]


# Built-in objects and classes often have special functions associated with them that are called methods. We access these methods by using a period ('.'). We will cover objects and their associated methods more in another lecture!
# 
# Using string methods we can count instances of a character or group of characters.

# In[197]:


print 'Count of the letter i in Supercalifragilisticexpialidocious: ', my_string.count('i')
print 'Count of "li" in the same word: ', my_string.count('li')


# In[198]:


print 'Count of the letter i in Anitalavalatina: ', my_string_3.count('i')
print 'Count of "li" in the same word: ', my_string_3.count('li')


# We can also find the first instance of a character or group of characters in a string.

# In[199]:


print 'The first time i appears is at index: ', my_string.find('i')


# In[200]:


print 'The first time i appears is at index: ', my_string_3.find('i')


# As well as replace characters in a string.

# In[ ]:


print "All i's are now a's: ", my_string.replace('i', 'a')


# In[201]:


print "It's raining cats and dogs".replace('dogs', 'more cats')


# In[203]:


print "I don't know how make this".replace(" don't", '')


# There are also some methods that are unique to strings. The function `upper()` will convert all characters in a string to uppercase, while `lower()` will convert all characters in a string to lowercase!

# In[204]:


my_string = "I can't hear you"
print my_string.upper()
my_string = "I said HELLO"
print my_string.lower()


# In[208]:


asdf="This is a sentence"
print asdf.upper()
print asdf.lower()


# ### String Formatting
# 
# Using the `format()` method we can add in variable values and generally format our strings.

# In[209]:


my_string = "{0} {1}".format('Marco', 'Polo')
print my_string


# In[212]:


my_string_3 = "{0} {1}".format('Hola', 'Mundo')
print my_string_3


# In[210]:


my_string = "{1} {0}".format('Marco', 'Polo')
print my_string


# In[213]:


my_string_3 = "{1} {0}".format('Hola', 'Mundo')
print my_string_3


# We use braces (`{}`) to indicate parts of the string that will be filled in later and we use the arguments of the `format()` function to provide the values to substitute. The numbers within the braces indicate the index of the value in the `format()` arguments.

# See the `format()` [documentation](https://docs.python.org/2/library/string.html#format-examples) for additional examples.

# If you need some quick and dirty formatting, you can instead use the `%` symbol, called the string formatting operator. 

# In[214]:


print 'insert %s here' % 'value'


# The `%` symbol basically cues Python to create a placeholder. Whatever character follows the `%` (in the string) indicates what sort of type the value put into the placeholder will have. This character is called a *conversion type*. Once the string has been closed, we need another `%` that will be followed by the values to insert. In the case of one value, you can just put it there. If you are inserting more than one value, they must be enclosed in a tuple.

# In[215]:


print 'There are %s cats in my %s' % (13, 'apartment')


# In these examples, the `%s` indicates that Python should convert the values into strings. There are multiple conversion types that you can use to get more specific with the the formatting. See the string formatting [documentation](https://docs.python.org/2/library/stdtypes.html#string-formatting) for additional examples and more complete details on use.

# ## Logical Operators
# ### Basic Logic
# 
# Logical operators deal with `boolean` values, as we briefly covered before. If you recall, a `bool` takes on one of two values, `True` or `False` (or $1$ or $0$). The basic logical statements that we can make are defined using the built-in comparators. These are `==` (equal), `!=` (not equal), `<` (less than), `>` (greater than), `<=` (less than or equal to), and `>=` (greater than or equal to).

# In[216]:


print 5 == 5


# In[219]:


print 1 == 5


# In[217]:


print 5 > 5


# In[220]:


print 5 > 3


# These comparators also work in conjunction with variables.

# In[221]:


m = 2
n = 23
print m < n


# In[222]:


m = 2
n = 23
print n < m


# We can string these comparators together to make more complex logical statements using the logical operators `or`, `and`, and `not`. 

# In[223]:


statement_1 = 10 > 2
statement_2 = 4 <= 6
print "Statement 1 truth value: {0}".format(statement_1)
print "Statement 2 truth value: {0}".format(statement_2)
print "Statement 1 and Statement 2: {0}".format(statement_1 and statement_2)


# In[224]:


print "Statement 1 or Statement 2: {0}".format(statement_1 or statement_2)


# The `or` operator performs a logical `or` calculation. This is an inclusive `or`, so if either component paired together by `or` is `True`, the whole statement will be `True`. The `and` statement only outputs `True` if all components that are `and`ed together are True. Otherwise it will output `False`. The `not` statement simply inverts the truth value of whichever statement follows it. So a `True` statement will be evaluated as `False` when a `not` is placed in front of it. Similarly, a `False` statement will become `True` when a `not` is in front of it.
# 
# Say that we have two logical statements, or assertions, $P$ and $Q$. The truth table for the basic logical operators is as follows:
# 
# |  P  |  Q  | `not` P| P `and` Q | P `or` Q|
# |:-----:|:-----:|:---:|:---:|:---:|
# | `True` | `True` | `False` | `True` | `True` |
# | `False` | `True` | `True` | `False` | `True` |
# | `True` | `False` | `False` | `False` | `True` |
# | `False` | `False` | `True` | `False` | `False` |
# 
# We can string multiple logical statements together using the logical operators.

# In[230]:


print ((2 < 3) and (3 > 0)) or ((5 > 6) and not (4 < 2)) 


# Logical statements can be as simple or complex as we like, depending on what we need to express. Evaluating the above logical statement step by step we see that we are evaluating (`True and True`) `or` (`False and not False`). This becomes `True or (False and True`), subsequently becoming `True or False`, ultimately being evaluated as `True`.

# #### Truthiness
# 
# Data types in Python have a fun characteristic called truthiness. What this means is that most built-in types will evaluate as either `True` or `False` when a boolean value is needed (such as with an if-statement). As a general rule, containers like strings, tuples, dictionaries, lists, and sets, will return `True` if they contain anything at all and `False` if they contain nothing.

# In[231]:


# Similar to how float() and int() work, bool() forces a value to be considered a boolean!
print bool('')


# In[232]:


print bool('I have character!')


# In[233]:


print bool([])


# In[235]:


print bool([1])


# In[234]:


print bool([1, 2, 3])


# In[237]:


print bool([])


# And so on, for the other collections and containers. `None` also evaluates as `False`. The number `1` is equivalent to `True` and the number `0` is equivalent to `False` as well, in a boolean context.

# ### If-statements
# 
# We can create segments of code that only execute if a set of conditions is met. We use if-statements in conjunction with logical statements in order to create branches in our code. 
# 
# An `if` block gets entered when the condition is considered to be `True`. If condition is evaluated as `False`, the `if` block will simply be skipped unless there is an `else` block to accompany it. Conditions are made using either logical operators or by using the truthiness of values in Python. An if-statement is defined with a colon and a block of indented text.

# In[238]:


# This is the basic format of an if statement. This is a vacuous example. 
# The string "Condition" will always evaluated as True because it is a
# non-empty string. he purpose of this code is to show the formatting of
# an if-statement.
if "Condition": 
    # This block of code will execute because the string is non-empty
    # Everything on these indented lines
    print True
else:
    # So if the condition that we examined with if is in fact False
    # This block of code will execute INSTEAD of the first block of code
    # Everything on these indented lines
    print False
# The else block here will never execute because "Condition" is a non-empty string.


# In[240]:


i = 4
if i == 5:
    print 'The variable i has a value of 5'


# In[241]:


i = 5
if i == 5:
    print 'The variable i has a value of 5'


# Because in this example `i = 4` and the if-statement is only looking for whether `i` is equal to `5`, the print statement will never be executed. We can add in an `else` statement to create a contingency block of code in case the condition in the if-statement is not evaluated as `True`.

# In[242]:


i = 4
if i == 5:
    print "All lines in this indented block are part of this block"
    print 'The variable i has a value of 5'
else:
    print "All lines in this indented block are part of this block"
    print 'The variable i is not equal to 5'


# In[243]:


i = 5
if i == 5:
    print "All lines in this indented block are part of this block"
    print 'The variable i has a value of 5'
else:
    print "All lines in this indented block are part of this block"
    print 'The variable i is not equal to 5'


# We can implement other branches off of the same if-statement by using `elif`, an abbreviation of "else if". We can include as many `elifs` as we like until we have exhausted all the logical branches of a condition.

# In[244]:


i = 1
if i == 1:
    print 'The variable i has a value of 1'
elif i == 2:
    print 'The variable i has a value of 2'
elif i == 3:
    print 'The variable i has a value of 3'
else:
    print "I don't care what i is"


# In[247]:


i = 3.5
if i == 1:
    print 'The variable i has a value of 1'
elif i == 2:
    print 'The variable i has a value of 2'
elif i == 3:
    print 'The variable i has a value of 3'
else:
    print "I don't care what i is"


# You can also nest if-statements within if-statements to check for further conditions.

# In[248]:


i = 10
if i % 2 == 0:
    if i % 3 == 0:
        print 'i is divisible by both 2 and 3! Wow!'
    elif i % 5 == 0:
        print 'i is divisible by both 2 and 5! Wow!'
    else:
        print 'i is divisible by 2, but not 3 or 5. Meh.'
else:
    print 'I guess that i is an odd number. Boring.'


# In[249]:


i = 6
if i % 2 == 0:
    if i % 3 == 0:
        print 'i is divisible by both 2 and 3! Wow!'
    elif i % 5 == 0:
        print 'i is divisible by both 2 and 5! Wow!'
    else:
        print 'i is divisible by 2, but not 3 or 5. Meh.'
else:
    print 'I guess that i is an odd number. Boring.'


# Remember that we can group multiple conditions together by using the logical operators!

# In[251]:


i = 5
j = 12
if i < 10 and j > 11:
    print '{0} is less than 10 and {1} is greater than 11! How novel and interesting!'.format(i, j)


# In[252]:


i = 9
j = 19
if i < 10 and j > 11:
    print '{0} is less than 10 and {1} is greater than 11! How novel and interesting!'.format(i, j)


# You can use the logical comparators to compare strings!

# In[253]:


my_string = "Carthago delenda est"
if my_string == "Carthago delenda est":
    print 'And so it was! For the glory of Rome!'
else:
    print 'War elephants are TERRIFYING. I am staying home.'


# In[254]:


my_string = "Hello"
if my_string == "Carthago delenda est":
    print 'And so it was! For the glory of Rome!'
else:
    print 'War elephants are TERRIFYING. I am staying home.'


# As with other data types, `==` will check for whether the two things on either side of it have the same value. In this case, we compare whether the value of the strings are the same. Using `>` or `<` or any of the other comparators is not quite so intuitive, however, so we will stay from using comparators with strings in this lecture. Comparators will examine the [lexicographical order](https://en.wikipedia.org/wiki/Lexicographical_order) of the strings, which might be a bit more in-depth than you might like.

# Some built-in functions return a boolean value, so they can be used as conditions in an if-statement. User-defined functions can also be constructed so that they return a boolean value. This will be covered later with function definition!
# 
# The `in` keyword is generally used to check membership of a value within another value. We can check memebership in the context of an if-statement and use it to output a truth value.

# In[255]:


if 'a' in my_string or 'e' in my_string:
    print 'Those are my favorite vowels!'


# In[256]:


if 'i' in my_string or 'u' in my_string:
    print 'Those are my favorite vowels!'


# Here we use `in` to check whether the variable `my_string` contains any particular letters. We will later use `in` to iterate through lists!

# ## Loop Structures
# 
# Loop structures are one of the most important parts of programming. The `for` loop and the `while` loop provide a way to repeatedly run a block of code repeatedly. A `while` loop will iterate until a certain condition has been met. If at any point after an iteration that condition is no longer satisfied, the loop terminates. A `for` loop will iterate over a sequence of values and terminate when the sequence has ended. You can instead include conditions within the `for` loop to decide whether it should terminate early or you could simply let it run its course.

# In[257]:


i = 5
while i > 0: # We can write this as 'while i:' because 0 is False!
    i -= 1
    print 'I am looping! {0} more to go!'.format(i)


# In[258]:


i = 0
while i < 5: # We can write this as 'while i:' because 0 is False!
    i += 1
    print 'I am looping! {0} more to go!'.format(i)


# 
# With `while` loops we need to make sure that something actually changes from iteration to iteration so that that the loop actually terminates. In this case, we use the shorthand `i -= 1` (short for `i = i - 1`) so that the value of `i` gets smaller with each iteration. Eventually `i` will be reduced to `0`, rendering the condition `False` and exiting the loop.

# A `for` loop iterates a set number of times, determined when you state the entry into the loop. In this case we are iterating over the list returned from `range()`. The `for` loop selects a value from the list, in order, and temporarily assigns the value of `i` to it so that operations can be performed with the value.

# In[259]:


for i in range(5):
    print 'I am looping! I have looped {0} times!'.format(i + 1)


# In[260]:


for i in range(100):
    print 'I am looping! I have looped {0} times!'.format(i + 1)


# Note that in this `for` loop we use the `in` keyword. Use of the `in` keyword is not limited to checking for membership as in the if-statement example. You can iterate over any collection with a `for` loop by using the `in` keyword.
# 
# In this next example, we will iterate over a `set` because we want to check for containment and add to a new set.

# In[261]:


my_list = {'cats', 'dogs', 'lizards', 'cows', 'bats', 'sponges', 'humans'} # Lists all the animals in the world
mammal_list = {'cats', 'dogs', 'cows', 'bats', 'humans'} # Lists all the mammals in the world
my_new_list = set()
for animal in my_list:
    if animal in mammal_list:
        # This adds any animal that is both in my_list and mammal_list to my_new_list
        my_new_list.add(animal)
        
print my_new_list


# There are two statements that are very helpful in dealing with both `for` and `while` loops. These are `break` and `continue`. If `break` is encountered at any point while a loop is executing, the loop will immediately end.

# In[262]:


i = 10
while True:
    if i == 14:
        break
    i += 1 # This is shorthand for i = i + 1. It increments i with each iteration.
    print i


# In[263]:


i = 5
while True:
    if i == 15:
        break
    i += 1 # This is shorthand for i = i + 1. It increments i with each iteration.
    print i


# In[264]:


for i in range(5):
    if i == 2:
        break
    print i


# In[265]:


for i in range(5):
    if i == 4:
        break
    print i


# The `continue` statement will tell the loop to immediately end this iteration and continue onto the next iteration of the loop.

# In[266]:


i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print i


# In[268]:


i = 0
while i < 10:
    i += 1
    if i%2==1:
        continue
    print i


# This loop skips printing the number $3$ because of the `continue` statement that executes when we enter the if-statement. The code never sees the command to print the number $3$ because it has already moved to the next iteration. The `break` and `continue` statements are further tools to help you control the flow of your loops and, as a result, your code.

# The variable that we use to iterate over a loop will retain its value when the loop exits. Similarly, any variables defined within the context of the loop will continue to exist outside of it.

# In[269]:


for i in range(5):
    loop_string = 'I transcend the loop!'
    print 'I am eternal! I am {0} and I exist everywhere!'.format(i)

print 'I persist! My value is {0}'.format(i)
print loop_string


# We can also iterate over a dictionary!

# In[270]:


my_dict = {'firstname' : 'Inigo', 'lastname' : 'Montoya', 'nemesis' : 'Rugen'}


# In[271]:


for key in my_dict:
    print key


# If we just iterate over a dictionary without doing anything else, we will only get the keys. We can either use the keys to get the values, like so:

# In[272]:


for key in my_dict:
    print my_dict[key]


# Or we can use the `items()` function to get both key and value at the same time.

# In[273]:


for key, value in my_dict.items():
    print key, ':', value


# The `items()` function creates a tuple of each key-value pair and the for loop unpacks that tuple into `key, value` on each separate execution of the loop!

# ## Functions
# 
# A function is a reusable block of code that you can call repeatedly to make calculations, output data, or really do anything that you want. This is one of the key aspects of using a programming language. To add to the built-in functions in Python, you can define your own!

# In[274]:


def hello_world():
    """ Prints Hello, world! """
    print 'Hello, world!'

hello_world()


# In[275]:


for i in range(5):
    hello_world()


# Functions are defined with `def`, a function name, a list of parameters, and a colon. Everything indented below the colon will be included in the definition of the function.
# 
# We can have our functions do anything that you can do with a normal block of code. For example, our `hello_world()` function prints a string every time it is called. If we want to keep a value that a function calculates, we can define the function so that it will `return` the value we want. This is a very important feature of functions, as any variable defined purely within a function will not exist outside of it.

# In[281]:


def see_the_scope():
    in_function_string = "I'm stuck in here!"

see_the_scope()
print in_function_string


#  The **scope** of a variable is the part of a block of code where that variable is tied to a particular value. Functions in Python have an enclosed scope, making it so that variables defined within them can only be accessed directly within them. If we pass those values to a return statement we can get them out of the function. This makes it so that the function call returns values so that you can store them in variables that have a greater scope.
#  
# In this case specifically, including a return statement allows us to keep the string value that we define in the function.

# In[ ]:





# In[282]:


def free_the_scope():
    in_function_string = "Anything you can do I can do better!"
    return in_function_string
my_string = free_the_scope()
print my_string


# Just as we can get values out of a function, we can also put values into a function. We do this by defining our function with parameters.

# In[283]:


def multiply_by_five(x):
    """ Multiplies an input number by 5 """
    return x * 5

n = 4
print n
print multiply_by_five(n)


# In[286]:


def multiply_by_five(x):
    """ Multiplies an input number by 5 """
    return x * 5

n = 100
print n
print multiply_by_five(n)


# In this example we only had one parameter for our function, `x`. We can easily add more parameters, separating everything with a comma.

# In[287]:


def calculate_area(length, width):
    """ Calculates the area of a rectangle """
    return length * width


# In[288]:


l = 5
w = 10
print 'Area: ', calculate_area(l, w)
print 'Length: ', l
print 'Width: ', w


# In[290]:


l = 100
w = 200
print 'Area: ', calculate_area(l, w)
print 'Length: ', l
print 'Width: ', w


# In[291]:


def calculate_volume(length, width, depth):
    """ Calculates the volume of a rectangular prism """
    return length * width * depth


# If we want to, we can define a function so that it takes an arbitrary number of parameters. We tell Python that we want this by using an asterisk (`*`).

# In[292]:


def sum_values(*args):
    sum_val = 0
    for i in args:
        sum_val += i
    return sum_val


# In[293]:


print sum_values(1, 2, 3)
print sum_values(10, 20, 30, 40, 50)
print sum_values(4, 2, 5, 1, 10, 249, 25, 24, 13, 6, 4)


# In[294]:


print sum_values(2, 2, 2)
print sum_values(20, 20, 20, 20, 20)
print sum_values(249, 249, 249, 249, 249, 249, 249, 249, 249,2496, 249)


# The time to use `*args` as a parameter for your function is when you do not know how many values may be passed to it, as in the case of our sum function. The asterisk in this case is the syntax that tells Python that you are going to pass an arbitrary number of parameters into your function. These parameters are stored in the form of a tuple.

# In[295]:


def test_args(*args):
    print type(args)

test_args(1, 2, 3, 4, 5, 6)


# We can put as many elements into the `args` tuple as we want to when we call the function. However, because `args` is a tuple, we cannot modify it after it has been created.
# 
# The `args` name of the variable is purely by convention. You could just as easily name your parameter `*vars` or `*things`. You can treat the `args` tuple like you would any other tuple, easily accessing `arg`'s values and iterating over it, as in the above `sum_values(*args)` function.

# Our functions can return any data type. This makes it easy for us to create functions that check for conditions that we might want to monitor.
# 
# Here we define a function that returns a boolean value. We can easily use this in conjunction with if-statements and  other situations that require a boolean.

# In[296]:


def has_a_vowel(word):
    """ 
    Checks to see whether a word contains a vowel 
    If it doesn't contain a conventional vowel, it
    will check for the presence of 'y' or 'w'. Does
    not check to see whether those are in the word
    in a vowel context.
    """
    vowel_list = ['a', 'e', 'i', 'o', 'u']
    
    for vowel in vowel_list:
        if vowel in word:
            return True
    # If there is a vowel in the word, the function returns, preventing anything after this loop from running
    return False


# In[297]:


my_word = 'catnapping'
if has_a_vowel(my_word):
    print 'How surprising, an english word contains a vowel.'
else:
    print 'This is actually surprising.'


# In[298]:


def point_maker(x, y):
    """ Groups x and y values into a point, technically a tuple """
    return x, y


# This above function returns an ordered pair of the input parameters, stored as a tuple.

# In[299]:


a = point_maker(0, 10)
b = point_maker(5, 3)
def calculate_slope(point_a, point_b):
    """ Calculates the linear slope between two points """
    return (point_b[1] - point_a[1])/(point_b[0] - point_a[0])
print "The slope between a and b is {0}".format(calculate_slope(a, b))


# And that one calculates the slope between two points!

# In[301]:


print "The slope-intercept form of the line between a and b, using point a, is: y - {0} = {2}(x - {1})".format(a[1], a[0], calculate_slope(a, b))


# With the proper syntax, you can define functions to do whatever calculations you want. This makes them an indispensible part of programming in any language.

# ## Next Steps
# 
# This was a lot of material and there is still even more to cover! Make sure you play around with the cells in each notebook to accustom yourself to the syntax featured here and to figure out any limitations. If you want to delve even deeper into the material, the [documentation for Python](https://docs.python.org/2/) is all available online. We are in the process of developing a second part to this Python tutorial, designed to provide you with even more programming knowledge, so keep an eye on the [Quantopian Lectures Page](quantopian.com/lectures) and the [forums](quantopian.com/posts) for any new lectures.

# *This presentation is for informational purposes only and does not constitute an offer to sell, a solicitation to buy, or a recommendation for any security; nor does it constitute an offer to provide investment advisory or other services by Quantopian, Inc. ("Quantopian"). Nothing contained herein constitutes investment advice or offers any opinion with respect to the suitability of any security, and any views expressed herein should not be taken as advice to buy, sell, or hold any security or as an endorsement of any security or company.  In preparing the information contained herein, Quantopian, Inc. has not taken into account the investment needs, objectives, and financial circumstances of any particular investor. Any views expressed and data illustrated herein were prepared based upon information, believed to be reliable, available to Quantopian, Inc. at the time of publication. Quantopian makes no guarantees as to their accuracy or completeness. All information is subject to change and may quickly become unreliable for various reasons, including changes in market conditions or economic circumstances.*

# In[ ]:




