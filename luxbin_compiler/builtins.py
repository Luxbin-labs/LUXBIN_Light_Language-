"""
LUXBIN Standard Library Built-in Functions

Provides the standard library functions for the LUXBIN language.
All functions receive a 'vm' parameter for VM integration.
"""

import math
import random
from typing import Any, Dict, Tuple, Callable, Optional


def photon_print(value: Any, vm=None) -> None:
    """Output to light display (console)."""
    output = str(value) if value is not None else "nil"
    print(output)
    if vm:
        vm.output.append(output)
    return None


def photon_input(prompt: str = "", vm=None) -> str:
    """Read from light sensor (console input)."""
    return input(prompt)


def photon_read(path: str, vm=None) -> str:
    """Read file as wavelength sequence."""
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return ""


def photon_write(path: str, data: Any, vm=None) -> bool:
    """Write wavelength sequence to file."""
    try:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(str(data))
        return True
    except IOError:
        return False


# Math functions
def photon_abs(n: float, vm=None) -> float:
    return abs(n)


def photon_sqrt(n: float, vm=None) -> float:
    return math.sqrt(n)


def photon_pow(base: float, exp: float, vm=None) -> float:
    return math.pow(base, exp)


def photon_sin(n: float, vm=None) -> float:
    return math.sin(n)


def photon_cos(n: float, vm=None) -> float:
    return math.cos(n)


def photon_tan(n: float, vm=None) -> float:
    return math.tan(n)


def photon_floor(n: float, vm=None) -> int:
    return math.floor(n)


def photon_ceil(n: float, vm=None) -> int:
    return math.ceil(n)


def photon_round(n: float, vm=None) -> int:
    return round(n)


def photon_min(a: float, b: float, vm=None) -> float:
    return min(a, b)


def photon_max(a: float, b: float, vm=None) -> float:
    return max(a, b)


def photon_random(vm=None) -> float:
    return random.random()


def photon_randint(a: int, b: int, vm=None) -> int:
    return random.randint(int(a), int(b))


# String/Wavelength functions
def photon_len(seq: Any, vm=None) -> int:
    if seq is None:
        return 0
    return len(seq)


def photon_concat(a: str, b: str, vm=None) -> str:
    return str(a) + str(b)


def photon_slice(seq: Any, start: int, end: int, vm=None) -> Any:
    return seq[int(start):int(end)]


def photon_wavelength(char: str, vm=None) -> float:
    from .lexer import CHAR_WAVELENGTHS
    if char and len(char) > 0:
        return CHAR_WAVELENGTHS.get(char[0], 540.3)
    return 540.3


def photon_char(wavelength: float, vm=None) -> str:
    from .lexer import CHAR_WAVELENGTHS
    closest = min(CHAR_WAVELENGTHS.items(), key=lambda x: abs(x[1] - wavelength))
    return closest[0]


def photon_upper(s: str, vm=None) -> str:
    return str(s).upper()


def photon_lower(s: str, vm=None) -> str:
    return str(s).lower()


def photon_split(s: str, sep: str = " ", vm=None) -> list:
    return str(s).split(sep)


def photon_join(arr: list, sep: str = "", vm=None) -> str:
    return sep.join(str(x) for x in arr)


def photon_strip(s: str, vm=None) -> str:
    return str(s).strip()


# Array functions
def photon_array(size: int, vm=None) -> list:
    return [None] * int(size)


def photon_push(arr: list, val: Any, vm=None) -> list:
    arr.append(val)
    return arr


def photon_pop(arr: list, vm=None) -> Any:
    if arr:
        return arr.pop()
    return None


def photon_get(arr: list, index: int, vm=None) -> Any:
    idx = int(index)
    if 0 <= idx < len(arr):
        return arr[idx]
    return None


def photon_set(arr: list, index: int, val: Any, vm=None) -> list:
    idx = int(index)
    if 0 <= idx < len(arr):
        arr[idx] = val
    return arr


def photon_sort(arr: list, vm=None) -> list:
    return sorted(arr)


def photon_reverse(arr: list, vm=None) -> list:
    return list(reversed(arr))


def photon_range(start: int, end: int = None, step: int = 1, vm=None) -> list:
    if end is None:
        return list(range(int(start)))
    return list(range(int(start), int(end), int(step)))


# Type conversion functions
def photon_to_int(value: Any, vm=None) -> int:
    if value is None:
        return 0
    if isinstance(value, bool):
        return 1 if value else 0
    try:
        return int(float(value))
    except (ValueError, TypeError):
        return 0


def photon_to_float(value: Any, vm=None) -> float:
    if value is None:
        return 0.0
    try:
        return float(value)
    except (ValueError, TypeError):
        return 0.0


def photon_to_string(value: Any, vm=None) -> str:
    if value is None:
        return "nil"
    return str(value)


def photon_to_bool(value: Any, vm=None) -> bool:
    if value is None:
        return False
    if isinstance(value, str):
        return len(value) > 0
    if isinstance(value, (list, dict)):
        return len(value) > 0
    return bool(value)


def photon_type(value: Any, vm=None) -> str:
    if value is None:
        return "nil"
    if isinstance(value, bool):
        return "bool"
    if isinstance(value, int):
        return "int"
    if isinstance(value, float):
        return "float"
    if isinstance(value, str):
        return "string"
    if isinstance(value, list):
        return "array"
    return type(value).__name__


# Quantum functions (simulated)
def quantum_superpose(*states, vm=None):
    from .vm import Qubit
    qubit = Qubit()
    n = len(states) if states else 2
    amp = 1.0 / math.sqrt(n)
    qubit.state = [complex(amp, 0), complex(amp, 0)]
    return qubit


def quantum_measure(qubit, vm=None) -> int:
    from .vm import Qubit
    if isinstance(qubit, Qubit):
        if random.random() < qubit.probability_zero():
            qubit.state = [complex(1, 0), complex(0, 0)]
            return 0
        else:
            qubit.state = [complex(0, 0), complex(1, 0)]
            return 1
    return 0


def quantum_entangle(q1, q2, vm=None) -> None:
    from .vm import Qubit
    if isinstance(q1, Qubit) and isinstance(q2, Qubit):
        q1.entangled_with = q2
        q2.entangled_with = q1
    return None


def quantum_hadamard(qubit, vm=None):
    from .vm import Qubit
    if isinstance(qubit, Qubit):
        a, b = qubit.state
        sqrt2 = math.sqrt(2)
        qubit.state = [(a + b) / sqrt2, (a - b) / sqrt2]
    return qubit


def quantum_cnot(control, target, vm=None) -> None:
    from .vm import Qubit
    if isinstance(control, Qubit) and isinstance(target, Qubit):
        if abs(control.state[1]) > abs(control.state[0]):
            target.state = [target.state[1], target.state[0]]
    return None


def quantum_phase(qubit, angle: float, vm=None):
    from .vm import Qubit
    if isinstance(qubit, Qubit):
        phase = complex(math.cos(angle), math.sin(angle))
        qubit.state[1] *= phase
    return qubit


def quantum_teleport(qubit, destination, vm=None) -> bool:
    from .vm import Qubit
    if isinstance(qubit, Qubit) and isinstance(destination, Qubit):
        destination.state = qubit.state.copy()
        qubit.state = [complex(1, 0), complex(0, 0)]
        return True
    return False


def __import__(module: str, vm=None):
    return {}


# Registry: name -> (function, num_args), -1 means variable args
BUILTINS: Dict[str, Tuple[Callable, int]] = {
    'photon_print': (photon_print, 1),
    'photon_input': (photon_input, 1),
    'photon_read': (photon_read, 1),
    'photon_write': (photon_write, 2),
    'photon_abs': (photon_abs, 1),
    'photon_sqrt': (photon_sqrt, 1),
    'photon_pow': (photon_pow, 2),
    'photon_sin': (photon_sin, 1),
    'photon_cos': (photon_cos, 1),
    'photon_tan': (photon_tan, 1),
    'photon_floor': (photon_floor, 1),
    'photon_ceil': (photon_ceil, 1),
    'photon_round': (photon_round, 1),
    'photon_min': (photon_min, 2),
    'photon_max': (photon_max, 2),
    'photon_random': (photon_random, 0),
    'photon_randint': (photon_randint, 2),
    'photon_len': (photon_len, 1),
    'photon_concat': (photon_concat, 2),
    'photon_slice': (photon_slice, 3),
    'photon_wavelength': (photon_wavelength, 1),
    'photon_char': (photon_char, 1),
    'photon_upper': (photon_upper, 1),
    'photon_lower': (photon_lower, 1),
    'photon_split': (photon_split, 2),
    'photon_join': (photon_join, 2),
    'photon_strip': (photon_strip, 1),
    'photon_array': (photon_array, 1),
    'photon_push': (photon_push, 2),
    'photon_pop': (photon_pop, 1),
    'photon_get': (photon_get, 2),
    'photon_set': (photon_set, 3),
    'photon_sort': (photon_sort, 1),
    'photon_reverse': (photon_reverse, 1),
    'photon_range': (photon_range, -1),
    'photon_to_int': (photon_to_int, 1),
    'photon_to_float': (photon_to_float, 1),
    'photon_to_string': (photon_to_string, 1),
    'photon_to_bool': (photon_to_bool, 1),
    'photon_type': (photon_type, 1),
    'quantum_superpose': (quantum_superpose, -1),
    'quantum_measure': (quantum_measure, 1),
    'quantum_entangle': (quantum_entangle, 2),
    'quantum_hadamard': (quantum_hadamard, 1),
    'quantum_cnot': (quantum_cnot, 2),
    'quantum_phase': (quantum_phase, 2),
    'quantum_teleport': (quantum_teleport, 2),
    '__import__': (__import__, 1),
}
