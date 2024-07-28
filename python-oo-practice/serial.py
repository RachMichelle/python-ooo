"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__ (self, start=1, step=1):
        """make a new generator, default start at 1 with incriments of 1"""

        self.start = self.next = start
        self.step = step

    def __repr__(self):

        return f"<SerialGenerator start={self.start} step={self.step} next={self.next}>"

    def generate(self):
        """set next value (increase by step) and return current value"""

        self.next += self.step 
        return self.next -self.step
    
    def reset(self):
        """return to start value""" 

        self.next = self.start

