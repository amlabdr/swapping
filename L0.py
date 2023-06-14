import math

def calculate_attenuation_factor(attenuation_length):
    attenuation_factor = 10 * math.log10(1 / attenuation_length)
    return attenuation_factor

# Example usage
attenuation_length = 22  # in km
attenuation_factor = calculate_attenuation_factor(attenuation_length)
print(f"Attenuation Factor: {attenuation_factor:.2f} dB/m")
