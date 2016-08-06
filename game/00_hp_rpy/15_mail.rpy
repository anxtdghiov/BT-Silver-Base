init python:
    from collections import defaultdict, Counter

    # lambda functions don't work with pickle (save/resume). This instead is ok.
    def get_Counter():
        return Counter()

    class DailyDelivery(list):

        maxdays = 10 # safety limit: if you send mail in 100000000000 days then
        # deliverylist grows and eats all your RAM (computer may crash)

        def send(self, in_days, kind, itemName, quantity=1):

            if in_days >= len(self) and in_days <= self.maxdays and in_days >= 0:
                # to get quantity 0 defaults for each kind of unsent mail:
                self.extend([defaultdict(get_Counter)] * (in_days - len(self) + 1))

            self[in_days][kind].update({itemName: quantity}) # add quantities
        def got_mail(self):
            return len(self) != 0

        def receive(self):
            return self.pop(0) if len(self) else {}

    #dailyDelivery = DailyDelivery()

label mail:
    if finished_report >= 1:
        $ letters -= 1 #Adds one letter in waiting list to be read. Displays owl with envelope.
        $ got_paycheck = False #When TRUE the paycheck is in the mail. Can't do paper work.
        hide screen owl
        show screen owl_02
        ">You read your mail."
        play sound "sounds/money.mp3"  #Quiet...
        if finished_report == 1:
            $ letter_text = "{size=-7}From:Ministry of Magic\nTo: Professor Dumbledore\n\n\n{/size}{size=-2}Thank you for completing one report this week.\nHere is your payment:{/size} \n{size=+4}40 gold coins.{/size}\n\n\n{size=-3}-With deepest respect-{/size}"
            $ gold += 40

        if finished_report == 2:
            $ letter_text = "{size=-7}From:Ministry of Magic\nTo: Professor Dumbledore\n\n\n{/size}{size=-2}Thank you for completing two reports this week.\nHere is your payment:{/size} \n{size=+4}70 gold coins.{/size}\n\n\n{size=-3}-With deepest respect-{/size}"
            $ gold += 70

        if finished_report == 3:
            $ letter_text = "{size=-7}From:Ministry of Magic\nTo: Professor Dumbledore\n\n\n{/size}{size=-2}Thank you for completing three reports this week.\nHere is your payment:{/size} \n{size=+4}90 gold coins.{/size}\n\n\n{size=-3}-With deepest respect-{/size}"
            $ gold += 90

        if finished_report == 4:
            $ letter_text = "{size=-7}From:Ministry of Magic\nTo: Professor Dumbledore\n\n\n{/size}{size=-2}Thank you for completing four reports this week.\nHere is your payment:{/size} \n{size=+4}110 gold coins.{/size}\n\n\n{size=-3}-With deepest respect-{/size}"
            $ gold += 110

        if finished_report == 5:
            $ letter_text = "{size=-7}From:Ministry of Magic\nTo: Professor Dumbledore\n\n\n{/size}{size=-2}Thank you for completing five reports this week.\nHere is your payment:{/size} \n{size=+4}150 gold coins.{/size}\n\n\n{size=-3}-With deepest respect-{/size}"
            $ gold += 150

        if finished_report >= 6:
            $ letter_text = "{size=-7}From:Ministry of Magic\nTo: Professor Dumbledore\n\n\n{/size}{size=-2}Thank you for completing six reports this week.\nHere is your payment:{/size} \n{size=+4}200 gold coins.{/size}\n\n\n{size=-3}-With deepest respect-{/size}"
            $ gold += 200

        show screen bld1
        show screen letter
        show screen ctc
        pause
        hide screen letter
        hide screen bld1
        hide screen ctc


#            ">Thank you for completing two reports this week. Here is your payment (40 gold)."
#            $ gold += 40

#        if finished_report >= 3:
#            "Thank you for completing three reports this week. Here is your payment (60 gold)."
#            $ gold += 60

#        if finished_report >= 4:
#            "Thank you for completing four reports this week. Here is your payment (80 gold)."
#            $ gold += 80

#        if finished_report >= 5: #Maximum amount per week.
#            "Thank you for completing five reports this week. Here is your payment (100 gold)."
#            $ gold += 100

#        if finished_report >= 6:
#            "Thank you for completing six reports this week. Here is your payment (20 gold)."
#            $ gold += 20

#        if finished_report >= 7:
#            "Thank you for completing seven reports this week. Here is your payment (20 gold)."
#            $ gold += 20

        $ finished_report = 0

        call screen main_menu_01


### MAIL FROM HERMIONE ###
#place after ### MAIL FROM HERMIONE ###

if outfit_ready:
    hide screen owl
    show screen owl_02
    $ letter_text = "{size=-7}From: Madam Mafkin\nTo: Professor Albus Dumbledore\n\n{/size}{size=-4}Dear professor Dumbledore.\nThis is a reminder that you have an order ready for pickup at the clothes store\n\n{size=-3}Thank you for your busness,\n M.M.{/size}"
    label letter_outfit:
    show screen letter
    show screen ctc
    show screen bld1
    with Dissolve(.3)
    pause
    menu:
        "-Done reading-":
            pass
        "-Not yet-":
            jump letter_outfit
    $ letters -= 1
    hide screen letter
    hide screen ctc
    hide screen bld1
    with Dissolve(.3)
    call screen main_menu_01

if day == 1:
    #$ letter_text = "{size=-4}-To professor Dumbledore-\n\nI am writing you to bring the current situation in our school to your attention.\n I'm afraid I'll need your help to sort this out.\n\n\n-Sincerely yours Hermione Granger-{/size}"
    $ letter_text = "{size=-7}From: Hermione Granger\nTo: Professor Dumbledore\n\n{/size}{size=-4}I am sure that you remember the reason why I'm writing you this letter from my last one, sir.\n\nI beg of you, please hear my plea this time. This injustice simply cannot go on...\nNot in this day and age, not in our school.\n\nPlease take action.\n\n{size=-3}With deepest respect,\nHermione Granger{/size}"
    hide screen owl
    show screen owl_02
    #$ mail_from_her = False #Comented out because replaced with $ letters += 1
    $ letters -= 1
    label letter01_agagin:
    show screen letter
    show screen ctc
    show screen bld1
    with Dissolve(.3)
    pause
    menu:
        "-Done reading-":
            pass
        "-Not yet-":
            jump letter01_agagin
    hide screen letter
    hide screen ctc
    hide screen bld1
    with Dissolve(.3)
    show screen bld1
    with d3
    m "Ehm..............................."
    m "What?"
    m "................................."
    hide screen bld1
    with d3
    jump event_00
    #call screen main_menu_01



if letter_from_hermione_02: #Letter from Hermione #02.
    $ letter_from_hermione_02 = False
    #$ letter_text = "{size=-4}-To professor Dumbledore-\n\nI am writing you to bring the current situation in our school to your attention.\n I'm afraid I'll need your help to sort this out.\n\n\n-Sincerely yours Hermione Granger--{/size}"
    $ letter_text = "{size=-7}From: Hermione Granger\nTo: Professor Dumbledore\n\n{/size}{size=-4}I am sorry to disturb you again, professor. I just want to make sure that you take this problem seriously.\n\nLast night another classmate confided inme... I gave my word to keep it a secret, so I cannot go into any details.\n\nAll I can say is that one of the Professors was involved.\n\nPlease take action soon.\n\n{size=-3}With deepest respect,\nHermione Granger.{/size}"
    hide screen owl
    show screen owl_02
    #$ mail_from_her = False #Comented out because replaced with $ letters += 1
    $ letters -= 1
    label letter02_agagin:
    show screen letter
    show screen ctc
    show screen bld1
    with Dissolve(.3)
    pause
    menu:
        "-Done reading-":
            pass
        "-Not yet-":
            jump letter02_agagin
    hide screen letter
    hide screen ctc
    hide screen bld1
    with Dissolve(.3)
    call screen main_menu_01





### MAIL THAT UNLOCKS ABILITY TO WORK ###
if work_unlock: # Send a letter that will unlock an ability to write reports
    $ work_unlock = False # Send a letter that will unlock an ability to write reports
    $ letters -= 1
    $ work_unlock2 = True # Unlocks the "Paperwork" button.
    hide screen owl
    show screen owl_02
    $ letter_text = "{size=-7}From: Ministry of Magic\nTo: Professor Albus Dumbledore\n\n{/size}{size=-4}Dear professor Dumbledore.\nWe remind you that only upon providing us with a completed report we will be able to make a paymentin your name.\n\n{size=-3}With deepest respect,\nThe Ministry of Magic.{/size}"
    label letter_work:
    show screen letter
    show screen ctc
    show screen bld1
    with Dissolve(.3)
    pause
    menu:
        "-Done reading-":
            pass
        "-Not yet-":
            jump letter_work
    hide screen letter
    hide screen ctc
    hide screen bld1
    with Dissolve(.3)
    m "Payments? Hm..."
    show screen blktone8
    with d3
    $ renpy.play('sounds/win2.mp3')   #Not loud.
    ">From now on you can do paperwork at your desk in order to earn additional gold..."
    hide screen blktone8
    with d3
    call screen main_menu_01























label mail_02: #Packages only. <=====================================================================### PACKAGES ###===================================================

### ITEMS ###
    # must receive every day, even if it's empty.
    $ delivery = dailyDelivery.receive()
    $ package_is_here = False

    if len(delivery) == 0:
        call screen main_menu_01

label package_gift:
    $ time = 1
    $ timer_range = 1
    $ timer_jump = 'package_gift'
    if 'Gift' in delivery and len(delivery['Gift']):
        $ (name, quantity) = delivery['Gift'].popitem()
        $ g3.inv.gift[name] += quantity
        $ the_gift = gift_list[name].image
        show screen giftTimer
        with d3
        if quantity > 1:
            "The pacakge contains [quantity] \"[name]'s\"{fast}"
        else:
            "The pacakge contains a \"[name]\"{fast}"
        hide screen giftTimer
        with d3

    if 'One time item' in delivery and len(delivery['One time item']):
        $ (name, quantity) = delivery['Gift'].popitem()
        $ the_gift = oneTimeItem[name].image
        $ oneTimeItem[name].orderStatus = orderStatus['delivered']
        if name == "Ball dress":
            $ descr = "A fancy nightdress has"
            $ gifts12.append("ball_dress")
        elif name == "Mini Skirt":
            $ descr = "A School miniskirt has"
            $ have_miniskirt = True # Turns TRUE when you have the skirt in your possession.
        elif name == "Glasses":
            $ descr = "Some fine reading glasses have"
            $ glasses = True #Glasses owned
            $ glasses_worn = False
        elif name == "S.P.E.W. Badge":
            $ descr = "A \"S.P.E.W.\" badge has"
            $ badge_01 = 1

            $ the_gift = "01_hp/18_store/29.png" # S.P.E.W. Badge.
        elif name == "Fishnet stockings":
            $ descr = "A pair of fishnet stockings have"
            $ nets = 1

        show screen giftTimer
        with d3
        ">[descr] been added to your possessions."
        hide screen giftTimer
        with d3
    call screen main_menu_01

