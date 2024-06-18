
class CCPropsItemWeaponRanged:
    attributes = {
        "AMMOANIM": "AMMOANIM",
        "AMMOANIMHUE": "AMMOANIMHUE",
        "AMMOANIMRENDER": "AMMOANIMRENDER",
        "AMMOCONT": "AMMOCONT",
        "AMMOSOUNDHIT": "AMMOSOUNDHIT",
        "AMMOSOUNDMISS": "AMMOSOUNDMISS",
        "AMMOTYPE": "AMMOTYPE",
    }

    @classmethod
    def get_attribute(cls, attr_name):
        return cls.attributes.get(attr_name, None)
