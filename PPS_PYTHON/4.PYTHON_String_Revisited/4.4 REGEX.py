#Chapter 6.11 Regex

import re

text = "hello world"

print(re.match("hello",text))

### serach 
import re 

text = "hello india welcome to chennai "

print(re.search("chennai",text))

### replace the string using REGEX

import re 

hi = "the world is seems to be great in next 5 year"

print(re.sub("5","2",hi))

#Returns all matches as a list.

import re 
text = "cars23 sludbuf543 54 4675447 hi32"

print(re.findall(r"\d+",text))