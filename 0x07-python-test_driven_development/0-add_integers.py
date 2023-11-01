>>> add_integer = __import__('0-add_integer').add_integer


>>> add_integer(4, 5)
9
>>> add_integer(4.0, 5.50)
9


>>> add_integer(None, 5)
Traceback (most recent call last):
TypeError: a must be an integer


>>> add_integer(7, None)
Traceback (most recent call last):
TypeError: b must be an integer


>>> add_integer(None, None)
Traceback (most recent call last):
TypeError: a must be an integer


>>> add_integer(5)
103


>>> add_integer(5, "mo")
Traceback (most recent call last):
TypeError: b must be an integer


>>> add_integer("mo", 8)
Traceback (most recent call last):
TypeError: a must be an integer


>>> add_integer(999999999999999999999999999999, 1)
1000000000000000000000000000000


>>> add_integer(1e308, 1e308)
200000000000000002195812725888091083480984619354623692673621365806315170809822983074326657956989377798122499339442345031223180567486280176656614018396292092062543329005866054371394979399177118086676768932330002356853795252425890355256182391573414916245567940343568830210583605786415746545949771430860446236672
