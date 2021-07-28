#List
colors = ["red", "green", "blue", "yellow"]
print(colors)
print(colors[0])
print(colors[0].title())
print(colors[-1]) #index for the last item in a list
print(colors[-2]) #index for the 2nd last item in a list
print(f"I like the color {colors[2].title()}")

#change item in a list
colors[1] = "black"
print(colors)

#add a new item to a list
colors.append("magenta")
print(colors)

days_of_week = []
days_of_week.append("mon")
days_of_week.append("tue")
print(days_of_week)

#inserting a new item
days_of_week.insert(0, "sun") #insert at index 0
print(days_of_week)

#remove an item from a list
del days_of_week[0] #remove item from index 0
print(days_of_week)

#pop an item - remove the last item but can be saved in a variable the item removed
print("---------------")
print(colors)
popped_color = colors.pop()
print(colors)
print(popped_color)

#popping item from any position
print("---------------")
print(colors)
popped_color1 = colors.pop(1) #pop 2nd item
print(colors)
print(popped_color1)

#If you’re unsure whether to use the del statement or the pop() method, here’s a simple way to decide: 
#when you want to delete an item from a list and not use that item in any way, use the del statement; 
#if you want to use an item as you remove it, use the pop() method.

#remove an item by value
print("---------------")
print(colors)
colors.remove("blue") #remove item named "blue"
print(colors)

#add more colors
print("---------------")
colors.append("white")
colors.append("maroon")
colors.append("indigo")
print(colors)

print("---------------")
#remove clor with variable
print(colors)
remove_color = "white"
colors.remove(remove_color)
print(colors)
print(f"Color removed is {remove_color}")

#The remove() method deletes only the first occurrence of the value you specify. 
# If there’s a possibility the value appears more than once in the list, 
# you’ll need to use a loop to make sure all occurrences of the value are removed.

#permanent sorting
print("---------------")
print(colors)
colors.sort()
print(colors)
colors.sort(reverse = True) #reverse sort
print(colors)

#temporary sorting for display
print("---------------")
colors.append("skyblue")
colors.append("ocean")
colors.append("cyan")
print(colors)
print(sorted(colors))
print(colors)
print(sorted(colors, reverse=True))
print(colors)
#Sorting a list alphabetically is a bit more complicated when all the values are not in lowercase.


#reverse the index, not sorting aphabetically - just reversing without sorting, permanently
print("---------------")
print(colors)
colors.reverse()
print(colors)

#find length
print("---------------")
print(colors)
print(len(colors))


