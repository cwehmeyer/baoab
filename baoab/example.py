
import numpy as np

class HarmonicPotential(object):
    def __init__(self, strength=1.0, mass=1.0):
        self.strength = strength
        self.mass = mass
    def potential_energy(self, q):
        return 0.5 * self.strength * (q**2).sum()
    def potential_gradient(self, q):
        return self.strength * q
    def kinetic_energy(self, p):
        return 0.5 * (p**2).sum() / self.mass
    def total_energy(self, q, p):
        return self.potential_energy(q) + self.kinetic_energy(p)
