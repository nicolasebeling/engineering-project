"""
Implements the calculation of the reserve factor against inter-rivet buckling in metallic structures according to HSB 45131-01, issue C, 2004.

The x-axis is defined in the direction of the fastener row.
"""

import math


def sigma_x_cr_irb(s: float, t: float, C: float, Ec: float, Rc02: float) -> float:
    """
    :param s: fastener pitch in loading direction
    :param t: sheet thickness
    :param C: clamping factor as defined in HSB 45131-01
    :param Ec: compressive Young's modulus
    :param Rc02: compressive yield strength
    :return: critical inter-rivet stress
    """
    psi: float = 1.1027 * s / t * math.sqrt(Rc02 / C / Ec)
    if psi <= 1.5275:
        return (1 - 0.3027 * psi ** 1.5) * Rc02
    else:
        return Rc02 / psi ** 2
