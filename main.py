from Segment import Segment
from SegmentTree import SegmentTree

s1 = Segment('s1', 1., 4.)
s2 = Segment('s2', 3., 5.)
s3 = Segment('s3', 6., 8.)
s4 = Segment('s4', 7., 8.)
s5 = Segment('s5', 3., 7.)

S = [s1, s2, s3, s4, s5]

st = SegmentTree(S)
print(st)
print(st.search(0))
print(st.search(2))
print(st.search(5))
print(st.search(10))
