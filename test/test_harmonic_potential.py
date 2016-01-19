# This file is part of baoab.
#
# Copyright 2015 Computational Molecular Biology Group, Freie Universitaet Berlin (GER)
#
# baoab is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

r"""
This test module checks the outcome of the BAOAB Langevin dynamics integrator when applied
to a 5D harmonic potential.
"""

import baoab
import numpy as np
from numpy.testing import assert_almost_equal

def test_5D_300K_ref():
    strength = 20.0
    kt = 0.0083144621 * 300.0
    zero = np.zeros(shape=(5,), dtype=np.float64)
    hamiltonian = baoab.HarmonicPotential(strength=strength)
    ld = baoab.BAOAB(hamiltonian, 0.001, kt, 0.1, skip=100, method='reference')
    q, p = ld.run(zero, zero, 5000)
    assert_almost_equal(np.mean(q, axis=0), zero, decimal=2)
    assert_almost_equal(np.std(q, ddof=1), np.sqrt(kt / strength), decimal=1)

def test_5D_300K_opt():
    strength = 20.0
    kt = 0.0083144621 * 300.0
    zero = np.zeros(shape=(5,), dtype=np.float64)
    hamiltonian = baoab.HarmonicPotential(strength=strength)
    ld = baoab.BAOAB(hamiltonian, 0.001, kt, 0.1, skip=100, method='optimized')
    q, p = ld.run(zero, zero, 5000)
    assert_almost_equal(np.mean(q, axis=0), zero, decimal=2)
    assert_almost_equal(np.std(q, ddof=1), np.sqrt(kt / strength), decimal=1)

def test_5D_500K_ref():
    strength = 20.0
    kt = 0.0083144621 * 500.0
    zero = np.zeros(shape=(5,), dtype=np.float64)
    hamiltonian = baoab.HarmonicPotential(strength=strength)
    ld = baoab.BAOAB(hamiltonian, 0.001, kt, 0.1, skip=100, method='reference')
    q, p = ld.run(zero, zero, 5000)
    assert_almost_equal(np.mean(q, axis=0), zero, decimal=2)
    assert_almost_equal(np.std(q, ddof=1), np.sqrt(kt / strength), decimal=1)

def test_5D_500K_opt():
    strength = 20.0
    kt = 0.0083144621 * 500.0
    zero = np.zeros(shape=(5,), dtype=np.float64)
    hamiltonian = baoab.HarmonicPotential(strength=strength)
    ld = baoab.BAOAB(hamiltonian, 0.001, kt, 0.1, skip=100, method='optimized')
    q, p = ld.run(zero, zero, 5000)
    assert_almost_equal(np.mean(q, axis=0), zero, decimal=2)
    assert_almost_equal(np.std(q, ddof=1), np.sqrt(kt / strength), decimal=1)
