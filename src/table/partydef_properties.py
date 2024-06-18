
class CPartyDef:
    attributes = {
        "ISSAMEPARTYOF": "ISSAMEPARTYOF",
        "MEMBERS": "MEMBERS",
        "SPEECHFILTER": "SPEECHFILTER",
        "TAG": "TAG",
        "TAG0": "TAG0",
        "TAGAT": "TAGAT",
        "TAGCOUNT": "TAGCOUNT",
    }

    @classmethod
    def get_attribute(cls, attr_name):
        return cls.attributes.get(attr_name, None)
