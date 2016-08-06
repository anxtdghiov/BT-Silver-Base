init -10 python:
    class Container(object):

        def __init__(self):
            self.__dict__['#'] = {}
            self.__dict__['.'] = ()

        def _tupleChain(self, k):
            d = self.__dict__
            d['.'] += k
            if d['.'] in d['#'] and isinstance(d['#'][d['.']], Container):
                k = d['.']
                d['.'] = ()
                return d['#'][k]
            return self

        def __getitem__(self, k):
            return self._tupleChain(tuple(k.split(".")))

        def __getattr__(self, k):
            return self._tupleChain((k,))

        def _tupleSet(self, k, v):
            if self.__dict__['.'] != None:
                self.__dict__['#'][self.__dict__['.'] + k] = v
            self.__dict__['.'] = ()

        def __setitem__(self, k, v):
            self._tupleSet(tuple(k.split(".")), v)

        def __setattr__(self, k, v):
            self._tupleSet((k,), v)

        def __iadd__(self, other):
            d = self.__dict__
            k = d['.']
            d['.'] = None # prevent second assignment for last tuple part
            d['#'][k] = d['#'][k] + other if k in d['#'] else other
            return d['#'][k]

        def __add__(self, other):
            other = self.__dict__['#'][self.__dict__['.']] + other
            self.__dict__['.'] = ()
            return other

        def __mul__(self, other): # *
            other = self.__dict__['#'][self.__dict__['.']] * other
            self.__dict__['.'] = ()

        def __delattr__(self, k):
            self.__dict__['#'].pop(self.__dict__['.'] + (k,), None)
            self.__dict__['.'] = ()

        def __repr__(self): # not needed?
            k = self.__dict__['.']
            self.__dict__['#'][()] = self.__dict__['#'][k]
            #self.__dict__['.'] = ()
            return repr(self.__dict__['#'][k])

        def __str__(self): # not needed?
            k = self.__dict__['.']
            self.__dict__['#'][()] = self.__dict__['#'][k]
            #self.__dict__['.'] = ()
            return repr(self.__dict__['#'][k])

        def __call__(self): # for testing
            renpy.error(self.__dict__['#'])

        def __lt__(self, other): # <
            d = self.__dict__
            k = d['.']
            d['.'] = ()
            return d['#'][k] < other if k in d['#'] else 0 < other

        def __le__(self, other): # <=
            d = self.__dict__
            k = d['.']
            d['.'] = ()
            return d['#'][k] <= other if k in d['#'] else 0 <= other

        def __eq__(self, other): # ==
            d = self.__dict__
            k = d['.']
            d['.'] = ()
            return d['#'][k] == other if k in d['#'] else 0 == other

        def __ne__(self, other): # !=
            d = self.__dict__
            k = d['.']
            d['.'] = ()
            return d['#'][k] != other if k in d['#'] else 0 != other

        def __ge__(self, other): # >=
            d = self.__dict__
            k = d['.']
            d['.'] = ()
            return d['#'][k] >= other if k in d['#'] else 0 >= other

        def __gt__(self, other) : # >
            d = self.__dict__
            k = d['.']
            d['.'] = ()
            return d['#'][k] > other if k in d['#'] else 0 > other


