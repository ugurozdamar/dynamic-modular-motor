
import math
from fractions import Fraction


class AdvancedFormulaEngine:
    """
    Advanced Formula Engine
    Version: 1.1.0

    Copyright (C) 2026 YOUR NAME

    Licensed under GNU GPLv3.
    """

    VERSION = "1.1.0"
    MAX_EXPONENT = 1000
    MAX_BASE = 100

    def __init__(self):
        print("=" * 55)
        print(f"ADVANCED FORMULA ENGINE v{self.VERSION}")
        print("Mathematical Verification System")
        print("=" * 55)

    def _validate_integer(self, value, name):
        if isinstance(value, bool) or not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")

    def _validate_size(self, n, s=None):
        if abs(n) > self.MAX_EXPONENT:
            raise ValueError("Exponent exceeds safety limit")

        if s is not None and abs(s) > self.MAX_BASE:
            raise ValueError("Base exceeds safety limit")

    def verify_complex_mod_model(self, n, s):
        print(f"\n[Complex Mod] n={n}, s={s}")

        try:
            self._validate_integer(n, "n")
            self._validate_integer(s, "s")
            self._validate_size(n, s)

            if s == 0:
                raise ZeroDivisionError("s cannot be zero")

            numerator = 2 ** n + 1
            s_power_n = Fraction(s) ** n

            k = (
                (s_power_n - s + 1)
                * Fraction(numerator, s)
                + s
            )

            if k == 0:
                raise ZeroDivisionError("Generated modulus is zero")

            result = Fraction(numerator) % k

            print("Generated k:", k)
            print("Result:", result)

            return result

        except (ValueError, TypeError, ZeroDivisionError) as error:
            print("Validation error:", error)
            return None

    def verify_integer_model(self, n, S, m=1):
        print(f"\n[Integer Model] n={n}, S={S}, m={m}")

        try:
            self._validate_integer(n, "n")
            self._validate_integer(S, "S")
            self._validate_integer(m, "m")
            self._validate_size(n)

            if m == 0:
                raise ZeroDivisionError("m cannot be zero")

            main_number = 2 ** n + 1
            k = Fraction(2 ** n - S + 1, m)

            if k == 0:
                raise ZeroDivisionError("k cannot be zero")

            result = Fraction(main_number) % k

            print("Generated k:", k)
            print("Result:", result)

            return result

        except (ValueError, TypeError, ZeroDivisionError) as error:
            print("Error:", error)
            return None

    def verify_rational_model(self, n, S_fraction, m=1):
        print(f"\n[Rational Model] n={n}")

        try:
            self._validate_integer(n, "n")
            self._validate_integer(m, "m")
            self._validate_size(n)

            S = Fraction(S_fraction)

            if m == 0:
                raise ZeroDivisionError("m cannot be zero")

            main_number = 2 ** n + 1
            k = Fraction(2 ** n + 1, m) - S / m

            if k == 0:
                raise ZeroDivisionError("k cannot be zero")

            result = Fraction(main_number) % k

            print("S:", S)
            print("k:", k)
            print("Result:", result)

            return result

        except (ValueError, TypeError, ZeroDivisionError) as error:
            print("Error:", error)
            return None

    def verify_irrational_model(self, S, m=1, precision=50):
        print(f"\n[Irrational Model] S={S}")

        try:
            from decimal import Decimal, localcontext

            if isinstance(precision, bool) or not isinstance(precision, int):
                raise TypeError("Precision must be an integer")

            if not 10 <= precision <= 500:
                raise ValueError("Precision must be between 10 and 500")

            if m == 0:
                raise ZeroDivisionError("m cannot be zero")

            with localcontext() as ctx:
                ctx.prec = precision

                two = Decimal(2)
                pi = Decimal(
                    "3.14159265358979323846264338327950288419716939937510"
                )

                main_number = (two ** pi) + 1
                s_value = Decimal(str(S))
                k = (main_number - s_value + 1) / Decimal(str(m))

                if k == 0:
                    raise ZeroDivisionError("k cannot be zero")

                result = main_number % k

                print("Precision:", precision)
                print("k:", k)
                print("Result:", result)

                return result

        except (ValueError, TypeError, ZeroDivisionError) as error:
            print("Error:", error)
            return None

    def verify_trigonometric_wave_model(self, degrees, m=1):
        print(f"\n[Trigonometric Model] degrees={degrees}")

        try:
            if m == 0:
                raise ZeroDivisionError("m cannot be zero")

            radians = math.radians(degrees)

            S = (
                math.sin(radians) ** 2
                + math.cos(radians) ** 2
            )

            main_number = 2 ** degrees + 1
            k = (main_number - S + 1) / m

            if math.isclose(k, 0.0, abs_tol=1e-12):
                raise ZeroDivisionError("k is approximately zero")

            result = math.fmod(main_number, k)

            print("Trigonometric S:", S)
            print("Generated k:", k)
            print("Result:", result)

            return result

        except (ValueError, TypeError, OverflowError,
                ZeroDivisionError) as error:
            print("Error:", error)
            return None

    def verify_autonomous_inf_model(self, S):
        raise PermissionError(
            "Stage 5 is restricted to Enterprise Edition."
        )


if __name__ == "__main__":

    engine = AdvancedFormulaEngine()

    engine.verify_complex_mod_model(5, 2)
    engine.verify_complex_mod_model(-3, 2)
    engine.verify_complex_mod_model(3, -2)
    engine.verify_complex_mod_model(-2, -2)
    engine.verify_complex_mod_model(10, 0)

    engine.verify_integer_model(10, 3)
    engine.verify_rational_model(6, Fraction(5, 3))
    engine.verify_irrational_model(3)
    engine.verify_trigonometric_wave_model(45)
