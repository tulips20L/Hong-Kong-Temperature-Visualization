# 🌡️ Hong Kong Temperature & Mandelbrot Art Project

A fascinating combination of real-time Hong Kong weather data and mathematical fractal art. This project fetches current temperature data from Hong Kong Observatory and creates beautiful visualizations using the Mandelbrot Set.

## 🎯 Project Overview

This project demonstrates the intersection of:
- **Real-world Data**: Live Hong Kong weather information
- **Mathematical Art**: Mandelbrot Set fractal visualizations  
- **Educational Content**: Step-by-step tutorials explaining both concepts
- **Creative Coding**: Temperature-influenced artistic parameters

## 📁 Project Structure

```
HK tem/
├── notebooks/                          # Jupyter Notebooks
│   ├── hk_temperature_chart_explained.ipynb      # Professional temperature visualization tutorial ⭐
│   └── mandelbrot_temperature_explained.ipynb    # Mandelbrot fractal art tutorial
├── src/                                # Python source code
│   ├── config.py                       # Configuration settings
│   ├── data_fetcher.py                # Hong Kong Observatory API client
│   ├── hk_temperature_chart.py        # Professional temperature visualization
│   ├── mandelbrot.py                  # Mandelbrot Set generation
│   └── utils.py                       # Utility functions
├── output/                            # Generated files
│   └── images/                        # Generated visualization images
│       ├── hk_temperature_*.png       # Professional temperature charts
│       └── hk_temp_mandelbrot_*.png   # Fractal art images
├── .github/                           # GitHub configuration
├── CHANGELOG.md                       # Project change history
├── requirements.txt                   # Python dependencies
├── .gitignore                         # Git ignore patterns
├── .venv/                             # Virtual environment (excluded from repo)
└── README.md                          # This file
```

## 🚀 Quick Start

1. **Install Dependencies**:
   ```bash
   pip install numpy matplotlib requests pandas seaborn
   ```

2. **Run the Main Tutorials**:
   - **NEW**: Open `notebooks/hk_temperature_chart_explained.ipynb` for professional weather visualization
   - Open `notebooks/mandelbrot_temperature_explained.ipynb` for fractal mathematics

3. **Explore the Code**:
   Check out the `src/` folder for individual Python modules

## 📚 What You'll Learn

### Temperature Visualization
- Fetching real-time data from Hong Kong Observatory API
- Creating professional temperature charts and gauges
- Color-coding temperature zones and humidity levels
- Data storytelling through visual design

### Mandelbrot Set Mathematics
- Understanding the formula: z = z² + c
- Vectorized computation using NumPy
- Creating beautiful fractal visualizations
- Exploring infinite zoom regions and self-similarity

### Creative Data Art
- Combining meteorological data with mathematical art
- Temperature-influenced color schemes and parameters
- Creating unique visualizations based on current weather
- Real-time artistic parameter adjustment

## 🎨 Featured Notebooks

### `hk_temperature_chart_explained.ipynb` ⭐ **NEW & RECOMMENDED**
Complete guide to professional weather data visualization:
- Part 1: Library imports and setup
- Part 2: Hong Kong Observatory API integration
- Part 3: Professional color system design
- Part 4: Multi-layer visual effects
- Part 5: Typography and layout design
- Part 6: Complete function workflow analysis
- Part 7: Best practices and learning points
- Part 8: Creating authentic temperature visualizations

### `mandelbrot_temperature_explained.ipynb` 
The mathematical art tutorial covering:
- Part 1: Library setup and data fetching
- Part 2: Hong Kong temperature data analysis  
- Part 3: Mandelbrot Set mathematics explanation
- Part 4: Fast vectorized fractal generation
- Part 5: Beautiful color schemes and artistic effects
- Part 6: Temperature-influenced fractal art
- Part 7: Exploring famous fractal regions
- Part 8: Creating unique weather-based masterpieces

## 🌡️ Data Sources

- **Hong Kong Observatory API**: Real-time temperature and humidity data
- **Backup System**: Realistic simulated data when API is unavailable
- **Multiple Stations**: King's Park, Tsim Sha Tsui, and other monitoring locations

## 🎭 Art Styles

The project creates different artistic moods based on temperature:
- **❄️ Cool (< 20°C)**: Blue winter themes
- **🍃 Mild (20-25°C)**: Fresh green nature themes  
- **🌞 Warm (25-30°C)**: Orange sunset themes
- **🔥 Hot (> 30°C)**: Red fire themes

## 🔧 Technical Features

- **Fast Performance**: Vectorized NumPy operations for rapid fractal generation
- **Real-time Data**: Live API integration with Hong Kong Observatory
- **Responsive Design**: Temperature-adaptive parameters and color schemes
- **Educational Focus**: Clear explanations of mathematical concepts
- **No File Clutter**: Direct visualization display without saving files

## 🎯 Use Cases

- **Education**: Teaching fractal mathematics and data visualization
- **Art**: Creating unique mathematical art pieces
- **Weather Monitoring**: Visual weather data representation
- **Programming**: Learning advanced Python visualization techniques

## 🛠️ Dependencies

- `numpy`: Fast numerical computations
- `matplotlib`: Professional plotting and visualization
- `requests`: Hong Kong Observatory API communication
- `pandas`: Data manipulation and analysis
- `seaborn`: Advanced statistical visualizations
- `jupyter`: Interactive notebook environment

## 📈 Performance

- **Fractal Generation**: ~5-10 seconds for high-quality 600x600 images
- **API Response**: ~1-2 seconds for weather data
- **Memory Usage**: Optimized for standard laptop configurations
- **Scalability**: Adjustable resolution and quality parameters

## 🌟 Getting Started

1. Clone or download this project
2. Install Python dependencies: `pip install -r requirements.txt`
3. **Start with**: `notebooks/hk_temperature_chart_explained.ipynb` for professional weather visualization
4. **Then explore**: `notebooks/mandelbrot_temperature_explained.ipynb` for mathematical art
5. Run all cells to see the complete demonstrations
6. Experiment with different parameters and regions

## 🎨 Sample Output

The project generates:
- **Professional temperature visualization charts** (NEW!)
- **Real-time weather dashboards with statistics** (NEW!)
- **Multi-layer temperature effects with glowing lines** (NEW!)
- Classic Mandelbrot Set displays
- Temperature-influenced fractal art
- Zoomed fractal detail explorations
- Unique daily weather-art masterpieces

---

*Created with ❤️ combining the beauty of mathematics with real-world data*