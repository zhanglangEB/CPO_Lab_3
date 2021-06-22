registry = {}


class MultiMethod(object):
    def __init__(self, name: str):
        self.name: str = name
        self.typemap: dict = {}

    def __call__(self, *args, **kwargs):
        states: list = list(self.typemap.keys())
        vals: list = [arg for arg in args]
        kvals: list = [value for value in kwargs.values()]
        vals.extend(kvals)
        for s in states:
            if len(s) == len(vals):
                ismatched = True
                for i in range(len(s)):
                    if not isinstance(vals[i], s[i]):
                        ismatched = False
                if ismatched:
                    return self.typemap.get(s)(*args, **kwargs)
        raise TypeError("no match")

    def register(self, types, function):
        if types not in self.typemap:
            # raise TypeError("duplicate registration")
            self.typemap[types] = function


def multimethod(*types):
    def register(function):
        function = getattr(function, "__lastreg__", function)
        name = function.__name__
        mm = registry.get(name)
        if mm is None:
            mm = registry[name] = MultiMethod(name)
        mm.register(types, function)
        mm.__lastreg__ = function
        return mm

    return register
