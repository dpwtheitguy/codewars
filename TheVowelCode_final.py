```
Step 1: Create a function called encode() to replace all the lowercase vowels in a given string with numbers according to the following pattern:
Step 2: Now create a function called decode() to turn the numbers back into vowels according to the same pattern shown above.

```

def encode(s, t=str.maketrans("aeiou", "12345")):
    return s.translate(t)
    
def decode(s, t=str.maketrans("12345", "aeiou")):
    return s.translate(t)
