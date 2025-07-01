"""
You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. We want to create the text that should be displayed next to such an item.
Implement the function which takes an array containing the names of people that like an item. It must return the display text as shown in the examples:

[]                                -->  "no one likes this"
["Peter"]                         -->  "Peter likes this"
["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"

"""

arr = ["Alex", "Jacob", "Mark", "Max", "Mark", "Max", "Mark", "Max"]
def likes(names : list):
    if len(names) == 1:
        return "".join(names) + " likes this"
    elif len(names) == 2:
        return "".join(names[0]) + " and " + "".join(names[1]) + " like this"
    elif len(names) == 3:
        return "".join(names[0]) + ", " + "".join(names[1]) + " and " + "".join(names[2]) + " like this"
    elif len(names) > 3: 
        return "".join(names[0]) + ", " + "".join(names[1]) + " and " + str(len(arr[2:])) + " others like this"
    else:
        return "no one likes this"
    
print(likes(arr))