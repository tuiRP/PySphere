# pysphere/src/base_base_def_props.py

class CBaseBaseDef:
    attributes = {
        "ABILITYPRIMARY": "ABILITYPRIMARY",
        "ABILITYSECONDARY": "ABILITYSECONDARY",
        "ARMOR": "ARMOR",
        "BASEID": "BASEID",
        "CAN": "CAN",
        "CATEGORY": "CATEGORY",
        "DAM": "DAM",
        "DEFNAME": "DEFNAME",
        "DEFNAME2": "DEFNAME2",
        "DESCRIPTION": "DESCRIPTION",
        "EXPANSION": "EXPANSION",
        "FACTION": "FACTION",
        "HASCOMPONENTPROPS": "HASCOMPONENTPROPS",
        "HEIGHT": "HEIGHT",
        "INSTANCES": "INSTANCES",
        "ISTEVENT": "ISTEVENT",
        "NAME": "NAME",
        "NAMELOC": "NAMELOC",
        "RESDISPDNHUE": "RESDISPDNHUE",
        "RESLEVEL": "RESLEVEL",
        "RESOURCES": "RESOURCES",
        "SLAYER": "SLAYER",
        "SUBSECTION": "SUBSECTION",
        "TAG": "TAG",
        "TAG0": "TAG0",
        "TEVENTS": "TEVENTS",
        "VELOCITY": "VELOCITY",
    }

    @classmethod
    def get_attribute(cls, attr_name):
        return cls.attributes.get(attr_name, None)

