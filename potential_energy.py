""""Barbara Rodriguez Lopez"""
"""Energía Potencial Gravitatoria"""
def potential(G: float, M: float, m: float, r: float) -> float:
    E = -G*((M*m)/r)
    return E


