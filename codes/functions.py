
def outer():
    outer_vavr = "outer variable"
    def inner():
        return outer_vavr
    return inner

func = outer()

func()
