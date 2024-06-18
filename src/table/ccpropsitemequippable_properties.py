
class CCPropsItemEquippable:
    attributes = {
        "ALTERED": "ALTERED",
        "ANTIQUE": "ANTIQUE",
        "BONUSBERSERK": "BONUSBERSERK",
        "BONUSDEX": "BONUSDEX",
        "BONUSDURABILITY": "BONUSDURABILITY",
        "BONUSHITSMAX": "BONUSHITSMAX",
        "BONUSINT": "BONUSINT",
        "BONUSMANAMAX": "BONUSMANAMAX",
        "BONUSSTAMMAX": "BONUSSTAMMAX",
        "BONUSSTR": "BONUSSTR",
        "BRITTLE": "BRITTLE",
        "CASTINGFOCUS": "CASTINGFOCUS",
        "COMBATBONUSPERCENT": "COMBATBONUSPERCENT",
        "COMBATBONUSSTAT": "COMBATBONUSSTAT",
        "DAMCHAOS": "DAMCHAOS",
        "DAMCOLD": "DAMCOLD",
        "DAMDIRECT": "DAMDIRECT",
        "DAMENERGY": "DAMENERGY",
        "DAMFIRE": "DAMFIRE",
        "DAMPHYSICAL": "DAMPHYSICAL",
        "DAMPOISON": "DAMPOISON",
        "EATERCOLD": "EATERCOLD",
        "EATERDAM": "EATERDAM",
        "EATERENERGY": "EATERENERGY",
        "EATERFIRE": "EATERFIRE",
        "EATERKINETIC": "EATERKINETIC",
        "EATERPOISON": "EATERPOISON",
        "ENHANCEPOTIONS": "ENHANCEPOTIONS",
        "EPHEMERAL": "EPHEMERAL",
        "FASTERCASTING": "FASTERCASTING",
        "FASTERCASTRECOVERY": "FASTERCASTRECOVERY",
        "HITAREACOLD": "HITAREACOLD",
        "HITAREAENERGY": "HITAREAENERGY",
        "HITAREAFIRE": "HITAREAFIRE",
        "HITAREAPHYSICAL": "HITAREAPHYSICAL",
        "HITAREAPOISON": "HITAREAPOISON",
        "HITCURSE": "HITCURSE",
        "HITDISPEL": "HITDISPEL",
        "HITFATIGUE": "HITFATIGUE",
        "HITFIREBALL": "HITFIREBALL",
        "HITHARM": "HITHARM",
        "HITLEECHLIFE": "HITLEECHLIFE",
        "HITLEECHMANA": "HITLEECHMANA",
        "HITLEECHSTAM": "HITLEECHSTAM",
        "HITLIGHTNING": "HITLIGHTNING",
        "HITLOWERATK": "HITLOWERATK",
        "HITLOWERDEF": "HITLOWERDEF",
        "HITMAGICARROW": "HITMAGICARROW",
        "HITMANADRAIN": "HITMANADRAIN",
        "HITSPARKS": "HITSPARKS",
        "HITSPELL": "HITSPELL",
        "HITSPELLSTR": "HITSPELLSTR",
        "HITSWARM": "HITSWARM",
        "IMBUED": "IMBUED",
        "INCREASEDAM": "INCREASEDAM",
        "INCREASEDEFCHANCE": "INCREASEDEFCHANCE",
        "INCREASEDEFCHANCEMAX": "INCREASEDEFCHANCEMAX",
        "INCREASEGOLD": "INCREASEGOLD",
        "INCREASEHITCHANCE": "INCREASEHITCHANCE",
        "INCREASEKARMALOSS": "INCREASEKARMALOSS",
        "INCREASESPELLDAM": "INCREASESPELLDAM",
        "INCREASESWINGSPEED": "INCREASESWINGSPEED",
        "LOWERAMMOCOST": "LOWERAMMOCOST",
        "LOWERMANACOST": "LOWERMANACOST",
        "LOWERREAGENTCOST": "LOWERREAGENTCOST",
        "LOWERREQ": "LOWERREQ",
        "LUCK": "LUCK",
        "MAGEARMOR": "MAGEARMOR",
        "MASSIVE": "MASSIVE",
        "NIGHTSIGHT": "NIGHTSIGHT",
        "PRIZED": "PRIZED",
        "RAGEFOCUS": "RAGEFOCUS",
        "REACTIVEPARALYZE": "REACTIVEPARALYZE",
        "REFLECTPHYSICALDAM": "REFLECTPHYSICALDAM",
        "REGENFOOD": "REGENFOOD",
        "REGENHITS": "REGENHITS",
        "REGENMANA": "REGENMANA",
        "REGENSTAM": "REGENSTAM",
        "REGENVALFOOD": "REGENVALFOOD",
        "REGENVALHITS": "REGENVALHITS",
        "REGENVALMANA": "REGENVALMANA",
        "REGENVALSTAM": "REGENVALSTAM",
        "RESCOLD": "RESCOLD",
        "RESCOLDMAX": "RESCOLDMAX",
        "RESENERGY": "RESENERGY",
        "RESENERGYMAX": "RESENERGYMAX",
        "RESFIRE": "RESFIRE",
        "RESFIREMAX": "RESFIREMAX",
        "RESONANCECOLD": "RESONANCECOLD",
        "RESONANCEENERGY": "RESONANCEENERGY",
        "RESONANCEFIRE": "RESONANCEFIRE",
        "RESONANCEKINETIC": "RESONANCEKINETIC",
        "RESONANCEPOISON": "RESONANCEPOISON",
        "RESPHYSICAL": "RESPHYSICAL",
        "RESPHYSICALMAX": "RESPHYSICALMAX",
        "RESPOISON": "RESPOISON",
        "RESPOISONMAX": "RESPOISONMAX",
        "SOULCHARGE": "SOULCHARGE",
        "SOULCHARGECOLD": "SOULCHARGECOLD",
        "SOULCHARGEENERGY": "SOULCHARGEENERGY",
        "SOULCHARGEFIRE": "SOULCHARGEFIRE",
        "SOULCHARGEKINETIC": "SOULCHARGEKINETIC",
        "SOULCHARGEPOISON": "SOULCHARGEPOISON",
        "SPELLCHANNELING": "SPELLCHANNELING",
        "SPELLCONSUMPTION": "SPELLCONSUMPTION",
        "SPELLFOCUSING": "SPELLFOCUSING",
        "UNWIELDLY": "UNWIELDLY",
    }

    @classmethod
    def get_attribute(cls, attr_name):
        return cls.attributes.get(attr_name, None)
