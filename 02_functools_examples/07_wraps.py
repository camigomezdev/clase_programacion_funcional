from functools import wraps


def another_function(func):
    """
    A function that accepts another function
    """
    # @wraps(func)
    def wrapper():
        """A wrapping function"""
        val = f"The result of {func()} is {eval(func())}"
        return val
    return wrapper


@another_function
def fucntion_test():
    """A pretty useless function"""
    return "1+1"


if __name__ == "__main__":
    print(fucntion_test())
    print(fucntion_test.__name__)
    print(fucntion_test.__doc__)