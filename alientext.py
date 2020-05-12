alien_alphabet = {"a": "@", "b": "|3", "c": "c", "d": "d", "e": "3", "f": "f", "g": "6", "h": "h", "i": "1",
                "j": "j", "k": "k", "l": "l", "m": "m", "n": "|\|", "o": "0", "p": "p", "q": "q", "r": "r",
                  "s": "5", "t": "t", "u": "u", "v": "v", "w": "w", "x": "x", "y": "y", "z": "z", " ": " "}

user_input = input("Say something! ")
translated: str = ''
for char in user_input.lower():
    translated += alien_alphabet[char]
print(f"The alien nearby says {translated}")


