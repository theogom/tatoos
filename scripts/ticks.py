import math
import matplotlib.pyplot as plt

MIN_TICK_LENGTH = 0.5
MAX_TICK_LENGTH = 3.0

def draw_tatoo(tick_lengths: list[float], tick_positions: list[int] | None = None, baseline_length: float | None = None):
    """Create a simple illustration with a baseline and perpendicular ticks extending on both sides"""
    if tick_positions is None:
        tick_positions = list(range(len(tick_lengths)))

    if baseline_length is None:
        # Add padding at the end
        baseline_length = max(tick_positions) + 1

    _, ax = plt.subplots(figsize=(8, 2))

    # Baseline
    ax.hlines(0, 0, baseline_length, color="black", linewidth=1)

    for position, length in zip(tick_positions, tick_lengths):
        ax.vlines(position, -length / 2, length / 2, color="black", linewidth=1)

    ax.axis("off")
    plt.show()


def to_binary_ticks(word: str):
    """Convert string to ticks by using binary"""
    return [0.5 + 0.5 * int(bit) for char in word for bit in format(ord(char), "08b")]


def to_morse_ticks(word: str):
    """Convert string to ticks by using morse code"""
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
        # Add a 0 separator after each character
        encoded.append(0)
    
    if encoded:
        # Remove the last separator
        encoded.pop()
    
    return encoded

def normalize(
    values: list[float], lower_bound: float, upper_bound: float
):
    """Normalize a list of values to a specific range using min-max scaling"""
    min_value = min(values)
    max_value = max(values)
    normalization_span = upper_bound - lower_bound
    value_span = (max_value - min_value) if max_value > min_value else 1.0
    return [lower_bound + (value - min_value) * normalization_span / value_span for value in values]


if __name__ == "__main__":
    binary_tick_lengths = to_binary_ticks("theo")
    binary_tick_positions = [i+1 for i in range(len(binary_tick_lengths))]

    morse_tick_lengths = to_morse_ticks("theo")
    morse_tick_positions = [i+1 for i in range(len(morse_tick_lengths))]

    planet_radiuses = [695_508, 2_440, 6_052, 6_371, 1_737, 3_390, 69_911, 58_232, 25_362, 24_622]
    planet_distances = [57_900_000, 108_200_000, 149_600_000, 227_900_000, 778_600_000, 1_433_500_000, 2_872_500_000, 4_495_100_000]
    planet_positions =  list(range(len(planet_radiuses) - 1))
    # Add Moon close to Earth
    planet_positions.insert(4, 3.15)
    planet_tick_lengths = normalize(list(map(math.log, planet_radiuses)), MIN_TICK_LENGTH, MAX_TICK_LENGTH)

    # draw_tatoo(binary_tick_lengths, binary_tick_positions)
    # draw_tatoo(morse_tick_lengths, morse_tick_positions)
    draw_tatoo(planet_tick_lengths, planet_positions, len(planet_positions) - 1)
