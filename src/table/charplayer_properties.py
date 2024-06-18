
class CCharPlayer:
    attributes = {
        "ACCOUNT": "ACCOUNT",
        "ADDHOUSE": "ADDHOUSE",
        "ADDSHIP": "ADDSHIP",
        "DEATHS": "DEATHS",
        "DELHOUSE": "DELHOUSE",
        "DELSHIP": "DELSHIP",
        "DSPEECH": "DSPEECH",
        "EMOTECOLOR": "EMOTECOLOR",
        "GETHOUSEPOS": "GETHOUSEPOS",
        "GETSHIPPOS": "GETSHIPPOS",
        "HOUSES": "HOUSES",
        "ISDSPEECH": "ISDSPEECH",
        "KILLS": "KILLS",
        "KRTOOLBARSTATUS": "KRTOOLBARSTATUS",
        "LASTDISCONNECTED": "LASTDISCONNECTED",
        "LASTUSED": "LASTUSED",
        "LIGHT": "LIGHT",
        "MAXHOUSES": "MAXHOUSES",
        "MAXSHIPS": "MAXSHIPS",
        "PFLAG": "PFLAG",
        "PROFILE": "PROFILE",
        "REFUSETRADES": "REFUSETRADES",
        "SHIPS": "SHIPS",
        "SKILLCLASS": "SKILLCLASS",
        "SKILLLOCK": "SKILLLOCK",
        "SPEECHCOLOR": "SPEECHCOLOR",
        "SPEEDMODE": "SPEEDMODE",
        "STATLOCK": "STATLOCK",
    }

    @classmethod
    def get_attribute(cls, attr_name):
        return cls.attributes.get(attr_name, None)
