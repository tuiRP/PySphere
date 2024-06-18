
class CStoneMember:
    attributes = {
        "ACCOUNTGOLD": "ACCOUNTGOLD",
        "GUILDTITLE": "TITLE",
        "ISALLY": "GUILD_ISALLY",
        "ISCANDIDATE": "ISCANDIDATE",
        "ISENEMY": "GUILD_ISENEMY",
        "ISMASTER": "ISMASTER",
        "ISMEMBER": "ISMEMBER",
        "LOYALTO": "LOYALTO",
        "PRIV": "PRIV",
        "PRIVNAME": "PRIVNAME",
        "SHOWABBREV": "SHOWABBREV",
        "THEYALLIANCE": "GUILD_THEYALLIANCE",
        "THEYWAR": "GUILD_THEYWAR",
        "WEALLIANCE": "GUILD_WEALLIANCE",
        "WEWAR": "GUILD_WEWAR",
    }

    @classmethod
    def get_attribute(cls, attr_name):
        return cls.attributes.get(attr_name, None)
