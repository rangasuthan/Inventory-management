class ItemNotFoundException(Exception):
    def __init__(self, name: str = None):
        self.name = name
        self.message = f"Item '{name}' not found" if name else "Item not found"
        super().__init__(self.message)


class InvalidStockException(Exception):
    def __init__(self, message: str = "Invalid stock operation"):
        self.message = message
        super().__init__(self.message)
