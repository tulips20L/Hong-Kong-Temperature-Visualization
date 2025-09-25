# Configuration settings for the tidal patterns visualization

# Animation settings
FPS = 60
DURATION = None  # Run indefinitely
FRAME_COUNT = None  # Run indefinitely
UPDATE_INTERVAL = 60  # Update temperature every 60 frames (about 1 second)

# Visualization parameters
WINDOW_SIZE = (1600, 900)  # Higher resolution
DPI = 100
WAVE_COUNT = 8  # More waves for complexity
PARTICLE_COUNT = 100  # Add particles for extra effect
BACKGROUND_COLOR = '#FFFFFF'  # White background

# Color settings for temperature visualization
COLOR_MAP = {
    'cold': ['#1E88E5', '#2196F3', '#64B5F6'],     # Deep blues
    'moderate': ['#43A047', '#4CAF50', '#81C784'],  # Rich greens
    'warm': ['#FB8C00', '#FF9800', '#FFB74D'],      # Deep oranges
    'hot': ['#E53935', '#F44336', '#EF5350']        # Rich reds
}

# Temperature thresholds (°C)
TEMP_THRESHOLDS = {
    'cold': 15,
    'moderate': 22,
    'warm': 28,
    'hot': 33
}

# Wave animation parameters
WAVE_AMPLITUDE = 60
WAVE_FREQUENCY = 2
WAVE_SPEED = 0.15

# Additional animation parameters
GLOW_EFFECT = True
WAVE_OPACITY = 0.6
PARTICLE_SIZE = 2
PARTICLE_SPEED = 0.5
GRADIENT_CYCLES = 3  # Number of color gradient cycles