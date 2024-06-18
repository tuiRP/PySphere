
class CCPropsItemChar:
    attributes = {
        "WEIGHTREDUCTION": "WEIGHTREDUCTION",
    }

    @classmethod
    def get_attribute(cls, attr_name):
        return cls.attributes.get(attr_name, None)
