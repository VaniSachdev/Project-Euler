# Active Learning! 
In an effort to actively learn and improve my skills I have developed a routine so that I get as much as I can from this experience:

 1. Work on a problem (no internet/stalk overflowing) until it is solved to truly gain a sense of how much knowledge I have at that moment. 
 2. Google questions/ read through [Stalk Overflow](https://stackoverflow.com) forums to see if there is a more efficient way to solve the problem/find different ways to solve the question. 
 3. Incorporate concepts I learned from Step2 into my program (no copy/pasting, old code is commented out if I change the code too much). 
 4. Note down any new concepts/functions/libraries/etc I learned. 

### Don't Judge Me Please!

This is more for me to have something to refer to as I progress both in Project Euler and in my programming journey as a whole. The point of this experience is to learn and strengthen my skills, so identifying my weaknesses are important. 

Also, the notes added aren't very coherent if you're not me; this is more of a document for me to come back to than a place to learn from. 
 
## Question Breakdown

|       Project Number          |Project Summary                          |New Skills/Concepts/Clarifications/Etc                         |
|----------------|-------------------------------|-----------------------------|
|1|Find the sum of all the multiples of 3 or 5 below 100          |N/A           |
|2          |Sum of the even-valued terms of the Fibonacci sequence whose values do not exceed four million     |N/A            |
|3         |Largest prime factor of the number 600851475143|Use step 2 because even numbers are not prime (50% faster), check the factors of a number till the square root of said number to further make the function a speedy boi, use “2 way table” technique (continuously divide number by a prime #)|
|4|Largest palindrome made from the product of two 3-digit numbers      |Reverse arrays w/ splicing w/ `[start:stop:end]`. If start & stop are omitted, whole list is selected so `[::-1]` effectively spits back the reverse          |
|5          |Smallest positive number that is evenly divisible by all of the numbers from 1 to 20        |I have a tendency to try to write everything in one function; use multiple functions and capitalize on the fact that booleans existing           |
|6         |Difference between the sum of the squares of the first one hundred natural numbers and the square of the sum|N/A|
|7|10,001st prime number      |[Sieve of Eratosthenes:](https://youtu.be/klcIklsWzrY) used to find all prime numbers up to any given limit (include the optimization of starting from a prime's square); Calculate the upper limit for nth prime with the following formula $$p_n <= n \cdot  log (n) + n \cdot log(log (n))     \\( if n >= 6)$$ |
|8          |Thirteenth adjacent digits in the 1000-digit number that have the greatest product of this number       |Using reduce (from [library functools](https://docs.python.org/3/library/functools.html)) to iterate and perform functions on a list           |
|9         |There exists exactly one Pythagorean triplet for which a + b + c = 1000|N/A|
|10|Sum of all the primes below two million |Used what I learned in Problem 3 (to check if a number is prime only check until sqrt of number)            |
|11          |Greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20×20 grid   |Use `‘’’` for multiline strings (`/n` are accounted for by default); Used `.strip()` (to get rid of spaces) and `.splitLines()` (to save each pre `/n` as it’s on element); New one line for loop structure `[return x for i in range(z)]`|
|12        |Value of the first triangle number to have over five hundred divisors|Learned the most efficient function to return all the factors of a number (divide the number by 1 to the square root of that number (+1) and added both the number it was divisible by and the number it’s corresponding factor (number/element) for the desired range) (Makes more sense if you look at the function)|
|13 |First ten digits of the sum of the following one-hundred 50-digit numbers        |Used map to convert each element in a string to an integer, used reduce & lambda from library functools again to add each element in a large number            |
|14         |Find a starting number (under one million) that produces the longest chain by the Collatz Problem          |N/A            |
|15         |Maximum number of lattice routes through a 20×20 grid|Lattice path (only goes right & up/left & down); Assuming (0,0) is the starting point, there exists a [formula](https://en.wikipedia.org/wiki/Binomial_coefficient) relating to the binomial coefficient to calculate all the possible paths to (a,b)|
|16         |Sum of the digits of the number: $$ 2^{1000} $$|Learned that [map](https://www.geeksforgeeks.org/python-map-function/) doesn't do what I originally thought it did; read some documentation and learned that it doesn't return a list but instead a map object (an iterator). Other than that, this one was pretty easy.  |
|17         |Add the length of the numbers (in words) from 1 to 1000 (no spaces, dashes)f |imports save lives! read about a function `num2words`a while ago that spits back a number in words which ended up making this process easier; to get rid of spaces and dashes I created a list with those two chars and used a foor loop + the replace method; if the function num2words didn't exist I would've saved each digit, eleven-nineteen, hundred, etc in seperate lists and used foor loops, boolean flags, and logic-based math to solve |
|19         |Determine how many Sundays fell on the first of the month during the twentieth century|imports save lives one again! imported calendar, read some documentatoin, and did it pretty easily; was a little confused why my solution wasnt working at first (i assumed the matrix had the 0th element as sunday (it was the 6th); read a few stack overflow posts & figured it out|
|20         |Sum of digits in 100!| N/A |
|21         |Amicable Numbers (sum of the factors of number n equals x; sum of factors of x equals n) | used sets! instead of lists! yay for automatic duplicate checking|

Something I'm seeing a lot is that a lot of the time mathematical formulas exist for these sort of questions and they make life nicer & code faster -- who would've guessed that math and computer science are friends! 

### Questions that gave me a tough time:
[11](https://projecteuler.net/problem=11), [15](https://projecteuler.net/problem=15)

## Resources 

I read a lot of Project Euler blogs to learn new ways to optimize my code. While I don't copy/paste code, reading and learning from other programmers has been very beneficial in my coding experience as a whole. 

I consulted/consult the following blogs fairly often:

 - [MikeYaworski](https://code.mikeyaworski.com/python/project_eu) 
 - [Ramon's Math Blog](https://ramonsmathsblog.wordpress.com/project-euler/) 
 - [Radius of a Circle](https://radiusofcircle.blogspot.com) 


 I also use[Stalk Overflow](https://stackoverflow.com) ,  [Wikipedia](https://www.wikipedia.org) and [Khan Academy](https://www.khanacademy.org). 
