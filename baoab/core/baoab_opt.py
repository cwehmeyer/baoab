
import numpy as np

def baoab_step(q0, p0, dth, factor_a, factor_b, hamiltonian):
    # factor_a = np.exp(-damping * dt)
    # factor_b = kt * (1.0 - np.exp(-2.0 * damping * dt))
    p1 = p0 + dth * hamiltonian.potential_gradient(q0)
    q1 = q0 - dth * p1 / hamiltonian.mass
    p1 = factor_a * p1 + \
        np.sqrt(factor_b / hamiltonian.mass) * \
        np.random.normal(size=p1.shape)
    q1 = q1 - dth * p1 / hamiltonian.mass
    p1 = p1 + dth * hamiltonian.potential_gradient(q1)
    return q1, p1

def baoab_run(n_samples, q0, p0, dth, factor_a, factor_b, hamiltonian, skip=1):
    q = []
    p = []
    q1 = q0.copy()
    p1 = p0.copy()
    for _step in range(n_samples):
        for _skip in range(skip):
            q1, p1 = baoab_step(q1, p1, dth, factor_a, factor_b, hamiltonian)
        q.append(q1)
        p.append(p1)
    return np.array(q), np.array(p)
