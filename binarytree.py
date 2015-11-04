__author__ = 'harryhao'


def Node(object):

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None