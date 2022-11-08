#try: Do this
#except: If it failed do this
#else: Do this if it didn't failed
#finally: Always work, Doesn't care if it failed or not

try:
    open("A real file.txt")

except:
    print("It failed, But gracefully")
    
else:
    print("IT WORKED! HOW?")
    
finally:
    print("Who cares what happened, the code worked, Believe me I know")
    raise TypeError("Lol I am always an error.")