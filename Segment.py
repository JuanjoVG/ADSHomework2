class Segment:
    def __init__(self, id: str, x1: float, x2: float):
        self.id = id
        self.x1 = x1
        self.x2 = x2

    @property
    def points(self):
        return [self.x1, self.x2]
