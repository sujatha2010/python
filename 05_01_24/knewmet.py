# class MyClass:
#     def __new__(cls, *args, **kwargs):
#         instance = super(MyClass, cls).__new__(cls)
#         print("Creating a new instance of MyClass")
#         return instance

#     def __init__(self, *args, **kwargs):
#         print("Initializing an instance of MyClass")
# obj = MyClass()


class Language:
    def __new__(cls, *args):
        return super().__new__(cls)
 
    def __init__(self, lang, year):
        self.lang = lang
        self.year = year
language = Language('Python', 1991)
print(language.lang)
print(language.year)
