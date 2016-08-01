init python:

    class Outfit(object):
        name = ""
        purchased = False
        cost = 0
        wait_time = 0 #the ammount of time to wait until compleded from clothes store
        top_layers = []
        outfit_layers = []
        actions = []
        action_images = []
        hair_layer = ""
        breast_layer = "breasts_nipfix"
        store_image = ""
        def __init__(self, **kwargs):
            self.__dict__.update(**kwargs)
        def getMenuText(self):
            return "-"+self.name+"-"
        def getFullPath(self, passed_list, character="hermione"):
            return [("01_hp/13_characters/"+character+"/clothes/custom/" + i) for i in passed_list]
        def getOutfitLayers(self):
            return self.getFullPath(self.outfit_layers)
        def getTopLayers(self):
            return self.getFullPath(self.top_layers)
        def getActionImage(self, action):
            return self.action_images[self.actions.index(action)]
        def getStoreImage(self):
           return "01_hp/23_clothes_store/cs_gui/"+self.store_image

    class OutfitList(list):
        indexForName = {}

        def append(self, **entry):
            self.indexForName[entry['name']] = len(self)
            super(OutfitList, self).append(Outfit(**entry))

    outfit_list = OutfitList()

    outfit_list.append(cost=100, wait_time=2, name="Maid", store_image="maid.png",
        outfit_layers=["maid_stockings.png", "maid_skirt.png", "maid_top.png", "maid_gloves.png"], top_layers=["maid_hat.png"])

    outfit_list.append(cost=200, wait_time=3, name="Griffindor Cheerleader", store_image="cheer.png",
        outfit_layers=["cheer_stockings.png", "cheer_pants.png", "cheer_top.png"], actions=["lift_top"], action_images=["cherr_flash.png"])

    outfit_list.append(cost=200, wait_time=3, name="Slythrin Cheerleader", store_image="s_cheer.png",
        outfit_layers=["s_cheer_stockings.png", "s_cheer_pants.png", "s_cheer_top.png"], actions=["lift_top"], action_images=["cherr_flash.png"])

    outfit_list.append(cost=300, wait_time=4, name="Heart Dancer", store_image="heart.png",
        outfit_layers=["heart_legs.png", "heart_top.png", "heart_collar.png"])

    outfit_list.append(cost=140, wait_time=2, name="Silk Nightgown", store_image="nightgown.png",
        outfit_layers=["silk_nightgown.png"], breast_layer="breasts_normal")

    outfit_list.append(cost=75, wait_time=2, name="Pirate", store_image="pirate.png",
        outfit_layers=["pirate_legs.png", "pirate_pants.png", "pirate_top.png"])

    outfit_list.append(cost=350, wait_time=3, name="Power Girl", store_image="power.png",
        outfit_layers=["power_costume.png"], hair_layer="power_hair", actions=["lift_top"], action_images=["power_costume_2.png"])

    outfit_list.append(cost=250, wait_time=5, name="Mrs Marvel", store_image="marvel.png",
        outfit_layers=["marvel_pants.png", "marvel_top.png", "marvel_sash.png", "marvel_gloves.png"])

    outfit_list.append(cost=300, wait_time=4, name="Harley Quinn", store_image="harley.png",
        outfit_layers=["harley_pants.png", "harley_top.png", "harley_gloves.png", "harley_collar.png"], hair_layer="harley_hair")

    outfit_list.append(cost=15000, wait_time=7, name="Ball Dress", store_image="ball_dress.png",
        outfit_layers=["ball_dress_skirt.png", "ball_dress_top.png"])

    outfit_list.append(cost=50, wait_time=2, name="Christmas Girl", store_image="christmas.png",
        outfit_layers=["christmas_pants.png", "christmas_top.png", "christmas_gloves.png", "christmas_collar.png"], top_layers=["christmas_antlers.png"], breast_layer="breasts_normal")

    outfit_list.append(cost=270, wait_time=2, name="Lara Croft", store_image="lara.png",
        outfit_layers=["lara_pants.png", "lara_top.png", "lara_gloves.png"])

