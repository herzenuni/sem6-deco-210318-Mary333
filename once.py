import functools

def once(func):
    functools.wraps(func)
    def inner(*args, **kwargs):
        if not inner.called:
            inner.func = func
            inner.result = func(*args, **kwargs)
            inner.called = True

        return inner.result
            
    inner.called = False
    return inner

@once
def initialize_settings():
    print("Settings initialized")
    return 'masha'
    
print(initialize_settings())
print(initialize_settings())
print(initialize_settings.func())