# 10) Write a Python program to get the class name of an instance in Python.


class ClassNameGetter:
    def get_class_name(self, instance):
        return instance.__class__.__name__

name = ClassNameGetter()
print(name.get_class_name("kaushik"))