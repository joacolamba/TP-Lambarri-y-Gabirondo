from fractions import Fraction


def decimal_a_fraccion(numero_decimal):
    # Convertir el número decimal a fracción
    fraccion = Fraction(str(numero_decimal)).limit_denominator()
    
    return fraccion.denominator




