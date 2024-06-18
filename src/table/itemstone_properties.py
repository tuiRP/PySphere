
class CItemStone:
    attributes = {
        "ABBREV": "ABBREV",
        "ABBREVIATIONTOGGLE": "ABBREVIATIONTOGGLE",
        "ADDHOUSE": "ADDHOUSE",
        "ADDSHIP": "ADDSHIP",
        "ALIGN": "ALIGN",
        "ALIGNTYPE": "ALIGNTYPE",
        "CHARTER": "CHARTER",
        "HOUSES": "HOUSES",
        "LOYALTO": "LOYALTO",
        "MASTER": "MASTER",
        "MASTERGENDERTITLE": "MASTERGENDERTITLE",
        "MASTERTITLE": "MASTERTITLE",
        "MASTERUID": "MASTERUID",
        "MAXHOUSES": "MAXHOUSES",
        "MAXSHIPS": "MAXSHIPS",
        "MEMBER": "MEMBER",
        "SHIPS": "SHIPS",
        "WEBPAGE": "WEBPAGE",
    }

    @classmethod
    def get_attribute(cls, attr_name):
        return cls.attributes.get(attr_name, None)
