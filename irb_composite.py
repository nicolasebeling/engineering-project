"""
Implements the calculation of the reserve factor against inter-rivet buckling in composite structures according to HSB 45131-02, issue A, 2019.

This method is valid for symmetric laminates which are orthotropic with respect to the x-y coordinate system where the x-axis is defined in the direction of the fastener row.
It is based on the equation for simple column buckling under uniaxial loading.

The result of the calculation is subject to the following constraints:
If both n_x and n_y are compressive, the plate is destabilized and the buckling resistance is lower than n_x_cr_irb.
If n_x is compressive and n_y is tensile, the plate is stabilized and the buckling resistance is higher than n_x_cr_irb.
If both n_x and n_y are tensile, buckling is impossible.

Abbreviations:
n_x = force flow in x-direction
n_y = force flow in y-direction
cr = critical
irb = inter-rivet buckling
"""

import math


def n_x_cr_irb(C: float, s: float, d11: float) -> float:
    """
    :param C: clamping factor as defined in HSB 45131-02
    :param s: fastener pitch
    :param d11: first term of the bending compliance matrix d
    :return: critical inter-rivet buckling force flow in x-direction for zero force flow in y-direction
    """
    return C * (math.pi / s) ** 2 / d11
