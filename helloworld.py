## Literal expressions
# An expression

print(100)

# Hello world

print("Salut, Terrien !")
couleur_favorite = "bleu"
print(couleur_favorite)
print(couleur_favorite*10, sep=" ")

# Functions

print(pow(4, 2))            # Carré de 4
print(int(3.14))
print("2*2", 2*int("2"))    # Parse a string to the int function
print(type(2.5))            # Print data type

## Non-literal (semantic?) expressions
# Our fonction (Le Cunn, 2019, p. 87)
def f(x,w) : return w*x
w=4
x=2
yp=f(x,w)
print(yp)

# Input
n = input("Please enter your name: ")
print("Hello", n, "!")