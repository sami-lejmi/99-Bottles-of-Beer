# Python version of 99 Bottles of Beer

for x in range(99, 0, -1):
    if x > 2:
        print(x, "Bottles of beer on the wall,", x, "bottles of beer.")
        print("Take one down and pass it around,", x - 1, "bottles of beer on the wall.")
    if x == 2:
        print(x, "Bottles of beer on the wall,", x, "bottles of beer.")
        print("Take one down and pass it around,", x - 1, "bottle of beer on the wall.")
    if x == 1:
        print(x, "Bottle of beer on the wall,", x, "bottle of beer.")
        print("Take one down and pass it around, no more bottles of beer on the wall.")

print("No more bottles of beer on the wall, no more bottles of beer.")
print("Go to the store and buy some more, 99 bottles of beer on the wall.")
