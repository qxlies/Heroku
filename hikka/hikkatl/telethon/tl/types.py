class MessageEntityBlockquote(MessageEntity):
    """
    Represents a blockquote message entity.
    """
    CONSTRUCTOR_ID = 0x... # Need to assign a unique ID
    SUBCLASS_OF_ID = 0x... # Need to assign appropriate subclass ID

    def __init__(self, offset: int, length: int):
        super().__init__(offset, length)

    def to_dict(self):
        return {
            '_': 'MessageEntityBlockquote',
            'offset': self.offset,
            'length': self.length
        } 