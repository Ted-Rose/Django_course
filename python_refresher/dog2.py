
class Dog:

    def __init__(self, name="", age=0, furcolor=""):
        self.name = name
        self.age = age
        self.furcolor = furcolor

    def bark(self, str):
        print("BARK! " + str)

mydog = Dog("Fido", 13, "Brown")
newdog = Dog()


print("mydog.age:")
print(mydog.age)

print("newdog.age:")
print(newdog.age)
