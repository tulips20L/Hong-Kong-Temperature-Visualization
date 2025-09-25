#!/bin/bash

# GitHub Repository Setup Script for HK Temperature & Mandelbrot Project
# This script helps you set up the project as a public GitHub repository

echo "🚀 Setting up Hong Kong Temperature & Mandelbrot Art Project for GitHub..."

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored output
print_step() {
    echo -e "${BLUE}📋 Step $1:${NC} $2"
}

print_success() {
    echo -e "${GREEN}✅ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠️ $1${NC}"
}

print_error() {
    echo -e "${RED}❌ $1${NC}"
}

# Check if git is installed
if ! command -v git &> /dev/null; then
    print_error "Git is not installed. Please install Git first."
    exit 1
fi

print_step "1" "Initializing Git repository..."

# Initialize git repository if not already done
if [ ! -d ".git" ]; then
    git init
    print_success "Git repository initialized"
else
    print_success "Git repository already exists"
fi

print_step "2" "Adding all files to Git..."
git add .

print_step "3" "Creating initial commit..."
git commit -m "🎉 Initial commit: Hong Kong Temperature & Mandelbrot Art Project

Features:
- 🌡️ Real-time Hong Kong weather data integration
- 🎨 Temperature-influenced Mandelbrot fractal art
- 📚 Comprehensive educational Jupyter notebooks
- ⚡ Optimized vectorized fractal generation
- 🎭 Multiple artistic themes and color schemes
- 📊 Professional temperature visualizations

Ready for educational use and collaboration!"

print_step "4" "Setting up remote repository..."

echo ""
echo "🎯 Next steps to complete GitHub setup:"
echo ""
echo "1. Create a new repository on GitHub:"
echo "   - Go to: https://github.com/new"
echo "   - Repository name: hk-temperature-mandelbrot"
echo "   - Description: 🌡️ Hong Kong Temperature & Mandelbrot Art - Real-time weather data meets mathematical fractal art"
echo "   - Make it public ✅"
echo "   - Don't initialize with README, .gitignore, or license (we have them already)"
echo ""

echo "2. Connect your local repository to GitHub:"
echo "   Replace 'yourusername' with your GitHub username:"
echo ""
echo -e "   ${YELLOW}git remote add origin https://github.com/yourusername/hk-temperature-mandelbrot.git${NC}"
echo -e "   ${YELLOW}git branch -M main${NC}"
echo -e "   ${YELLOW}git push -u origin main${NC}"
echo ""

echo "3. Update README.md badges:"
echo "   Replace 'yourusername' in README.md with your actual GitHub username"
echo ""

echo "4. Enable GitHub features:"
echo "   - ✅ Issues (for bug reports and feature requests)"
echo "   - ✅ Discussions (for community questions)"
echo "   - ✅ Actions (CI/CD pipeline is already configured)"
echo "   - ✅ Pages (if you want to host documentation)"
echo ""

echo "5. Configure repository settings:"
echo "   - Add topics: python, jupyter, fractals, mandelbrot, weather-data, visualization, art, hong-kong"
echo "   - Set up branch protection for main branch"
echo "   - Enable 'Delete head branches' for clean PR workflow"
echo ""

echo "🎉 Your project is ready for GitHub! After following the steps above, you'll have:"
echo "   ✨ Professional repository structure"
echo "   📝 Comprehensive documentation"
echo "   🔄 Automated CI/CD pipeline"
echo "   🤝 Contribution guidelines and templates"
echo "   📜 MIT license for open source collaboration"
echo ""

print_success "Setup script completed successfully!"

echo ""
echo "💡 Pro tips:"
echo "   - Star your own repository to show it's actively maintained"
echo "   - Share it on social media with hashtags: #Python #Fractals #DataVisualization #HongKong"
echo "   - Consider submitting to awesome lists and Python galleries"
echo "   - Add a 'Made with ❤️ in Hong Kong' note to show local pride"
echo ""

echo "🌟 Happy coding and thank you for contributing to open source!"