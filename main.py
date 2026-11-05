import math

class AdvancedFormulaEngine:
    def __init__(self):
        """
        Initializes the Dynamic Modular Formula Engine under GNU GPLv3 protection.
        """
        self.version = "1.0.0-Core (GPLv3)"
        print(f"====================================================")
        print(f"🌀 INITIALIZING ADVANCED FORMULA ENGINE v{self.version} 🌀")
        print(f"====================================================")

    def verify_complex_mod_model(self, n, s):
        """
        CRITICAL FORMULA: f(n,s) = (2^n + 1) mod k
        with k = (s^n - s + 1) * ((2^n + 1) / s) + s
        
        FULL NEGATIVE, POSITIVE & ZERO CRASH PROTECTION INCLUDED.
        """
        print(f"\n--- [Complex Mod Verification] n={n}, s={s} ---")
        
        # 🛡️ PROTECTION 1: Zero Division Check
        if s == 0:
            print("🚨 Crash Avoided: 's' cannot be 0 (Division by Zero)!")
            return None

        # 🛡️ PROTECTION 2: Negative Base with Float Exponent Check (Complex Number Crash)
        if s < 0 and isinstance(n, float):
            print("🚨 Crash Avoided: Negative base with float exponent creates undefined complex domains!")
            return None

        try:
            # 🛡️ PROTECTION 3: Overflow Prevention for huge numbers
            if abs(n) > 1000 or (abs(s) > 100 and abs(n) > 50):
                print("🚨 Crash Avoided: Input values are too large (Memory Overflow risk)!")
                return None

            # 1. Base components calculation
            numerator = (2 ** n) + 1
            s_power_n = s ** n
            
            # 2. Calculating the dynamic base 'k'
            k = (s_power_n - s + 1) * (numerator / s) + s
            
            # 🛡️ PROTECTION 4: Modulo by zero or negative k check
            if k <= 0:
                print(f"🚨 Crash Avoided: Generated base 'k' ({k}) is negative or zero. Modulo undefined.")
                return None

            # 3. Final Function f(n,s) = numerator % k
            result = numerator % k
            
            print(f"Generated Base (k)         : {k}")
            print(f"Formula Output f(n,s)      : {result}")
            return result

        except OverflowError:
            print("🚨 Crash Avoided: Math overflow error handled successfully.")
            return None
        except Exception as e:
            print(f"🚨 Unexpected Error Handled: {e}")
            return None

    def verify_integer_model(self, n, S, m=1):
        """ STAGE 1: Basic Integer Model """
        print(f"\n--- [Stage 1: Integer Verification] n={n}, S={S} ---")
        try:
            main_number = (2 ** n) + 1
            k = ((2 ** n) - S + 1) / m
            if k <= 0:
                print("🚨 Error: k cannot be negative or zero.")
                return None
            remainder = main_number % k
            print(f"Formula Output (Remainder) : {remainder}")
            return remainder
        except Exception as e:
            print(f"🚨 Error: {e}")
            return None

    def verify_rational_model(self, n, S_fraction, m=1):
        """ STAGE 2: Rational Model """
        print(f"\n--- [Stage 2: Rational Verification] n={n}, S={S_fraction:.4f} ---")
        try:
            main_number = (2 ** n) + 1
            k = ((2 ** n) - S_fraction + 1) / m
            remainder = main_number % k
            print(f"Formula Output (Remainder)   : {remainder:.4f}")
            return remainder
        except Exception as e:
            print(f"🚨 Error: {e}")
            return None

    def verify_irrational_model(self, n_pi, S, m=1):
        """ STAGE 3: Irrational Model """
        print(f"\n--- [Stage 3: Irrational Verification] n=π, S={S} ---")
        try:
            main_number = (2 ** n_pi) + 1
            k = ((2 ** n_pi) - S + 1) / m
            remainder = main_number % k
            print(f"Formula Output (Remainder)   : {remainder}")
            return remainder
        except Exception as e:
            print(f"🚨 Error: {e}")
            return None

    def verify_trigonometric_wave_model(self, n_degrees, m=1):
        """ STAGE 4: Trigonometric Wave Model """
        print(f"\n--- [Stage 4: Trigonometric Wave Verification] n={n_degrees}° ---")
        try:
            n_radians = math.radians(n_degrees)
            S = (math.sin(n_radians) ** 2) + (math.cos(n_radians) ** 2)
            main_number = (2 ** n_degrees) + 1
            k = ((2 ** n_degrees) - S + 1) / m
            remainder = main_number % k
            print(f"Formula Output (Remainder)   : {remainder}")
            return remainder
        except Exception as e:
            print(f"🚨 Error: {e}")
            return None

    def verify_autonomous_inf_model(self, S):
        """ ENTERPRISE FEATURE - STAGE 5 """
        raise PermissionError(
            "CRITICAL: Stage 5 Autonomous Engine is restricted to the ENTERPRISE EDITION."
        )

if __name__ == "__main__":
    engine = AdvancedFormulaEngine()
    
    # 🧪 EXHAUSTIVE TESTING WITH POSITIVE, NEGATIVE AND ZERO VALUES
    engine.verify_complex_mod_model(n=5, s=2)       # Positive Test
    engine.verify_complex_mod_model(n=-3, s=2)      # Negative Exponent Test
    engine.verify_complex_mod_model(n=3, s=-2)      # Negative Base Test
    engine.verify_complex_mod_model(n=-2, s=-2)    # Double Negative Test (Triggers Protection)
    engine.verify_complex_mod_model(n=10, s=0)      # Zero Base Test (Triggers Protection)
    engine.verify_complex_mod_model(n=5000, s=200)  # Extreme Value Test (Triggers Protection)
    
    # Engine verification blocks
    engine.verify_integer_model(n=10, S=3)
    engine.verify_rational_model(n=6, S_fraction=5/3)
