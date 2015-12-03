
import numpy as np

def baoab_step(q0, p0, dt, kt, damping, hamiltonian):
    p1 = p0 + 0.5 * dt * hamiltonian.potential_gradient(q0)
    q1 = q0 - 0.5 * dt * p1 / hamiltonian.mass
    p1 = np.exp(-damping * dt) * p1 + \
        np.sqrt(kt * (1.0 - np.exp(-2.0 * damping * dt)) / hamiltonian.mass) * \
        np.random.normal(size=p1.shape)
    q1 = q1 - 0.5 * dt * p1 / hamiltonian.mass
    p1 = p1 + 0.5 * dt * hamiltonian.potential_gradient(q1)
    return q1, p1

def baoab_run(n_samples, q0, p0, dt, kt, damping, hamiltonian, skip=1):
    q = []
    p = []
    q1 = q0.copy()
    p1 = p0.copy()
    for _step in range(n_samples):
        for _skip in range(skip):
            q1, p1 = baoab_step(q1, p1, dt, kt, damping, hamiltonian)
        q.append(q1)
        p.append(p1)
    return np.array(q), np.array(p)
