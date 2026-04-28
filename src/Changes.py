class Changes:
    def __init__(self):
        self.data = ""

    def get(self):
        return self.data

    def insert_data(self, data):
        self.data = data


class Patch(Changes):
    def get_text(self):
        return "PATCH: " + self.data + '\n'


class GeneralChanges(Changes):
    def get_text(self):
        return "GENERAL CHANGES:\n" + (self.data if self.data else "No changes found." ) \
            + "\n----------------------------------------------------"


class NeutralCreepsChanges(Changes):
    def get_text(self):
        return "NEUTRAL CREEPS CHANGES:\n" + (self.data if self.data else "No changes found.") \
            + "\n----------------------------------------------------"


class ItemsChanges(Changes):
    def get_text(self):
        return "ITEMS CHANGES:\n" + (self.data if self.data else "No changes found.") \
            + "\n----------------------------------------------------"


class NeutralItemsChanges(ItemsChanges):
    def get_text(self):
        return "NEUTRAL ITEMS CHANGES:\n" + (self.data if self.data else "No changes found.") \
            + "\n----------------------------------------------------"


class HeroesChanges(Changes):
    def get_text(self):
        return "HEROES CHANGES:\n" + (self.data if self.data else "No changes found.") \
            + "\n----------------------------------------------------"
