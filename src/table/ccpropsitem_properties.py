
class CCPropsItem:
    attributes = {
        "LAVAINFUSED": "LAVAINFUSED",
        "SHIPWRECKITEM": "SHIPWRECKITEM",
        "UNLUCKY": "UNLUCKY",
    }

    @classmethod
    def get_attribute(cls, attr_name):
        return cls.attributes.get(attr_name, None)
