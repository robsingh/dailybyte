"""
In this Bite you complete print_hanging_indents to print a poem (or text) in a nicer way.

For example calling it on (part of) Christina Rosetti's Remember it should convert:

                      Remember me when I am gone away,
                      Gone far away into the silent land;
                      When you can no more hold me by the hand,

                      Nor I half turn to go yet turning stay.

                      Remember me when no more day by day
                      You tell me of our future that you planned:
                      Only remember me; you understand
to:

Remember me when I am gone away,
    Gone far away into the silent land;
    When you can no more hold me by the hand,
Nor I half turn to go yet turning stay.
Remember me when no more day by day
    You tell me of our future that you planned:
    Only remember me; you understand
print the resulting poem (don't return it)! The tests include another text snippet from Shakespeare. Have fun!
"""

import re

def print_hanging_indents(poem):
    for line in poem.split('\n'):
        if re.match(r'\s+',line):
            print(line)
        else:
            print(re.sub(r'(.+) ', r'\1 ', line))

poem = """
Remember me when I am gone away,
Gone far away into the silent land;
When you can no more hold me by the hand,

Nor I half turn to go yet turning stay.

Remember me when no more day by day
You tell me of our future that you planned:
Only remember me; you understand
"""

print_hanging_indents(poem)