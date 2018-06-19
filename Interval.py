from Segment import Segment


class Interval:

    def __init__(self, x1: float, x2: float):
        self.x1 = x1
        self.x2 = x2

    def repr(self, left_char: str, right_char: str):
        return left_char + str(self.x1) + ', ' + str(self.x2) + right_char

    def contained_in(self, segment: Segment):
        return segment.x1 <= self.x1 and self.x2 <= segment.x2

    @staticmethod
    def is_right_open():
        raise NotImplementedError("Not implemented method")

    def merge(self, right_interval: 'Interval'):
        raise NotImplementedError("Not implemented method")

    def intersect_with(self, segment: Segment):
        raise NotImplementedError("Not implemented method")

    def contains(self, p: float):
        raise NotImplementedError("Not implemented method")


class CCInterval(Interval):
    LEFT_CHAR = '['

    RIGHT_CHAR = ']'

    def __repr__(self):
        return self.repr(self.LEFT_CHAR, self.RIGHT_CHAR)

    @staticmethod
    def is_right_open():
        return False

    def merge(self, right_interval: Interval):
        if right_interval.is_right_open():
            return COInterval(self.x1, right_interval.x2)
        else:
            return CCInterval(self.x1, right_interval.x2)

    def intersect_with(self, segment: Segment):
        return segment.x1 <= self.x2 and self.x1 <= segment.x2

    def contains(self, p: float):
        return self.x1 <= p <= self.x2


class COInterval(Interval):
    LEFT_CHAR = '['
    RIGHT_CHAR = ')'

    def __repr__(self):
        return self.repr(self.LEFT_CHAR, self.RIGHT_CHAR)

    @staticmethod
    def is_right_open():
        return True

    def merge(self, right_interval: Interval):
        if right_interval.is_right_open():
            return COInterval(self.x1, right_interval.x2)
        else:
            return CCInterval(self.x1, right_interval.x2)

    def intersect_with(self, segment: Segment):
        return segment.x1 < self.x2 and self.x1 <= segment.x2

    def contains(self, p: float):
        return self.x1 <= p < self.x2


class OCInterval(Interval):
    LEFT_CHAR = '('
    RIGHT_CHAR = ']'

    def __repr__(self):
        return self.repr(self.LEFT_CHAR, self.RIGHT_CHAR)

    @staticmethod
    def is_right_open():
        return False

    def merge(self, right_interval: Interval):
        if right_interval.is_right_open():
            return OOInterval(self.x1, right_interval.x2)
        else:
            return OCInterval(self.x1, right_interval.x2)

    def intersect_with(self, segment: Segment):
        return segment.x1 <= self.x2 and self.x1 < segment.x2

    def contains(self, p: float):
        return self.x1 < p <= self.x2


class OOInterval(Interval):
    LEFT_CHAR = '('
    RIGHT_CHAR = ')'

    def __repr__(self):
        return self.repr(self.LEFT_CHAR, self.RIGHT_CHAR)

    @staticmethod
    def is_right_open():
        return True

    def merge(self, right_interval: Interval):
        if right_interval.is_right_open():
            return OOInterval(self.x1, right_interval.x2)
        else:
            return OCInterval(self.x1, right_interval.x2)

    def intersect_with(self, segment: Segment):
        return segment.x1 < self.x2 and self.x1 < segment.x2

    def contains(self, p: float):
        return self.x1 < p < self.x2
