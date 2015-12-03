
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
