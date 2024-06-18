
class CCharNpc:
    attributes = {
        "ACTPRI": "ACTPRI",
        "BONDED": "BONDED",
        "FOLLOWERSLOTS": "FOLLOWERSLOTS",
        "HOMEDIST": "HOMEDIST",
        "NEED": "NEED",
        "NEEDNAME": "NEEDNAME",
        "NPC": "NPC",
        "SPEECH": "SPEECH",
        "SPELLADD": "SPELLADD",
        "THROWDAM": "THROWDAM",
        "THROWDAMTYPE": "THROWDAMTYPE",
        "THROWOBJ": "THROWOBJ",
        "THROWRANGE": "THROWRANGE",
        "VENDCAP": "VENDCAP",
        "VENDGOLD": "VENDGOLD",
    }

    @classmethod
    def get_attribute(cls, attr_name):
        return cls.attributes.get(attr_name, None)
