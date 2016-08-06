init -10 python:
    class Container(object):

        def __init__(self):
            self._at = ()
            self._has = {}

        def _keyChain(self, k):
            self._at += k
            if self._at in self._has and isinstance(self._has[self._at], Container):
                k = self._at
                self._at = ()
                return self._has[k]
            return self

        def __getitem__(self, k):
            return self._keyChain(tuple(k.split(".")))

        def __getattr__(self, k):
            return self._keyChain((k,))

        def __setitem__(self, k, v):
            if self._at != None:
                if not isinstance(k, tuple):
                    k = tuple(k.split("."))
                self._has[self._at + k] = v
            self._at = ()

        def __setattr__(self, k, v):
            if k[0] != '_':
                self.__setitem__((k,), v)
            else:
                super(Container, self).__setattr__(k, v)

        def __add__(self, other):
            other = self._has[self._at] + other if k in self._has else other
            self._at = ()
            return other

        def __iadd__(self, other):
            k = self._at
            self._at = None # prevent second assignment for last tuple part
            self._has[k] = self._has[k] + other if k in self._has else other
            return self._has[k]

        def __sub__(self, other): # -
            other = self._has[self._at] - other if k in self._has else -other
            self._at = ()
            return other

        def __isub__(self, other): # -=
            k = self._at
            self._at = None # prevent second assignment for last tuple part
            self._has[k] = self._has[k] - other if k in self._has else other
            return self._has[k]

        def __mul__(self, other): # *
            other = self._has[self._at] * other if k in self._has else 0
            self._at = ()
            return other

        def __imul__(self, other): # -=
            k = self._at
            self._at = None # prevent second assignment for last tuple part
            self._has[k] = self._has[k] * other if k in self._has else other
            return self._has[k]

        def __delattr__(self, k):
            self._has.pop(self._at + (k,), None)
            self._at = ()

        def __repr__(self): # needed?
            k = self._at
            self._has[()] = self._has[k]
            #self._at = ()
            return repr(self._has[k])

        def __str__(self): # needed?
            k = self._at
            self._has[()] = self._has[k]
            #self._at = ()
            return repr(self._has[k])

        def __call__(self): # for testing
            renpy.error(self._has)

        def __lt__(self, other): # <
            k = self._at
            self._at = ()
            return self._has[k] < other if k in self._has else 0 < other

        def __le__(self, other): # <=
            k = self._at
            self._at = ()
            return self._has[k] <= other if k in self._has else 0 <= other

        def __eq__(self, other): # ==
            k = self._at
            self._at = ()
            return self._has[k] == other if k in self._has else 0 == other

        def __ne__(self, other): # !=
            k = self._at
            self._at = ()
            return self._has[k] != other if k in self._has else 0 != other

        def __ge__(self, other): # >=
            k = self._at
            self._at = ()
            return self._has[k] >= other if k in self._has else 0 >= other

        def __gt__(self, other) : # >
            k = self._at
            self._at = ()
            return self._has[k] > other if k in self._has else 0 > other


