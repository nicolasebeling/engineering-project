"""
Implements the calculation of the margin of safety assuming a ratio of 1.5 between ultimate and limit load as commonly done in aerospace.
"""


def ms(allowable: float, actual: float) -> float:
    """
    :param allowable: allowable (ultimate) load
    :param actual: actual (limit) load
    :return: margin of safety
    """
    return allowable / (1.5 * actual) - 1
