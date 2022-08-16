# it's a string question
def isAnagram(a : str, b : str):
        if sorted(a) == sorted(b):
            return True
        return False
    
a = 'geeksforgeeks'
b = 'forgeeksgeeks'

print(isAnagram(a,b))

# method 'sorted(str)' sorts alphabets accordingly (a-z)