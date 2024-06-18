
class CSFileObj:
    attributes = {
        "FILEEXIST": "FILEEXIST",
        "FILELINES": "FILELINES",
        "FILEPATH": "FILEPATH",
        "INUSE": "INUSE",
        "ISEOF": "ISEOF",
        "LENGTH": "LENGTH",
        "OPEN": "OPEN",
        "POSITION": "POSITION",
        "READBYTE": "READBYTE",
        "READCHAR": "READCHAR",
        "READLINE": "READLINE",
        "SEEK": "SEEK",
        "WRITE": "WRITE",
        "WRITECHR": "WRITECHR",
        "WRITELINE": "WRITELINE",
    }

    @classmethod
    def get_attribute(cls, attr_name):
        return cls.attributes.get(attr_name, None)
