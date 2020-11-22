import numpy
import math
import tensorflow as tf

# import math 
# print(math.pi, math.log(32, 2))
# or use:
# import math as mt
# print(mt.pi, mt.log(32, 2))
# or use:
# from math import log, pi
# print(pi, log(32, 2))
# or use:
# from math import *
# print(pi, log(32, 2))

def least_difference(a, b, c):
    """Return the smallest difference between any two numbers
    among a, b and c.
    
    >>> least_difference(1, 5, -5)
    4
    """
    diff1 = abs(a - b)
    diff2 = abs(b - c)
    diff3 = abs(a - c)
    return min(diff1, diff2, diff3)

def greet(who="Colin"):
    """Example of a function with default value"""
    print("Hello ", who)

def mult_by_five(x):
    return 5 * x

def call(fn, arg):
    """Call fn on arg"""
    return fn(arg)

def squared_call(fn, arg):
    """Call fn on the result of calling fn on arg"""
    return fn(fn(arg))    

def mod_5(x):
    """Return the remainder of x after dividing by 5"""
    return x % 5

def using_round():
    # test code
    print(
        'Original value',
        123456.789012,
        'Round with negative argument round(123456.789012, -2)',
        round(123456.789012, -2),
        'Round with positive argument round(123456.789012, 2)',
        round(123456.789012, 2),
        'Round with 0 value argument round(123456.789012, 0)',
        round(123456.789012, 0),
        'Round with no argument round(123456.789012)',
        round(123456.789012),
        sep='\n'
    )

def is_odd(n):
    return (n % 2) == 1

def can_run_for_president(age, is_natural_born_citizen):
    """Can someone of the given age and citizenship status run for president in the US?"""
    # The US Constitution says you must be a natural born citizen *and* at least 35 years old
    return is_natural_born_citizen and (age >= 35)

def inspect(x):
    if x == 0:
        print(x, "is zero")
    elif x > 0:
        print(x, "is positive")
    elif x < 0:
        print(x, "is negative")
    else:
        print(x, "is unlike anything I've ever seen...")    

def should_hit(dealer_total, player_total, player_low_aces, player_high_aces):
    """Return True if the player should hit (request another card) given the current game
    state, or False if the player should stay.
    When calculating a hand's total value, we count aces as "high" (with value 11) if doing so
    doesn't bring the total above 21, otherwise we count them as low (with value 1). 
    For example, if the player's hand is {A, A, A, 7}, we will count it as 11 + 1 + 1 + 7,
    and therefore set player_total=20, player_low_aces=2, player_high_aces=1.
    """
    return False     

def fashionably_late(arrivals, name):
    """Given an ordered list of arrivals to the party and a name, return whether the guest with that
    name was fashionably late.
    We're using lists to record people who attended our party and what order they arrived in. 
    For example, the following list represents a party with 7 guests, in which Adela showed up first and Ford was the last to arrive:

    party_attendees = ['Adela', 'Fleda', 'Owen', 'May', 'Mona', 'Gilbert', 'Ford']

    A guest is considered 'fashionably late' if they arrived after at least half of the party's guests. 
    However, they must not be the very last guest (that's taking it too far). 
    In the above example, Mona and Gilbert are the only guests who were fashionably late.

    Complete the function below which takes a list of party attendees as well as a person, and tells us whether that person is fashionably late.

    """
    indice = arrivals.index(name)
    tam = len(arrivals)
    print('arrivals: ', arrivals)
    print('indice: ', indice)
    print('tam: ', tam)
    
    return not ((indice < (tam/2)) or (indice == (tam-1)))

def count_negatives1(nums):
    """Return the number of negative numbers in the given list.
    
    >>> count_negatives([5, -1, -2, 0, 3])
    2
    """
    n_negative = 0
    for num in nums:
        if num < 0:
            n_negative = n_negative + 1
    return n_negative

def count_negatives2(nums):
    return len([num for num in nums if num < 0])

def count_negatives3(nums):
    return sum([num < 0 for num in nums])

def has_lucky_number(nums):
    """Return whether the given list of numbers is lucky. A lucky list contains
    at least one number divisible by 7.
    """
    return any([num % 7 == 0 for num in nums])
    
def elementwise_greater_than(L, thresh):
    """Return a list with the same length as L, where the value at index i is 
    True if L[i] is greater than thresh, and False otherwise.
    
    >>> elementwise_greater_than([1, 2, 3, 4], 2)
    [False, False, True, True]
    """
    return [ele > thresh for ele in L]

def menu_is_boring(meals):
    """Given a list of meals served over some period of time, return True if the
    same meal has ever been served two days in a row, and False otherwise.
    """
    for i in range(len(meals)-1):
        if meals[i] == meals[i+1]:
            return True
    return False

def is_valid_USA_zip(zip_str):
    return len(zip_str) == 5 and zip_str.isdigit()

def word_search(documents, keyword):
    # list to hold the indices of matching documents
    indices = [] 
    # Iterate through the indices (i) and elements (doc) of documents
    for i, doc in enumerate(documents):
        # Split the string doc into a list of words (according to whitespace)
        tokens = doc.split()
        # Make a transformed list where we 'normalize' each word to facilitate matching.
        # Periods and commas are removed from the end of each word, and it's set to all lowercase.
        normalized = [token.rstrip('.,;').lower() for token in tokens]
        # Is there a match? If so, update the list of matching indices.
        if keyword.lower() in normalized:
            indices.append(i)
    return indices

def multi_word_search(documents, keywords):
    keyword_to_indices = {}
    for keyword in keywords:
        keyword_to_indices[keyword] = word_search(documents, keyword)
    return keyword_to_indices

if __name__ == '__main__':
    
    #example 1
    print("#example 1")
    print(least_difference(1,10,100),
        least_difference(1,10,10),
        least_difference(5,6,7)
    )
    
    #example 2
    print("\n#example 2")
    greet()
    greet("Luis")

    #example 3
    print("\n#example 3")
    print(
        call(mult_by_five, 1),
        squared_call(mult_by_five, 1), 
        sep='\n', # '\n' is the newline character - it starts a new line
    )

    #example 4
    print("\n#example 4")
    print(
        'Which number is biggest?',
        max(100, 51, 14),
        'Which number is the biggest modulo 5?',
        max(100, 51, 14, key=mod_5),
        sep='\n',
    )

    #example 5
    print("\n#example 5")
    using_round()

    #example 6
    print("\n#example 6")
    print("Is 100 odd?", is_odd(100))
    print("Is -1 odd?", is_odd(-1))

    #example 7
    print("\n#example 7")
    print("Can run for president (age, is_natural_born_citizen) (19,True)", 
        can_run_for_president(19, True), sep=' > '
    )
    print("Can run for president (age, is_natural_born_citizen) (55,False)",
        can_run_for_president(55, False), sep=' > '
    )
    print("Can run for president (age, is_natural_born_citizen) (55,True)", 
        can_run_for_president(55, True), sep=' > '
    )

    #example 8
    print("\n#example 8")
    inspect(0)
    inspect(15)
    inspect(-15)
    
    #example 9
    print("\n#example 9")
    print("bool(1)", bool(1)) # all numbers are treated as true, except 0
    print("bool(0)", bool(0))
    print("bool('asf')", bool("asf")) # all strings are treated as true, except the empty string ""
    print("bool('')", bool(""))
    # Generally empty sequences (strings, lists, and other types we've yet to see like lists and tuples)
    # are "falsey" and the rest are "truthy"
    # We can use non-boolean objects in if conditions and other places where a boolean would be expected.
    # Python will implicitly treat them as their corresponding boolean value:
    if 0:
        print(0)
    elif "spam":
        print("spam")

    
    #example 10
    print("\n#example 10")
    print("Lists")
    print("\nPlanetas")
    planets = ['Mercury', 'Venus', 'Earth', 'Malacandra', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    print(planets)
    print("The first item planets[0] => ", planets[0])
    print("The last item planets[-1] => ", planets[-1])
    print("len => ", len(planets))
    print("sorted => ", sorted(planets))
    planets.append('Pluto')
    print("append => ", planets) 
    print("Remove last item - pop => ", planets.pop())
    print(planets)
    print("index('Earth') => ", planets.index('Earth'))
    print("'Earth' in planets => ", "Earth" in planets)

    print("\nPrimos")
    primes = [2, 3, 5, 7]
    print(primes)
    print("sum => ", sum(primes))
    print("max => ", max(primes))
    print("min => ", min(primes))

    #example 11
    print("\n#example 11")
    print("Tuples")
    t = (1, 2, 3)
    print(t)
    t = 1, 2, 3
    print(t)
    x = 0.125
    print("as_integer_ratio of 0.125 => ", x.as_integer_ratio())
    numerator, denominator = x.as_integer_ratio()
    print("numerator / denominator = x.as_integer_ratio() => ", numerator / denominator)
    print("\nClassic Stupid Python Trick")
    print("a = 1")
    print("b = 0")
    print("a, b = b, a")
    a = 1
    b = 0
    a, b = b, a
    print("a = ", a)
    print("b = ", b)

    #example 12
    print("\n#example 12")
    print(fashionably_late(['Adela', 'Fleda', 'Owen', 'May', 'Mona', 'Gilbert', 'Ford'], 'Adela'))
    print(fashionably_late(['Adela', 'Fleda', 'Owen', 'May', 'Mona', 'Gilbert', 'Ford'], 'Fleda'))
    print(fashionably_late(['Adela', 'Fleda', 'Owen', 'May', 'Mona', 'Gilbert', 'Ford'], 'Owen'))
    print(fashionably_late(['Adela', 'Fleda', 'Owen', 'May', 'Mona', 'Gilbert', 'Ford'], 'May'))
    print(fashionably_late(['Adela', 'Fleda', 'Owen', 'May', 'Mona', 'Gilbert', 'Ford'], 'Mona'))
    print(fashionably_late(['Adela', 'Fleda', 'Owen', 'May', 'Mona', 'Gilbert', 'Ford'], 'Gilbert'))
    print(fashionably_late(['Adela', 'Fleda', 'Owen', 'May', 'Mona', 'Gilbert', 'Ford'], 'Ford'))

    #example 13
    print("\n#example 13")
    print("\nLoop for in with List")
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    print(planets)
    for planet in planets:
        print(planet, end=' ') # print all on same line
    
    print("\n\nLoop for in with Tuples")
    multiplicands = (2, 2, 2, 3, 3, 5)
    print ("multiplicands", multiplicands)
    product = 1
    for mult in multiplicands:
        product = product * mult
    print (product)

    print("\nLoop for in with char/string")
    s = 'steganograpHy is the practicE of conceaLing a file, message, image, or video within another fiLe, message, image, Or video.'
    msg = ''
    print ("print all the uppercase letters in s, one at a time")
    print ("s = 'steganograpHy is the practicE of conceaLing a file, message, image, or video within another fiLe, message, image, Or video.'")
    # print all the uppercase letters in s, one at a time
    for char in s:
        if char.isupper():
            print(char, end='') 
    print("\n")

    print("Loop for in with range")
    for i in range(5):
        print("Doing important work. i =", i)

    print("\nWhile Loops")
    i = 0
    while i < 10:
        print(i, end=' ')
        i += 1        
    print("\n")

    print("List comprehensions")
    print("List comprehensions are one of Python's most beloved and unique features.", \
        "The easiest way to understand them is probably to just look at a few examples:")
    
    print("\n")
    print("squares = [n**2 for n in range(10)]")
    squares = [n**2 for n in range(10)]
    print("squares => ",squares)
    
    print("\n")
    print("short_planets = [planet for planet in planets if len(planet) < 6]")
    short_planets = [planet for planet in planets if len(planet) < 6]
    print("squares => ",short_planets)

    print("\n")
    print("If you're familiar with SQL, you might think of this as being like a 'WHERE' clause")
    print("Here's an example of filtering with an if condition and applying some transformation to the loop variable:")
    print("\nshort_planets = [planet for planet in planets if len(planet) < 6]")
    loud_short_planets = [planet.upper() + '!' for planet in planets if len(planet) < 6]
    print("loud_short_planets => ",loud_short_planets)

    print("\n")
    print("People usually write these on a single line, but you might find the structure clearer when it's split up over 3 lines:")
    print("[")
    print("    planet.upper() + '!'")
    print("    for planet in planets")
    print("    if len(planet) < 6")
    print("]")
    loud_short_planets = \
        [
            planet.upper() + '!' 
            for planet in planets 
            if len(planet) < 6
        ]
    print("loud_short_planets => ",loud_short_planets)

    print("\n")
    print("The expression on the left doesn't technically have to involve the loop variable (though it'd be pretty unusual for it not to).", \
        "\nWhat do you think the expression below will evaluate to? Press the 'output' button to check.")
    print("\n[32 for planet in planets]")
    print([32 for planet in planets])
    
    print("\n")
    print("Return the number of negative numbers in the given list.")
    print("\n")
    print("count_negatives1([5, -1, -2, 0, 3]) normal")
    print(count_negatives1([5, -1, -2, 0, 3]))
    print("\n")
    print("count_negatives2([5, -1, -2, 0, 3]) List Comprehension")
    print(count_negatives2([5, -1, -2, 0, 3]))
    print("\n")
    print("count_negatives3([5, -1, -2, 0, 3]) List Comprehension optimized")
    print(count_negatives3([5, -1, -2, 0, 3]))
    
    #example 14
    print("\n#example 14")
    print("\nExercises")
    print("\nhas_lucky_number([])")
    print(has_lucky_number([]))    
    print("\nhas_lucky_number([3, 14])")
    print(has_lucky_number([3, 14]))
    print("\nhas_lucky_number([3, 1, 18, 221])")
    print(has_lucky_number([3, 1, 18, 221]))
    print("\nhas_lucky_number([3, 1, 18, 700])")
    print(has_lucky_number([3, 1, 18, 700]))

    print("\nelementwise_greater_than([1, 2, 3, 4], 2)")
    print(elementwise_greater_than([1, 2, 3, 4], 2))

    print("\nmenu_is_boring([])")
    print(menu_is_boring([]))
    print("\nmenu_is_boring(['pasta'])")
    print(menu_is_boring(['pasta']))
    print("\nmenu_is_boring(['rice', 'beans', 'pasta', 'meat'])")
    print(menu_is_boring(['rice', 'beans', 'pasta', 'meat']))
    print("\nmenu_is_boring(['rice', 'beans', 'pasta', 'meat', 'meat'])")
    print(menu_is_boring(['rice', 'beans', 'pasta', 'meat', 'meat']))
    print("\nmenu_is_boring(['rice', 'beans', 'beans', 'salad', 'salad', 'pasta', 'meat', 'meat'])")
    print(menu_is_boring(['rice', 'beans', 'beans', 'salad', 'salad', 'pasta', 'meat', 'meat']))


    #example 15
    print("\n#example 15")
    print("\nString Examples")
    
    print("\nBackslash in strings")
    print("\nExample 'What\\'s up?'") # put the result of this print() in the next print()
    print('What\'s up?')
    
    print('\n"That\'s \\"cool\\""') # put the result of this print() in the next print()
    print("That's \"cool\"")

    print('\n"Look, a mountain: /\\\\"') # put the result of this print() in the next print()
    print("Look, a mountain: /\\")

    print('\n"1\\n2 3"') # put the result of this print() in the next print()
    print("1\n2 3")

    print("\n")
    hello = "hello\nworld"
    print(hello)
    print("In addition, Python's triple quote syntax for strings lets us include newlines literally", \
        "(i.e. by just hitting 'Enter' on our keyboard, rather than using the special '\n' sequence).", \
        "We've already seen this in the docstrings we use to document our functions, but we can use them anywhere we want to define a string.")
    triplequoted_hello = """hello
world"""
    print(triplequoted_hello)
    print("triplequoted_hello == hello")
    print(triplequoted_hello == hello)

    print("\n# Indexing String")
    print(planet)
    planet = 'Pluto'
    print(planet)
    print(planet[0])
    print("\n# Slicing")
    print(planet[-3:])

    print("\n# All Caps")
    claim = "Pluto is a planet!"
    print('claim => ', claim)
    print(claim.upper())
    print("\n# all lowercase")
    print(claim.lower())
    print("\n# Searching for the first index of a substring")
    print(claim.index('plan'))
    print("claim.startswith(planet)")
    print(claim.startswith(planet))
    print("claim.endswith('dwarf planet')")
    print(claim.endswith('dwarf planet'))    

    words = claim.split()
    print(words)

    datestr = '1956-01-31'
    print("datestr = '1956-01-31'")
    year, month, day = datestr.split('-')
    print("year, month, day = datestr.split('-')")
    print(year, month, day)

    datestr = '1956-01-31'
    print("'/'.join([month, day, year])")
    strjoin ='/'.join([month, day, year])
    print(strjoin)

    print("' 👏 '.join([word.upper() for word in words])")
    strjoin = ' 👏 '.join([word.upper() for word in words])
    print(strjoin)

    position = 9
    strjoin = planet + ", you'll always be the " + str(position) + "th planet to me."
    print(strjoin)

    strjoin = "{}, you'll always be the {}th planet to me.".format(planet, position)
    print(strjoin)

    pluto_mass = 1.303 * 10**22
    earth_mass = 5.9722 * 10**24
    population = 52910390
    # 2 decimal points   3 decimal points, format as percent, separate with commas
    strjoin = "{} weighs about {:.2} kilograms ({:.3%} of Earth's mass). It is home to {:,} Plutonians.".format(
        planet, pluto_mass, pluto_mass / earth_mass, population,
    )
    print(strjoin)

    # Referring to format() arguments by index, starting from 0
    s = """Pluto's a {0}.
No, it's a {1}.
{0}!
{1}!""".format('planet', 'dwarf planet')
    print(s)

    #example 16
    print("\n#example 16")
    print("\nDictionaries Examples")
    
    print("numbers = {'one':1, 'two':2, 'three':3}")    
    numbers = {'one':1, 'two':2, 'three':3}
    print(numbers)
    print("numbers['one']")
    print(numbers['one'])
    print("numbers['eleven'] = 11")
    numbers['eleven'] = 11
    print(numbers)
    print("numbers['one'] = 'Pluto'")
    numbers['one'] = 'Pluto'
    print(numbers)
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    print(planets)
    planet_to_initial = {planet: planet[0] for planet in planets}
    print("planet_to_initial = {planet: planet[0] for planet in planets}")
    print(planet_to_initial)
    print("'Saturn' in planet_to_initial", 'Saturn' in planet_to_initial)
    print(planet_to_initial)
    print("'Betelgeuse' in planet_to_initial", 'Betelgeuse' in planet_to_initial)
    for k in numbers:
        print("{} = {}".format(k, numbers[k]))

    # Get all the initials, sort them alphabetically, and put them in a space-separated string.
    strjoin = ' '.join(sorted(planet_to_initial.values()))
    print(strjoin)

    for planet, initial in planet_to_initial.items():
        print("{} begins with \"{}\"".format(planet.rjust(10), initial))

    print("is_valid_USA_zip('') => ", is_valid_USA_zip(''))
    print("is_valid_USA_zip('1234x') => ", is_valid_USA_zip('1234x'))
    print("is_valid_USA_zip('1234') => ", is_valid_USA_zip('1234'))
    print("is_valid_USA_zip('12345') => ", is_valid_USA_zip('12345'))

    documents=['The Learn Python Challenge Casino', 'They bought a car, and a horse', 'Casinoville?']
    keyword='car'
    print(word_search(documents, keyword))

    documents=['The Learn Python Challenge Casino', 'They bought a car, and a horse', 'Casinoville?']
    keyword='Casino'
    print(word_search(documents, keyword))

    documents=['The Learn Python Challenge Casino', 'They bought a car', 'Casinoville?']
    keywords=['car', 'Casino']
    print(multi_word_search(documents, keywords))

    documents=['The Learn Python Challenge Casino', 'They bought a car', 'Casinoville?']
    keywords=[]
    print(multi_word_search(documents, keywords))

    documents=['The Learn Python Challenge Casino', 'They bought a car', 'Casinoville?']
    keywords=['Learn', 'car']
    print(multi_word_search(documents, keywords))        



    #example 16
    print("\n#example 16")
    print("\nLibrary Math and NumPy")
    print("It's math! It has type {}".format(type(math)))
    print(dir(math))
    print("\npi to 4 significant digits = {:.4}".format(math.pi))
    print("\nLog in Math: Return the logarithm of x to the given base. Ex. math.log(32, 2) => ", math.log(32, 2))
    print("\nPI value in Math Ex. math.pi => ", math.pi)
    print("\nnumpy.random is a", type(numpy.random))
    print("it contains names such as...",
      dir(numpy.random)[-15:]
     )
    print("\nSo if we import numpy as above, then calling a function in the random 'submodule' will require two dots.")
    print("rolls = numpy.random.randint(low=1, high=6, size=10)")
    rolls = numpy.random.randint(low=1, high=6, size=10)
    print('rolls => ', rolls)
    print('\ntype() (what is this thing?). Example: type(rolls) => ', type(rolls))    
    print('\ndir() (what can I do with it?). Example: dir(rolls) => \n\n', dir(rolls))    
    print("\nWhat am I trying to do with this dice roll data? Maybe I want the average roll, in which case the 'mean'")
    print('method looks promising...')
    print('\nrolls.mean() =>', rolls.mean())
    print("\nOr maybe I just want to get back on familiar ground, in which case I might want to check out 'tolist'")
    print('\nrolls.tolist() =>', rolls.tolist())
    print('\nrolls + 10 => ',rolls + 10)
    print("""
    We might think that Python strictly polices how pieces of its core syntax behave such as +, <, in, ==, or square brackets for indexing and slicing. But in fact, it takes a very hands-off approach. When you define a new type, you can choose how addition works for it, or what it means for an object of that type to be equal to something else.

The designers of lists decided that adding them to numbers wasn't allowed. The designers of numpy arrays went a different way (adding the number to each element of the array).

Here are a few more examples of how numpy arrays interact unexpectedly with Python operators (or at least differently from lists).
    """)
    print('\nrolls <= 3', rolls <= 3)
    print('\nxlist = [[1,2,3],[2,4,6],] -> Create a 2-dimensional array')
    xlist = [[1,2,3],[2,4,6],]
    print('\nx = numpy.asarray(xlist)')
    x = numpy.asarray(xlist)
    print("xlist = {}\nx = {}".format(xlist, x))
    print("\nGet the last element of the second row of our numpy array")
    print("x[1,-1] => ", x[1,-1])
    print("\nGet the second element of the first row of our numpy array")
    print("x[0,1] => ", x[0,1])
 
    #example 17
    print("\n#example 17")
    print("\nLibrary Tensorflow")
    print("\nCreate two constants, each with value 1")
    print("a = tf.constant(1)")
    print("b = tf.constant(1)")
    a = tf.constant(1)
    b = tf.constant(1)
    print("\nAdd them together to get...")
    print("a + b => ", a + b)
    
    print("""
a + b isn't 2, it is (to quote tensorflow's documentation)...

a symbolic handle to one of the outputs of an Operation. It does not hold the values of that operation's output, but instead provides a means of computing those values in a TensorFlow tf.Session.

It's important just to be aware of the fact that this sort of thing is possible and that libraries will often use operator overloading in non-obvious or magical-seeming ways.

Understanding how Python's operators work when applied to ints, strings, and lists is no guarantee that you'll be able to immediately understand what they do when applied to a tensorflow Tensor, or a numpy ndarray, or a pandas DataFrame.

Once you've had a little taste of DataFrames, for example, an expression like the one below starts to look appealingly intuitive:

# Get the rows with population over 1m in South America
df[(df['population'] > 10**6) & (df['continent'] == 'South America')]
But why does it work? The example above features something like 5 different overloaded operators. What's each of those operations doing? It can help to know the answer when things start going wrong.

Curious how it all works?
Have you ever called help() or dir() on an object and wondered what the heck all those names with the double-underscores were?

print(dir(list))
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
This turns out to be directly related to operator overloading.

When Python programmers want to define how operators behave on their types, they do so by implementing methods with special names beginning and ending with 2 underscores such as __lt__, __setattr__, or __contains__. Generally, names that follow this double-underscore format have a special meaning to Python.

So, for example, the expression x in [1, 2, 3] is actually calling the list method __contains__ behind-the-scenes. It's equivalent to (the much uglier) [1, 2, 3].__contains__(x).

If you're curious to learn more, you can check out Python's official documentation, which describes many, many more of these special "underscores" methods.

We won't be defining our own types in these lessons (if only there was time!), but I hope you'll get to experience the joys of defining your own wonderful, weird types later down the road.
"""    
    )