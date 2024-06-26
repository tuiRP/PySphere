
class CCharBase:
    attributes = {
        "ANIM": "ANIM",
        "ARMOR": "ARMOR",
        "AVERSIONS": "AVERSIONS",
        "BLOODCOLOR": "BLOODCOLOR",
        "BONDED": "BONDED",
        "BREATH": "BREATH",
        "COLOR": "COLOR",
        "DESIRES": "DESIRES",
        "DEX": "DEX",
        "DISPID": "DISPID",
        "ERALIMITGEAR": "ERALIMITGEAR",
        "ERALIMITLOOT": "ERALIMITLOOT",
        "ERALIMITPROPS": "ERALIMITPROPS",
        "FOLLOWERSLOTS": "FOLLOWERSLOTS",
        "FOODTYPE": "FOODTYPE",
        "HIREDAYWAGE": "HIREDAYWAGE",
        "ICON": "ICON",
        "ID": "ID",
        "INT": "INT",
        "JOB": "JOB",
        "MAXFOLLOWER": "MAXFOLLOWER",
        "MAXFOOD": "MAXFOOD",
        "MOVERATE": "MOVERATE",
        "RANGE": "RANGE",
        "RANGEH": "RANGEH",
        "RANGEL": "RANGEL",
        "RESDISPDNID": "RESDISPDNID",
        "SOUND": "SOUND",
        "SOUNDDIE": "SOUNDDIE",
        "SOUNDGETHIT": "SOUNDGETHIT",
        "SOUNDHIT": "SOUNDHIT",
        "SOUNDIDLE": "SOUNDIDLE",
        "SOUNDNOTICE": "SOUNDNOTICE",
        "STR": "STR",
        "THROWDAM": "THROWDAM",
        "THROWDAMTYPE": "THROWDAMTYPE",
        "THROWOBJ": "THROWOBJ",
        "THROWRANGE": "THROWRANGE",
        "TITHING": "TITHING",
        "TSPEECH": "TSPEECH",
    }

    @classmethod
    def get_attribute(cls, attr_name):
        return cls.attributes.get(attr_name, None)
