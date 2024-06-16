```
Step 1: Create a function called encode() to replace all the lowercase vowels in a given string with numbers according to the following pattern:
Step 2: Now create a function called decode() to turn the numbers back into vowels according to the same pattern shown above.

```


def encode(chars):

    vowel_to_number = {
        'a': '1',
        'e': '2',
        'i': '3',
        'o': '4',
        'u': '5'
    }
    new_chars = []
    
    for char in chars:
        if char in vowel_to_number:
            new_chars.append(vowel_to_number[char])
        else:
            new_chars.append(char)
    return ''.join(new_chars)
        
def decode(chars):
    number_to_vowel = {
        '1': 'a',
        '2': 'e',
        '3': 'i',
        '4': 'o',
        '5': 'u'
    }    
    
    new_chars = []
    
    for char in chars:
        if char in number_to_vowel:
            new_chars.append(number_to_vowel[char])
        else:
            new_chars.append(char)
    return ''.join(new_chars)
