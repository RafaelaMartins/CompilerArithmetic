class Token:
    def __init__(self, types, lexems):
        self.type = types
        (const, msg) = types
        self.const = const
        self.msg = msg
        self.lexems = lexems