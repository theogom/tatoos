import math
import matplotlib.pyplot as plt

MIN_LENGTH = 0.5
MAX_LENGTH = 3.0

def draw_tatoo(tick_positions: list[int], tick_lengths: list[int]):
    # Create a simple illustration with a baseline and perpendicular marks extending on both sides
    fig, ax = plt.subplots(figsize=(8, 2))

    # Draw baseline
    ax.hlines(0, 0, len(tick_positions), color="black", linewidth=1)

    for pos, length in zip(tick_positions, tick_lengths):
        ax.vlines(pos, -length / 2, length / 2, color="black", linewidth=1)

    ax.axis("off")
    plt.show()


# convert string to ticks by using binary
def to_binary_ticks(word: str):
    return [0.5 + 0.5 * int(bit) for char in word for bit in format(ord(char), "08b")]


# convert string to ticks by using morse code
def to_morse_ticks(word: str):
    morse_code = {
        "a": [0, 1],
        "b": [1, 0, 0, 0],
        "c": [1, 0, 1, 0],
        "d": [1, 0, 0],
        "e": [0],
        "f": [0, 0, 1, 0],
        "g": [1, 1, 0],
        "h": [0, 0, 0, 0],
        "i": [0, 0],
        "j": [0, 1, 1, 1],
        "k": [1, 0, 1],
        "l": [0, 1, 0, 0],
        "m": [1, 1],
        "n": [1, 0],
        "o": [1, 1, 1],
        "p": [0, 1, 1, 0],
        "q": [1, 1, 0, 1],
        "r": [0, 1, 0],
        "s": [0, 0, 0],
        "t": [1],
        "u": [0, 0, 1],
        "v": [0, 0, 0, 1],
        "w": [0, 1, 1],
        "x": [1, 0, 0, 1],
        "y": [1, 0, 1, 1],
        "z": [1, 1, 0, 0],
    }

    encoded: list[int] = []
    
    for char in word:
        bits = morse_code.get(char, [])
        encoded.extend([0.5 + 0.5 * bit for bit in bits])
        encoded.append(0)  # Add a 0 separator after each character
    
    if encoded:
        encoded.pop()  # Remove the last separator
    
    return encoded

def normalize(
    values: list[float], min_value: float | None = None, max_value: float | None = None
):
    if min_value is None:
        min_value = min(values)
    if max_value is None:
        max_value = max(values)
    span = (max_value - min_value) if max_value > min_value else 1.0
    return [MIN_LENGTH + (value - min_value) / span * (MAX_LENGTH - MIN_LENGTH) for value in values]

def lengths_linear(lengths: list[float]):
    return normalize(lengths)

def lengths_sqrt(lengths: list[float]):
    return normalize([math.sqrt(d) for d in lengths])

def lengths_log10(lengths: list[float]):
    return normalize([math.log10(d) for d in lengths])

# Draw perpendicular ticks of varying lengths (both sides)
random_tick_lengths = [0.5, 0.8, 0.3, 1.0, 0.6, 0.4, 1.2, 0.7, 0.9, 0.5]
random_tick_positions = [0.5, 1, 1.5, 2.5, 3, 3.5, 5, 6, 7.5, 9]

binary_tick_lengths = to_binary_ticks("theo")
binary_tick_positions = [i for i in range(len(binary_tick_lengths))]

morse_tick_lengths = to_morse_ticks("theo")
morse_tick_positions = [i for i in range(len(morse_tick_lengths))]

planet_radiuses = [695508, 2440, 6052, 6371, 3390, 69911, 58232, 25362, 24622]
planet_tick_positions = [i for i in range(len(planet_radiuses))]

# draw_tatoo(random_tick_positions, random_tick_lengths)
draw_tatoo(binary_tick_positions, binary_tick_lengths)
draw_tatoo(morse_tick_positions, morse_tick_lengths)
draw_tatoo(planet_tick_positions, lengths_linear(planet_radiuses))
# draw_tatoo(planet_tick_positions, lengths_sqrt(planet_radiuses))
draw_tatoo(planet_tick_positions, lengths_log10(planet_radiuses))
