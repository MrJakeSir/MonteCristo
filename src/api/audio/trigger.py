"""
MonteCristo trigger, it can be a double tap (doesn't require AI) or 
a certain keyword (requires AI)
"""
# import pyaudio


class Trigger:
    def __init__(self, ttype: int = 0):
        """
        init function
        args:
            ttype: int -> Type of trigger, may be 0 (tap) or 1 (speech recognition)
        """
        trigger = (self.on_tap, self.on_keyword)
        trigger[ttype]()

    def on_tap(self):
        return None

    def on_keyword(self):
        return None
