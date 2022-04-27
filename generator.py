class Element:
    def __init__(self, id):
        self.id = id
        self.tagList = []
    def addTag(self, id):
        self.tagList.insert(id)

class Generator:
    def __init__(self):
        self.archetype = 'tank'
        self.abilityStyle = 'martial'
        self.magicType = 'scholar'
        self.attackMode = 'mixed'
        self.element = 'none'
        self.leader = False
        self.legendary = False
        self.magicItems = False
        self.BASE_HP = 10

    def generate(self, arch, ability, magic, attack, element, leader, legendary, items):
        # generate AC
        # generate HP
        # generate stats
        # choose skills

        # generate spells
            # base 1 combat spell, 1 utility spell
            # type of spell effects number of later elements
                # ie. if spell is a reaction, number of reactions to gen is 1 less
        # generate abilities
        # generate actions
            # melee attacks
            # ranged attacks
            # misc. actions
        # generate bonus actions
        # generate reactions
        # generate magic items
        pass

    def save(self):
        pass

    def load(self):
        pass



