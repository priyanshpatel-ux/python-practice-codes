procedural= ["c", "fortran", "pascal"]
object_oriented= ["java", "c++", "python"]
functional= ["haskell", "scala", "lisp"]

l=input("Enter programming language= ")

if l in procedural:
    print(procedural)
elif l in object_oriented:
    print(object_oriented)
elif l in functional:
    print(functional)

else:
    print("not in the list")