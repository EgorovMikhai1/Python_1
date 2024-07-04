def get1(name, age=25):
    print(f"Hello {name}, how old are you? {age}")


def greet(*args):
    for arg in args:
        print(f"Hello {arg}")


def get2(**kwargs):
    for key, value in kwargs.items():
        print(f"Param 1 {key}: Param 2 {value}")


def mix(greeting, *args, punct="****"):
    for name in args:
        print(f"Hello {greeting} {name}> : {punct}")

    # for key, value in kwargs:
    #     print(f"Key {key} ** {value}")


mix("JAVA", 1,2,3,4,8)

def unionList(*args):
    for arg in args:
        
