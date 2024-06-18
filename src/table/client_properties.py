
class CClient:
    attributes = {
        "ALLMOVE": "ALLMOVE",
        "ALLSHOW": "ALLSHOW",
        "CLIENTIS3D": "CLIENTIS3D",
        "CLIENTISENHANCED": "CLIENTISENHANCED",
        "CLIENTISKR": "CLIENTISKR",
        "CLIENTVERSION": "CLIENTVERSION",
        "DEBUG": "DEBUG",
        "DETAIL": "DETAIL",
        "GM": "GM",
        "HEARALL": "HEARALL",
        "LASTEVENT": "LASTEVENT",
        "LASTEVENTWALK": "LASTEVENTWALK",
        "PRIVSHOW": "PRIVSHOW",
        "REPORTEDCLIVER": "REPORTEDCLIVER",
        "SCREENSIZE": "SCREENSIZE",
        "TARG": "TARG",
        "TARGP": "TARGP",
        "TARGPROP": "TARGPROP",
        "TARGPRV": "TARGPRV",
        "TARGTXT": "TARGTXT",
    }

    @classmethod
    def get_attribute(cls, attr_name):
        return cls.attributes.get(attr_name, None)
