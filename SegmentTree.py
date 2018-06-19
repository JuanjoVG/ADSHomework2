from typing import List

from Interval import CCInterval, OOInterval, Interval
from Segment import Segment


class Node:

    def __init__(self, interval: Interval, left: 'Node' = None, right: 'Node' = None):
        self.interval = interval
        self.right = right
        self.left = left
        self.segments = []

    def __repr__(self):
        return str(self.interval) + '*' + str(self.segments) + '*' + ':{' + str(self.left) + ', ' + str(
            self.right) + '}'

    def create_parent(self, right: 'Node'):
        parent_interval = self.interval.merge(right.interval)
        parent = Node(parent_interval, self, right)
        return parent

    def insert(self, segment: Segment):
        if self.interval.contained_in(segment):
            self.segments.append(segment.id)
        else:
            if self.left and self.left.interval.intersect_with(segment):
                self.left.insert(segment)
            if self.right and self.right.interval.intersect_with(segment):
                self.right.insert(segment)

    def search(self, p: float):
        segments = []
        if self.interval.contains(p):
            segments += self.segments
            if self.left: segments += self.left.search(p)
            if self.right: segments += self.right.search(p)
        return segments


class SegmentTree:
    def __init__(self, segments: List[Segment]):
        points = [float('-Inf')] + sorted(set([p for s in segments for p in s.points]))
        n_points = len(points)
        intervals = [interval for i in range(1, n_points) for interval in
                     [OOInterval(points[i - 1], points[i]), CCInterval(points[i], points[i])]]
        intervals.append(OOInterval(points[-1], float('Inf')))
        self.root = self.build_segment_tree_from_intervals(intervals)
        for segment in segments:
            self.root.insert(segment)

    def __repr__(self):
        return str(self.root)

    @staticmethod
    def build_segment_tree_from_intervals(intervals: List[Interval]):
        nodes = [Node(interval) for interval in intervals]
        while len(nodes) > 1:
            new_nodes = []
            for i in range(len(nodes) // 2):
                ii = 2 * i
                new_nodes.append(nodes[ii].create_parent(nodes[ii + 1]))
            if len(nodes) % 2:
                new_nodes.append(nodes[-1])
            nodes = new_nodes
        return nodes[0]

    def search(self, p: float):
        return self.root.search(p)
