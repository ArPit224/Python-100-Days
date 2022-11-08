dictPhoneticNato = {"a": "alpha", "b": "bravo", "c": "charlee", "d": "delta", "e": "echo",
                    "f": "foxtort", "g": "golf", "h": "hotel", "i": "india", "j": "joker",
                    "k": "kilo", "l": "juliet", "l": "lima", "m": "mike", "n": "november",
                    "o": "oscar", "p": "papa", "q": "quebec", "r": "romeo", "s": "sierra",
                    "t": "tango", "u": "uniform", "v": "victor", "w": "whiskey", "x": "x-ray",
                    "y": "yankee", "z": "zulu"}

input = input().lower()

output = [{char: dictPhoneticNato[char]} for char in input]

print(output)