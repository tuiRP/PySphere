
class CCPropsItemWeapon:
    attributes = {
        "ASSASSINHONED": "ASSASSINHONED",
        "BALANCED": "BALANCED",
        "BANE": "BANE",
        "BATTLELUST": "BATTLELUST",
        "BONEBREAKER": "BONEBREAKER",
        "BLOODDRINKER": "BLOODDRINKER",
        "MAGEWEAPON": "MAGEWEAPON",
        "MYSTICWEAPON": "MYSTICWEAPON",
        "RANGE": "RANGE",
        "RANGEH": "RANGEH",
        "RANGEL": "RANGEL",
        "SEARINGWEAPON": "SEARING",
        "SPLINTERINGWEAPON": "SPLINTERING",
        "USEBESTWEAPONSKILL": "USEBESTWEAPONSKILL",
        "WEAPONSOUNDHIT": "WEAPONSOUNDHIT",
        "WEAPONSOUNDMISS": "WEAPONSOUNDMISS",
    }

    @classmethod
    def get_attribute(cls, attr_name):
        return cls.attributes.get(attr_name, None)
