"""
CS101
HW7
Lillie Atkins
Lab X
October 31, 2017
"""

import hmmmAssembler

#GCD
#input: integers n and m
#output: GCD n (largest positive integer that evenly divides both numbers)

#register usage:
#r1 - input n and GCD n
#r2 - input m then m = n % m
#r3 - old n

GCD = """
00  read r1          #get n
01  read r2          #get m
02  jeqzn r2 07      #stop loop if m = 0
03  copy r3 r1       #r3 = r1
04  copy r1 r2       #m = n
05  mod r2 r3 r2     #m = r3 % m 
06  jumpn 02         #loop
07  write r1         #print n
08  halt             #stop the program
"""

#LCM
#input: integers n and m
#output: LCM = n*m/gcd(n, m) (the smallest number that can be evenly divided by both input numbers)

#register usage:
#r1 - input n then new n (equal to last m)
#r2 - input m then m = n % m
#r3 - old n
#r4 - m * n
#r5 - (m * n) / gcd(m,n) (LCM)

LCM = """
00  read r1             #get n
01  read r2             #get m
02  mul r4 r1 r2        #m * n
03  jeqzn r2 08         #stop loop if m = 0
04  copy r3 r1          #r3 = r1
05  copy r1 r2          #m = n
06  mod r2 r3 r2        #m = r3 (n) % m 
07  jumpn 03            #loop
08  div r5 r4 r1        #(m * n) / gcd(m,n)
09  write r5            #print LCM
10  halt                #stop program
"""

#Power
#input: two non-negative integers c and d
#output: c**d

#register usage:
#r1 - input c
#r2 - input d
#r3 - d - 1
#r4 - 1
#r5 - result c**d

Power = """
00  read r1            #get c
01  read r2            #get d
02  jeqzn r2 10        #if d = 0 skip to line 10
03  copy r5 r1         #set r5 = r1
04  setn r4 1          #set r4 = 1
05  copy r3 r2         #set r3 = r2
06  sub r3 r3 r4       #set r3 = r3 - r4 (count down of how many more loops)
07  jeqzn r3 11        #if r3 = 0 jump to line 11
08  mul r5 r5 r1       #r5 = r5 * r1
09  jumpn 06           #jump to 06 (loop)
10  setn r5 1          #set r5 to 1
11  write r5           #print the result
12  halt               #stop the program
"""

#Average
#input: z - integer representing the how many numbers will be averaged
#output: k - the average

#register usage:
#r1 - input z
#r2 - z - 1
#r3 - 1
#r4 - a (each number that will be averaged)
#r5 - sum of a's (r4 + past a's)
#r6 - k = r5 / r1 (average)

Average = """
00  read r1           #get z
01  copy r2 r1        #set r2 = r1
02  setn r3 1         #set r3 = 1
03  setn r5 0         #set r5 = 0
04  sub r2 r2 r3      #r2 = r2 - r3 (count down how many a's more to get)
05  jltzn r2 09       #stop asking for a number when you have r1 numbers
06  read r4           #get and store a number 
07  add r5 r4 r5      #sum the numbers
08  jumpn 04          #loop back to keep asking for numbers
09  div r6 r5 r1      #find the average
10  write r6          #print the average
11  halt              #stop the program
"""

#Fibonacci
#input: e (integer number of Fibonacci terms to print out)
#output: f -- e terms of the Fibonacci sequence printed (fib(n) = fib(n-1) + f(n-2), with fib(1) = fib(2) = 1)

#register usage:
#r1 - e
#r2 - r3sum + next term
#r3 - r2sum + next term
#r4 - e - 1
#r5 - 1

Fibonacci = """
00  read r1             #get e 
01  jeqzn r1 16         #stop program if r1 = 0
02  setn r2 1           #r2 = 1
03  write r2            #print 1
04  setn r3 0           #r3 = 0
05  setn r5 1           #r5 = 1
06  copy r4 r1          #r4 = r1
07  sub r4 r4 r5        #r4 = r4 - r5 (how many more loops to go through)
08  jeqzn r4 16         #stop loop if r4 = 0
09  add r3 r3 r2        #r3 = r3 + r2 (next term)
10  write r3            #print r3
11  sub r4 r4 r5        #r4 = r4 - r5
12  jeqzn r4 16         #stop loop if r4 = 0
13  add r2 r2 r3        #r2 = r3 + r2 (next term)
14  write r2            #print r2
15  jumpn 07            #loop back until all e Fib numbers are printed
16  halt                #stop program
"""