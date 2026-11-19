fruits = ["blueberry", "strawberry", "lemon", "orange", "plum","raspberry","apple"]
            #0          #1             #2       #3      #4      #5          #6...........
#dictionary
#key,value
fruits_d = {"muffin":"blueberyy","shortcake":"strawberry","meringue":"lemon","blossom":"orange","pudding":"plum","tart":"raspberry","dumplin":"apple"}

print(fruits[6])

print(fruits_d["muffin"])

#traversing a dictionary
for x,y in fruits_d.items():
    print("key is",x,"-- value is",y)