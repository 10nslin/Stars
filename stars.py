'''
Scott Enslin
part 1 Create a function called draw_stars() that takes a list of numbers and prints out *.

part 2

Modify the function above. Allow a list containing integers and strings to be passed to the draw_stars() function. 
When a string is passed, instead of displaying *, display the first letter of the string according to the example below. 
You may use the .lower() string method for this part.

'''

x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
def draw_stars(alist):
    
    
    for char in alist:
        if isinstance(char, str):
            print char[0].lower()*len(char)
        elif isinstance(char, int):
            print "*" * char

draw_stars(x)


