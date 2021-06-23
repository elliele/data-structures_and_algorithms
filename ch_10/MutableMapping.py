# Created by Ellie Le at 6/22/2021

class MutableMapping:

    def __contains__(self, k):
        try:
            self[k]
            return True
        except KeyError:
            return False

    def setdefault(self, k, d):
        try:
            return self[k]
        except KeyError:
            self[k] = d
            return d