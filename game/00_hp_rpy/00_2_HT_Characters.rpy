###HARRY POTTER CHARACTERS###
init python:
    import re
    import datetime
    from math import exp

    class Caricature(Container):
        def __init__(self, name, real_char):
            super(Caricature, self).__init__()
            # cannot use attributes in Container type.
            self._name = name
            self._real_char = real_char

        def __call__(self, what, interact=True):
            return getattr(store, self._real_char)(what, interact=interact)

        def predict(self, what):
            return getattr(store, self._real_char).predict(what)

        def giveTo(self, other, section=None):
            if section == None:
                section = self._at
            other[section] += 1
            self[self._at] -= 1

    class Breast(Container):
        def __init__(self, cupsize=None):
            super(Breast, self).__init__()
            m = re.search("([0-9]+)([a-zA-Z])$", cupsize)
            self.cup = ord(m.group(2).upper()) - 67
            self.size = int(m.group(1))
            self._milked = None
        def weight(self):
            # in pounds
            vol = self.size + self.cup * 2
            return exp(-3.84 + (self.size + self.cup * 2) * .1)
        def milk(self):
            # in pounds as well
            if not self._milked:
                return 0
            d = datetime.timedelta(hours=15)
            now = datetime.datetime.now()
            d = min(now - self._milked, d).total_seconds() / d.total_seconds()
            self._milked = now
            return self.weight() * .18 * d

    class Pussy(Container):
        def __init__(self):
            super(Pussy, self).__init__()

    class Anus(Container):
        def __init__(self):
            super(Anus, self).__init__()

    class Girl(Caricature):
        def __init__(self, name, real_char, cupsize=None):
            if cupsize == None:
                cupsize = "38C"
            super(Girl, self).__init__(name, real_char)
            self.breasts = [Breast(cupsize), Breast(cupsize)]
            self.pussy = Pussy()
            self.anus = Anus()

        def set_lactating(self, last_time=None):
            if not last_time:
                last_time = datetime.datetime.now()
            for breast in self.breasts:
                breast._milked = last_time

    # Character tables

    ### SNAPE HEAD ###
    sna_ = [""]
    for i in range(1,26):
        sna_.append("")
        sna_[i] = Character("Severus Snape", color="#402313", window_right_padding=270, show_side_image=Image("01_hp/13_characters/snape/head/head_" + str(i) + ".png", xalign=1.0, yalign=0.0), show_two_window=True, show_who_xalign=0.5, ctc="ctc3", ctc_position="fixed")


    fem = Character('Female Student', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    mal = Character('Male Student # 1', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    mal2 = Character('Male Student # 2', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    ann = Character('The Announcer', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    sly1 = Character('Slytherin student', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    sly2 = Character('Another Slytherin student', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    cr1 = Character('Somebody from the crowd', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    cr2 = Character('Another voice from the crowd', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")


    ###HARRY POTTER CHARACTERS###
    her_char = Character('Hermione', color="#402313", window_left_padding=85, show_two_window=True, ctc="ctc3", ctc_position="fixed")
    her2 = Character('Hermione', color="#402313", window_right_padding=220, show_two_window=True, ctc="ctc3", ctc_position="fixed") #Text box used for "head only" speech. (Because it has padding).
    sna_char = Character('Severus Snape', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    sna2 = Character('Severus Snape', color="#402313", window_right_padding=220, show_two_window=True, ctc="ctc3", ctc_position="fixed")  #Text box used for "head only" speech. (Because it has padding).
    vol = Character('Lord Voldemort', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    l_char = Character('Lola', color="#402313", window_right_padding=230, show_two_window=True, ctc="ctc3", ctc_position="fixed") #Text box used for "head only" speech. (Because it has padding).
    g3_char = Character('Genie', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")

    ###Custom Characters for WT:Silver
    spo = Character('Professor Sprout', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    maf = Character('Madam Mafkin', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    hoo = Character('Madam Hooch', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    abe = Character('Aberforth', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    lun_char = Character('Luna', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")


define dum = Character(None, window_left_padding=240, image="dum1", color="#402313", ctc="ctc3", ctc_position="fixed")
define dum2 = Character(None, window_left_padding=240, image="dum2", color="#402313", ctc="ctc3", ctc_position="fixed")
define dum3 = Character(None, window_left_padding=240, image="dum3", color="#402313", ctc="ctc3", ctc_position="fixed")
define dum4 = Character(None, window_left_padding=240, image="dum4", color="#402313", ctc="ctc3", ctc_position="fixed")
define dum5 = Character(None, window_left_padding=240, image="dum5", color="#402313", ctc="ctc3", ctc_position="fixed")


## FAWKES ##
define faw = Character('Fawkes',
    color="#f21111",
    window_right_padding=270,
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")



define pat = Character('silvarius2000',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("01_hp/11_misc/pat.png", xalign=1.0, yalign=1.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define dahr = Character(None,
    color="#402313",
    window_left_padding=230,
    show_side_image=Image("01_hp/18_store/dahr.png", xalign=0.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc4",
    ctc_position="fixed")

#######################################################################
##  Additions by JJ for replacement tutoring section  JJ 01/03/2015  ##

define her_wLeft = Character('Hermione',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("01_hp/15_hermione_head/HermioneWandEyesLeft.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define her_wMad = Character('Hermione',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("01_hp/15_hermione_head/HermioneWandEyesMad.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define her_wShut = Character('Hermione',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("01_hp/15_hermione_head/HermioneWandEyesShut.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define her_wWLeft = Character('Hermione',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("01_hp/15_hermione_head/HermioneWandEyesWideLeft.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define her_wWOpen = Character('Hermione',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("01_hp/15_hermione_head/HermioneWandEyesWideOpen.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define her_wDown = Character('Hermione',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("01_hp/15_hermione_head/HermioneWandLookDown.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define her_wOneopen = Character('Hermione',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("01_hp/15_hermione_head/HermioneWandOneShutDrop.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define her_wTears = Character('Hermione',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("01_hp/15_hermione_head/HermioneWandOneShutTears.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")
#######   JJ End additions           ##############################
###################################################################
