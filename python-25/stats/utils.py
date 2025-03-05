from typing import Iterable


def min_max(liste: Iterable) -> tuple:
    """Retourne le minimum et le maximum d'une liste"""

    for e in liste:
        if not isinstance(e, (int, float)):
            raise ValueError("La liste doit contenir des nombres")

    return min(liste), max(liste)
