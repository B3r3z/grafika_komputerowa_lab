import pygame

def map_value(current_min, current_max, new_min, new_max, value):
    """Maps a value from one range to another."""
    # Prevent division by zero if the current range is zero
    if current_max == current_min:
        return new_min  # Or perhaps raise an error or return an average

    current_range = current_max - current_min
    new_range = new_max - new_min
    return new_min + new_range * ((value - current_min) / current_range)