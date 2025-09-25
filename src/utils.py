import numpy as np

import numpy as np
from matplotlib.colors import LinearSegmentedColormap
from config import (PARTICLE_SIZE, WAVE_COUNT, WAVE_AMPLITUDE, 
                   WAVE_OPACITY, PARTICLE_COUNT, PARTICLE_SPEED)

def generate_wave_points(x, amplitude, frequency, phase, harmonic=1):
    """
    Generate points for a single wave with harmonics
    """
    base_wave = amplitude * np.sin(frequency * x + phase)
    harmonic_wave = (amplitude * 0.3) * np.sin(frequency * harmonic * x + phase)
    return base_wave + harmonic_wave

def create_gradient_colormap(colors):
    """
    Create a custom colormap from a list of colors
    """
    return LinearSegmentedColormap.from_list('custom', colors, N=256)

def generate_particle_positions(frame, count, width, height, speed):
    """
    Generate particle positions for decorative effect
    """
    t = frame * speed
    x = width * np.random.rand(count)
    y = height * 0.5 + np.sin(x * 0.02 + t) * height * 0.2
    sizes = np.random.rand(count) * PARTICLE_SIZE
    return x, y, sizes

def interpolate_color(colors, factor):
    """
    Interpolate between multiple colors based on factor
    """
    def hex_to_rgb(hex_color):
        hex_color = hex_color.lstrip('#')
        return tuple(int(hex_color[i:i+2], 16) / 255.0 for i in (0, 2, 4))
    
    n_colors = len(colors)
    if n_colors == 0:
        return '#000000'
    elif n_colors == 1:
        return colors[0]
    
    # Convert all colors to RGB
    rgb_colors = [hex_to_rgb(c) for c in colors]
    
    # Find which colors to interpolate between
    idx = int(factor * (n_colors - 1))
    if idx >= n_colors - 1:
        return colors[-1]
    
    local_factor = factor * (n_colors - 1) - idx
    c1 = rgb_colors[idx]
    c2 = rgb_colors[idx + 1]
    
    # Interpolate
    result = tuple(c1[i] * (1 - local_factor) + c2[i] * local_factor for i in range(3))
    
    # Convert back to hex
    return '#{:02x}{:02x}{:02x}'.format(
        int(result[0] * 255),
        int(result[1] * 255),
        int(result[2] * 255)
    )

def calculate_wave_parameters(temperature):
    """
    Calculate wave parameters based on temperature
    """
    # Normalize temperature to 0-1 range (assuming temperature range 0-40°C)
    temp_normalized = min(max(temperature, 0), 40) / 40
    
    # Calculate wave parameters with more dynamic ranges
    amplitude = 40 + (temp_normalized * 40)   # Range: 40-80
    frequency = 0.8 + (temp_normalized * 2.4) # Range: 0.8-3.2
    speed = 0.08 + (temp_normalized * 0.14)   # Range: 0.08-0.22
    
    # Additional parameters for visual effects
    glow = 0.3 + (temp_normalized * 0.4)      # Range: 0.3-0.7
    turbulence = 0.5 + (temp_normalized * 1.5) # Range: 0.5-2.0
    
    return amplitude, frequency, speed, glow, turbulence