"""
🌀 Hong Kong Temperature Mandelbrot Visualization
Combines real temperature data with the mathematical beauty of Mandelbrot fractals
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import requests
from datetime import datetime, timedelta

def fetch_hk_temperature():
    """Fetch current Hong Kong temperature for fractal mapping"""
    try:
        api_url = "https://data.weather.gov.hk/weatherAPI/opendata/weather.php"
        response = requests.get(f"{api_url}?dataType=rhrread&lang=en", timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            temp_data = data.get('temperature', {}).get('data', [])
            
            # Get HKO temperature
            for station in temp_data:
                if 'Observatory' in station.get('place', ''):
                    return float(station.get('value', 26.5))
            
            # Fallback to first available
            if temp_data:
                return float(temp_data[0].get('value', 26.5))
                
        return 26.5  # Default Hong Kong temperature
        
    except Exception:
        return 26.5  # Fallback

def generate_temperature_pattern(base_temp):
    """Generate 24-hour temperature pattern for fractal mapping"""
    hours = np.arange(24)
    
    # Physics-based Hong Kong temperature model
    daily_temps = []
    for hour in hours:
        if hour <= 6:  # Pre-dawn cooling
            offset = -3.5 - (6-hour) * 0.4
        elif hour <= 14:  # Solar heating
            offset = -3.5 + (hour-6) * 0.85
        elif hour <= 18:  # Afternoon peak
            offset = 3.3 - (hour-14) * 0.5
        else:  # Evening cooling
            offset = 1.3 - (hour-18) * 0.45
        
        # Add realistic variation
        offset += np.random.normal(0, 0.3)
        daily_temps.append(base_temp + offset)
    
    return np.array(daily_temps)

def mandelbrot_iteration(c, max_iter=100):
    """Calculate Mandelbrot iterations for a complex number"""
    z = 0
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z*z + c
    return max_iter

def create_temperature_mandelbrot(temps, width=800, height=600, max_iter=100):
    """Create Mandelbrot set colored by temperature data"""
    
    # Temperature statistics for mapping
    temp_min, temp_max = np.min(temps), np.max(temps)
    temp_range = temp_max - temp_min
    
    print(f"🌡️ Temperature Range: {temp_min:.1f}°C - {temp_max:.1f}°C")
    print(f"🌀 Generating {width}x{height} Mandelbrot fractal...")
    
    # Create complex plane with temperature-influenced bounds
    # Map temperature to fractal zoom and position
    temp_factor = (np.mean(temps) - 20) / 10  # Normalize around 20°C
    
    # Temperature influences the viewing window
    zoom = 1.5 + temp_factor * 0.3  # Warmer = more zoomed
    center_x = -0.5 + temp_factor * 0.1  # Slight horizontal shift
    center_y = 0 + temp_factor * 0.05   # Slight vertical shift
    
    x_min, x_max = center_x - zoom, center_x + zoom
    y_min, y_max = center_y - zoom, center_y + zoom
    
    # Generate complex plane
    x = np.linspace(x_min, x_max, width)
    y = np.linspace(y_min, y_max, height)
    X, Y = np.meshgrid(x, y)
    C = X + 1j*Y
    
    # Calculate Mandelbrot set
    mandelbrot_set = np.zeros((height, width))
    
    print("🎨 Computing fractal iterations...")
    for i in range(height):
        for j in range(width):
            mandelbrot_set[i, j] = mandelbrot_iteration(C[i, j], max_iter)
        
        if i % (height // 10) == 0:
            progress = (i / height) * 100
            print(f"   Progress: {progress:.0f}%")
    
    # Temperature-based color mapping
    # Map 24 temperature values to fractal regions
    temp_zones = np.zeros_like(mandelbrot_set)
    
    # Divide fractal into temperature regions
    for i in range(height):
        for j in range(width):
            # Map position to hour of day (0-23)
            hour_idx = int((j / width) * 23)
            temp_zones[i, j] = temps[hour_idx]
    
    return mandelbrot_set, temp_zones, (temp_min, temp_max)

def create_temperature_mandelbrot_art(current_temp):
    """Create the ultimate temperature-Mandelbrot artistic fusion"""
    
    # Generate temperature pattern
    daily_temps = generate_temperature_pattern(current_temp)
    
    # Create Mandelbrot fractal influenced by temperature
    mandelbrot_data, temp_zones, temp_range = create_temperature_mandelbrot(
        daily_temps, width=1200, height=900, max_iter=150
    )
    
    # Setup the artistic visualization
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(20, 16), dpi=150)
    fig.patch.set_facecolor('#0a0a0a')
    
    # 1. Classic Mandelbrot with temperature colors
    temp_colormap = LinearSegmentedColormap.from_list(
        'temp_mandelbrot', 
        ['#000033', '#0066ff', '#00ffff', '#ffff00', '#ff6600', '#ff0000', '#ffffff']
    )
    
    im1 = ax1.imshow(mandelbrot_data, extent=[-2, 2, -2, 2], 
                     cmap=temp_colormap, origin='lower', interpolation='bilinear')
    ax1.set_title('Temperature-Influenced Mandelbrot Set', 
                  fontsize=16, color='white', fontweight='bold')
    ax1.set_xlabel('Real Axis', color='white')
    ax1.set_ylabel('Imaginary Axis', color='white')
    ax1.tick_params(colors='white')
    
    # 2. Temperature zones overlay
    temp_cmap = LinearSegmentedColormap.from_list(
        'hk_temps',
        ['#4a90e2', '#f39c12', '#e74c3c']  # Cool blue to warm red
    )
    
    im2 = ax2.imshow(temp_zones, extent=[-2, 2, -2, 2], 
                     cmap=temp_cmap, origin='lower', alpha=0.8, 
                     vmin=temp_range[0], vmax=temp_range[1])
    ax2.set_title('Temperature Mapping Overlay', 
                  fontsize=16, color='white', fontweight='bold')
    ax2.set_xlabel('Real Axis', color='white') 
    ax2.set_ylabel('Imaginary Axis', color='white')
    ax2.tick_params(colors='white')
    
    # Add temperature colorbar
    cbar2 = plt.colorbar(im2, ax=ax2, fraction=0.046, pad=0.04)
    cbar2.set_label('Temperature (°C)', color='white')
    cbar2.ax.yaxis.set_tick_params(color='white')
    
    # 3. Hybrid fractal-temperature fusion
    # Blend Mandelbrot iterations with temperature data
    hybrid_data = mandelbrot_data * 0.7 + (temp_zones - temp_range[0]) / (temp_range[1] - temp_range[0]) * 50
    
    fusion_cmap = LinearSegmentedColormap.from_list(
        'fusion',
        ['#0f0f23', '#1a1a3a', '#2d4a7c', '#4a90e2', '#74c0fc', 
         '#ffcc5c', '#ff8a50', '#ff5722', '#e91e63', '#9c27b0']
    )
    
    im3 = ax3.imshow(hybrid_data, extent=[-2, 2, -2, 2], 
                     cmap=fusion_cmap, origin='lower', interpolation='bilinear')
    ax3.set_title('Fractal-Temperature Fusion Art', 
                  fontsize=16, color='white', fontweight='bold')
    ax3.set_xlabel('Real Axis', color='white')
    ax3.set_ylabel('Imaginary Axis', color='white')
    ax3.tick_params(colors='white')
    
    # 4. Temperature timeline with fractal styling
    hours = np.arange(24)
    
    # Create fractal-styled temperature curve
    ax4.set_facecolor('#1a1a1a')
    
    # Plot temperature with fractal-inspired styling
    ax4.plot(hours, daily_temps, color='#ff6b6b', linewidth=4, alpha=0.9,
             marker='o', markersize=8, markerfacecolor='#ff4757',
             markeredgecolor='white', markeredgewidth=2)
    
    # Add fractal-inspired background pattern
    for i in range(5):
        alpha = 0.1 - i * 0.015
        offset = i * 0.5
        ax4.fill_between(hours, daily_temps - offset, daily_temps + offset,
                        alpha=alpha, color='#4ecdc4')
    
    ax4.set_title('Hong Kong Temperature Rhythm', 
                  fontsize=16, color='white', fontweight='bold')
    ax4.set_xlabel('Hour of Day', color='white')
    ax4.set_ylabel('Temperature (°C)', color='white')
    ax4.tick_params(colors='white')
    ax4.grid(True, alpha=0.3, color='gray')
    
    # Add current temperature indicator
    current_hour = datetime.now().hour
    ax4.axvline(x=current_hour, color='#ffe66d', linestyle='--', 
                linewidth=3, alpha=0.8)
    ax4.annotate(f'NOW\n{current_temp:.1f}°C', 
                xy=(current_hour, current_temp), 
                xytext=(10, 20), textcoords='offset points',
                bbox=dict(boxstyle='round,pad=0.8', fc='#ffe66d', alpha=0.9),
                arrowprops=dict(arrowstyle='->', color='white'),
                color='black', fontweight='bold', ha='center')
    
    # Overall title and styling
    fig.suptitle('Hong Kong Temperature Mandelbrot Fusion Art', 
                 fontsize=24, color='white', fontweight='bold', y=0.95)
    
    # Add timestamp
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    fig.text(0.5, 0.02, f'Generated: {timestamp} | Current: {current_temp:.1f}°C', 
             ha='center', color='lightgray', fontsize=12)
    
    # Style all axes
    for ax in [ax1, ax2, ax3, ax4]:
        ax.set_facecolor('#1a1a1a')
        for spine in ax.spines.values():
            spine.set_color('white')
            spine.set_alpha(0.7)
    
    plt.tight_layout()
    plt.subplots_adjust(top=0.9, bottom=0.08)
    
    return fig, daily_temps

def main():
    """Create temperature-Mandelbrot fusion masterpiece"""
    
    print("HONG KONG TEMPERATURE MANDELBROT ART GENERATOR")
    print("=" * 60)
    print("Fetching live Hong Kong temperature data...")
    
    current_temp = fetch_hk_temperature()
    print(f"Current Hong Kong temperature: {current_temp:.1f}°C")
    print("Generating fractal temperature fusion art...")
    print("This may take a few minutes due to fractal calculations...")
    
    # Create the masterpiece
    fig, temps = create_temperature_mandelbrot_art(current_temp)
    
    # Save with beautiful filename
    timestamp = datetime.now().strftime('%Y%m%d_%H%M')
    filename = f"hk_temp_mandelbrot_fusion_{timestamp}.png"
    
    plt.savefig(filename, dpi=300, bbox_inches='tight', 
               facecolor='#0a0a0a', pad_inches=0.2)
    
    print(f"Mandelbrot fusion masterpiece saved: {filename}")
    print(f"Temperature range: {np.min(temps):.1f}°C - {np.max(temps):.1f}°C")
    print("Mathematical beauty meets meteorological data!")
    print("=" * 60)
    
    # Display the art
    plt.show()

if __name__ == "__main__":
    main()