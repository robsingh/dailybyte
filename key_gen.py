"""
Write a function called gen_key that creates a license key with this format: KI80OMZ7-5OGYC1AC-735LDPT1-4L11XU1U

The key consists of a combination of upper case letters and digits.

It takes two arguments: parts and chars_per_part which default to 4 and 8 respectively, so you can call the function like:

gen_key() to get a similar key as above, or
as gen_key(parts=3, chars_per_part=4) to get a shorter one, e.g. 54N8-I70K-2JZ7
"""

import random
import string

def gen_key(*, parts=4, chars_per_part=8):
    key_parts = []
    for _ in range(parts):
        part = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(chars_per_part))
        key_parts.append(part)

    return '-'.join(key_parts)    


print(gen_key(parts=3,chars_per_part=4))