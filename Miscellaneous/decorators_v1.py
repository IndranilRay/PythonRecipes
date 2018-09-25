def a_new_decorator(a_func):

    def wrap_the_func():
        print("I am doing some boring work before executing a_func")

        a_func()

        print("I am doing some boring work after executing a_func")
    return wrap_the_func


def a_function_requiring_decoration():
    print("I am the function which needs some decoration")


a_function_requiring_decoration()

a_function_requiring_decoration = a_new_decorator(a_function_requiring_decoration)

a_function_requiring_decoration()





