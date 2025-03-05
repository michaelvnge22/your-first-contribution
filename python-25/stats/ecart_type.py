import math

def ecart_type(variance):
    if variance < 0:
        raise ValueError("La variance ne peut pas être négative")
    
    return math.sqrt(variance)

# Test
print("Écart-type :", ecart_type(25))  # Doit afficher 5.0
