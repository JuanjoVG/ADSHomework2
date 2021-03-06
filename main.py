from Segment import Segment
from SegmentTree import SegmentTree

s1 = Segment('s1', 1., 4.)
s2 = Segment('s2', 3., 5.)
s3 = Segment('s3', 6., 8.)
s4 = Segment('s4', 7., 8.)
s5 = Segment('s5', 3., 7.)

S = [s1, s2, s3, s4, s5]

st = SegmentTree(S)
assert st.search(0) == []
assert st.search(1) == ['s1']
assert st.search(3) == ['s1', 's2', 's5']
assert st.search(4) == ['s2', 's5', 's1']
assert st.search(4.1) == ['s2', 's5']
assert st.search(5) == ['s2', 's5']
assert st.search(5.99) == ['s5']
assert st.search(6) == ['s5', 's3']
assert st.search(7) == ['s5', 's3', 's4']
assert st.search(8) == ['s3', 's4']
assert st.search(10) == []
