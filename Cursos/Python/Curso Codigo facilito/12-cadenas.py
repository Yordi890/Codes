course = "Course of python 3"

print(len(course))
print(course[0])
print(course[-1])
print(course[::2])

languages = "Python; Java; Ruby; PHP; Swift; Javascript; C#; C; C++"

lans = languages.split("; ")

as_string = "; ".join(lans)

print(lans)
print(as_string)

text = """text 
    with 
    \\n"""
print(text.splitlines())

text= course

print(text.capitalize())
print(text.swapcase())
print(text.upper())
course = "Course of python 3"

print(len(course))
print(course[0])
print(course[-1])
print(course[::2])

languages = "Python; Java; Ruby; PHP; Swift; Javascript; C#; C; C++"

lans = languages.split("; ")

as_string = "; ".join(lans)

print(lans)
print(as_string)


text= course

print(text.capitalize())
print(text.swapcase())
print(text.upper())
print(text.lower())

print(text.replace("C","c",1))

text = """  text 
    with 
    \\n  """
print(text.splitlines())

print(text.strip())

text ="course %s" %("Python")
print(text)


