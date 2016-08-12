init -9 python:
    import re
    import datetime
    from math import exp
    #class Caricature(Container):
    #    def __init__(self, name):
    #        super(Caricature, self).__init__()
    #        self.name = name
    #    def __getattr__(self, k):
    #        return super(Caricature, self).__dict__['#'][(k,)]

    class Breast(Container):
        def __init__(self, cupsize):
            super(Breast, self).__init__()
            m = re.search("([0-9]+)([a-zA-Z])$", cupsize)
            self.cup = ord(m.group(2).upper()) - 67
            self.size = int(m.group(1))
            self.milked = None
        def __getattr__(self, k):
            return super(Breast, self).__dict__['#'][(k,)]
        def weight(self):
            # in pounds
            vol = self.size + self.cup * 2
            return exp(-3.84 + (self.size + self.cup * 2) * .1)
        def set_lactating(self, last_time=None):
            self.milked = last_time if last_time else datetime.datetime.now()
        def milk(self):
            # in pounds as well
            if not self.milked:
                return 0
            d = datetime.timedelta(hours=15)
            now = datetime.datetime.now()
            d = min(now - self.milked, d).total_seconds() / d.total_seconds()
            self.milked = now
            return self.weight() * .18 * d

    #renpy.error(Key()["hoi"]["roel"]["kluin"])
    #horm = Caricature("Hermione")
    #horm.inv = Container()
    #horm.inv.lipstick.count = 2
    #horm.inv.lipstick.colors = ['red', 'pink']

    #horm.body = Container()
    #horm.body.right.breast = Breast("36A")
    #horm.body.left.breast = Breast("36A")
    #horm.body.left.breast.cup += 5

    #horm.body.right.breast.set_lactating(datetime.datetime.now() - datetime.timedelta(days=1))
    #horm.body.left.breast.set_lactating(datetime.datetime.now() - datetime.timedelta(days=1))
    #milk = horm.body.right.breast.milk() + horm.body.left.breast.milk()
    #renpy.error(horm.name+" produced "+str(milk)+" pounds of milk")


#return self for fluent interface (to allow chaining .a(wow).b(thats).etc(great)
#https://en.wikipedia.org/wiki/Fluent_interface
