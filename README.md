[![Downloads](https://static.pepy.tech/personalized-badge/fizzbuzz2?period=total&units=none&left_color=grey&right_color=blue&left_text=Downloads)](https://pepy.tech/project/fizzbuzz2)

# FizzBuzz2
A powerful fizz buzz engine.

## Overview
Can't you implement Fizz Buzz? No problem! This module solves everything.

## Installation
```
$ pip install fizzbuzz2
```

## Usage
```
>>> from fizzbuzz import FizzBuzz
>>> print(FizzBuzz())
1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, Fizz Buzz, ..., 97, 98, Fizz, Buzz
```

## API
### Preparation
```
>>> from fizzbuzz import FizzBuzz
```
### Configuration Parameters
```
>>> FizzBuzz.fizz
'Fizz'
>>> FizzBuzz.buzz
'Buzz'
>>> FizzBuzz.fizzbuzz
'Fizz Buzz'
>>> FizzBuzz.delimiter
', '
```
### Judgement Method
```
>>> FizzBuzz.judge(6)
'Fizz'
>>> FizzBuzz.judge(20)
'Buzz'
>>> FizzBuzz.judge(30)
'Fizz Buzz'
>>> FizzBuzz.judge(31)
'31'
```
### Creating a FizzBuzz Generator
```
>>> gen = FizzBuzz.generate(start=1, end=100)
>>> print(list(gen))
['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', ..., '98', 'Fizz', 'Buzz']
```
### Creating a FizzBuzz Instance
```
>>> fb = FizzBuzz(start=1, end=100))
>>> print(fb)
1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, Fizz Buzz, ..., 97, 98, Fizz, Buzz
```
### Example
```
>>> FizzBuzz.fizz = 'fizz'
>>> FizzBuzz.buzz = 'buzz'
>>> FizzBuzz.fizzbuzz = 'fizzbuzz'
>>> FizzBuzz.delimiter = '\n'
>>> print(FizzBuzz(start=9, end=15))
fizz
buzz
11
fizz
13
14
fizzbuzz
```

## CLI
### Arguments
```
$ fizzbuzz -h
usage: fizzbuzz [-h] [-s start] [-e end] [-f fizz] [-b buzz] [-z fizzbuzz] [-d delimiter]

a powerful fizz buzz engine.

options:
  -h, --help    show this help message and exit
  -s start      start with this number. (default: 1)
  -e end        end with this number. (default: 100)
  -f fizz       replace "Fizz" string. (default: Fizz)
  -b buzz       replace "Buzz" string. (default: Buzz)
  -z fizzbuzz   replace "Fizz Buzz" string. (default: Fizz Buzz)
  -d delimiter  replace the word delimiter. (default: , )
```
### Example 1
```
$ fizzbuzz
1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, Fizz Buzz, ..., 97, 98, Fizz, Buzz
```
### Example 2
```
$ fizzbuzz -s 9 -e 15 -f fizz -b buzz -z fizzbuzz -d '\n'
fizz
buzz
11
fizz
13
14
fizzbuzz
```
