"""
Write a function called get_profile that only allows 2 keyword arguments: name and profession which default to julian and programmer respectively.

The function does nothing fancy, just return a str: name is a profession.

The point is to limit the interface of this function and you'll see Python makes it very easy ... have fun!

"""
# * before the function parameters indicate that the function only accepts keyword arguments. 

def get_profile(*, name, profession) -> str:
    return f'{name} is a {profession}'



print(get_profile(name="julian", profession="programmer"))