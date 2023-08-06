

class Link:
    empty = ()
    def __init__(self, first, rest=empty):
        assert isinstance(rest, Link) or rest is Link.empty, "Link(<first>, <rest>): If you chose to include <rest>, it must be an instance of Link.\nType Link.examples() to view examples."
        self.first = first
        self.rest = rest
    def __repr__(self):
        if self.rest:
            repr_rest = ", " + repr(self.rest)
        else:
            repr_rest = ""
        return "Link(" + repr(self.first) + repr_rest + ")"
    def examples():
        print('\nLink(1)\nLink(1, Link(2))\nLink(1, Link(2, Link(3)))\n')