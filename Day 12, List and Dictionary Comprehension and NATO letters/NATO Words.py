dictPhoneticNato = {"a": "alpha", "b": "bravo", "c": "charlee", "d": "delta", "e": "echo",
                    "f": "foxtort", "g": "golf", "h": "hotel", "i": "india", "j": "joker",
                    "k": "kilo", "l": "juliet", "l": "lima", "m": "mike", "n": "november",
                    "o": "oscar", "p": "papa", "q": "quebec", "r": "romeo", "s": "sierra",
                    "t": "tango", "u": "uniform", "v": "victor", "w": "whiskey", "x": "x-ray",
                    "y": "yankee", "z": "zulu"}

input = input("Enter the word\n").lower()

output = []

for i in input:
    try:
        
        output.append({i: dictPhoneticNato[i]})
        
    except KeyError:
        pass

print(output)