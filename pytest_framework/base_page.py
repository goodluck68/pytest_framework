
def exception_handle(fun):
    def magic(*args, **kwargs):
        print(f"{fun.__name__} ({args}, {kwargs})")
        res = fun(*args, **kwargs)
        print(f"{fun.__name__} finish")
        return res
    return magic


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    @exception_handle
    def find(self, by, value):
        return self.driver.find_element(by, value)
