s = input("Combien de secondes ?")
s = int(s)      # String vers entier

h = s // 3600
m = s % 3600    # Ou s - 3600*h 
x = m // 60
s = m % 60      # Ou m - 60*x

print(h, "heures", x, "minutes", s, "secondes.")