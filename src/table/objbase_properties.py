
class CObjBase:
    attributes = {
        "ABILITYPRIMARY": "ABILITYPRIMARY",
        "ABILITYSECONDARY": "ABILITYSECONDARY",
        "ARMOR": "ARMOR",
        "CAN": "CAN",
        "CANMASK": "CANMASK",
        "CANSEE": "CANSEE",
        "CANSEELOS": "CANSEELOS",
        "CANSEELOSFLAG": "CANSEELOSFLAG",
        "CLILOC": "CLILOC",
        "CLILOCCOUNT": "CLILOCCOUNT",
        "COLOR": "COLOR",
        "COMPLEXITY": "COMPLEXITY",
        "CTAGCOUNT": "CTAGCOUNT",
        "DAM": "DAM",
        "DIALOGLIST": "DIALOGLIST",
        "DISTANCE": "DISTANCE",
        "EVENTS": "EVENTS",
        "FACING": "FACING",
        "HASCOMPONENTPROPS": "HASCOMPONENTPROPS",
        "ISARMOR": "ISARMOR",
        "ISCHAR": "ISCHAR",
        "ISCONT": "ISCONT",
        "ISDIALOGOPEN": "ISDIALOGOPEN",
        "ISEVENT": "ISEVENT",
        "ISITEM": "ISITEM",
        "ISNEARTYPE": "ISNEARTYPE",
        "ISNEARTYPETOP": "ISNEARTYPETOP",
        "ISPLAYER": "ISPLAYER",
        "ISSLEEPING": "ISSLEEPING",
        "ISTEVENT": "ISTEVENT",
        "ISTIMERF": "ISTIMERF",
        "ISWEAPON": "ISWEAPON",
        "MAP": "MAP",
        "MODAC": "MODAC",
        "MODAR": "MODAR",
        "MODMAXWEIGHT": "MODMAXWEIGHT",
        "NAME": "NAME",
        "NAMELOC": "NAMELOC",
        "ONAME": "ONAME",
        "P": "P",
        "PROPSAT": "PROPSAT",
        "PROPSCOUNT": "PROPSCOUNT",
        "RECIPEALCHEMY": "RECIPEALCHEMY",
        "RECIPEBLACKSMITH": "RECIPEBLACKSMITH",
        "RECIPEBOWCRAFT": "RECIPEBOWCRAFT",
        "RECIPECARPENTRY": "RECIPECARPENTRY",
        "RECIPECARTOGRAPHY": "RECIPECARTOGRAPHY",
        "RECIPECOOKING": "RECIPECOOKING",
        "RECIPEGLASSBLOWING": "RECIPEGLASSBLOWING",
        "RECIPEINSCRIPTION": "RECIPEINSCRIPTION",
        "RECIPEMASONRY": "RECIPEMASONRY",
        "RECIPETAILORING": "RECIPETAILORING",
        "RECIPETINKERING": "RECIPETINKERING",
        "RESDISPDNHUE": "RESDISPDNHUE",
        "SERIAL": "SERIAL",
        "SEXTANTP": "SEXTANTP",
        "SLAYER": "SLAYER",
        "SLAYERLESSER": "SLAYERLESSER",
        "SLAYERMISC": "SLAYERMISC",
        "SLAYERSUPER": "SLAYERSUPER",
        "SPAWNITEM": "SPAWNITEM",
        "SPEED": "SPEED",
        "TAG": "TAG",
        "TAG0": "TAG0",
        "TAGAT": "TAGAT",
        "TAGCOUNT": "TAGCOUNT",
        "TEXTF": "TEXTF",
        "TIMER": "TIMER",
        "TIMERD": "TIMERD",
        "TIMERMS": "TIMERMS",
        "TIMESTAMP": "TIMESTAMP",
        "TOPOBJ": "TOPOBJ",
        "TRIGGER": "TRIGGER",
        "UID": "UID",
        "VERSION": "VERSION",
        "WEIGHT": "WEIGHT",
        "Z": "Z",
    }

    @classmethod
    def get_attribute(cls, attr_name):
        return cls.attributes.get(attr_name, None)
