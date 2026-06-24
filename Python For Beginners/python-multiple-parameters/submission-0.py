Number = float | int

def add(a: Number, b: Number) -> float:
    return float(a + b)

print(add(2, 4))  # Output: 6.0
print(add("2", "4"))  # Output: 24.0