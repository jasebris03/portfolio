# Jason Merefield - Portfolio Website

A modern, responsive portfolio website showcasing my skills as a Platform Engineer and Developer. Built with vanilla HTML, CSS, and JavaScript for optimal performance and easy deployment.

## 🚀 Features

- **Modern Design**: Clean, professional layout with a light sense of humour
- **Responsive**: Works perfectly on desktop, tablet, and mobile devices
- **Fast Loading**: Optimized for performance with minimal dependencies
- **Interactive**: Smooth animations and engaging user experience
- **Dynamic Content**: Automatically loads GitHub repositories and project data
- **SEO Optimized**: Proper meta tags and semantic HTML structure

## 🛠️ Technologies Used

- **HTML5**: Semantic markup for accessibility and SEO
- **CSS3**: Modern styling with CSS Grid, Flexbox, and custom properties
- **JavaScript (ES6+)**: Vanilla JS for interactivity and dynamic content
- **Font Awesome**: Icons for enhanced visual appeal
- **Google Fonts**: Inter font family for modern typography

## 📁 Project Structure

```
jm-portfolio/
├── index.html              # Main HTML file
├── styles.css              # CSS styles and animations
├── script.js               # JavaScript functionality
├── extract_cv.py           # Script to extract CV data
├── portfolio_data.json     # Generated portfolio data
├── CVs/                    # CV documents
│   └── JM Platform Engineer Resume 20250618.docx
├── .github/
│   └── workflows/
│       └── deploy.yml      # GitHub Actions deployment
└── README.md               # This file
```

## 🚀 Quick Start

### Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/jasebris03/jm-portfolio.git
   cd jm-portfolio
   ```

2. **Extract CV data** (optional - data is already included)
   ```bash
   python extract_cv.py
   ```

3. **Open in browser**
   - Simply open `index.html` in your web browser
   - Or use a local server:
     ```bash
     # Using Python
     python -m http.server 8000
     
     # Using Node.js
     npx serve .
     ```

### Deployment

#### Option 1: GitHub Pages (Recommended)

1. **Push to GitHub**
   ```bash
   git add .
   git commit -m "Initial portfolio commit"
   git push origin main
   ```

2. **Enable GitHub Pages**
   - Go to your repository settings
   - Navigate to "Pages" section
   - Select "Deploy from a branch"
   - Choose `main` branch and `/ (root)` folder
   - Your site will be available at `https://jasebris03.github.io/jm-portfolio`

#### Option 2: Netlify

1. **Connect to Netlify**
   - Sign up/login to [Netlify](https://netlify.com)
   - Connect your GitHub repository
   - Deploy automatically on push

#### Option 3: Vercel

1. **Connect to Vercel**
   - Sign up/login to [Vercel](https://vercel.com)
   - Import your GitHub repository
   - Deploy automatically on push

## 🔧 Customization

### Personal Information

1. **Update personal details** in `index.html`:
   - Name and title in the hero section
   - About me text
   - Contact information

2. **Update social links**:
   - LinkedIn URL
   - GitHub username
   - Any other social media links

### Styling

1. **Colors**: Modify CSS custom properties in `styles.css`:
   ```css
   :root {
       --primary-color: #2563eb;
       --accent-color: #f59e0b;
       /* ... other colors */
   }
   ```

2. **Fonts**: Change Google Fonts import in `index.html`

### Content

1. **Skills**: Update the skills section in `index.html`
2. **Projects**: The projects are automatically loaded from your GitHub repositories
3. **CV Data**: Run `extract_cv.py` to update portfolio data from your CV

## 📱 Responsive Design

The website is fully responsive and optimized for:
- **Desktop**: 1200px+ (full layout)
- **Tablet**: 768px - 1199px (adjusted grid layouts)
- **Mobile**: < 768px (stacked layout, mobile menu)

## 🎨 Design Features

- **Gradient backgrounds** for visual appeal
- **Smooth animations** and transitions
- **Floating cards** in hero section
- **Hover effects** on interactive elements
- **Custom scrollbar** styling
- **Loading animations** for better UX

## 🔍 SEO & Performance

- **Semantic HTML** for better accessibility
- **Meta tags** for social sharing
- **Optimized images** and assets
- **Minimal dependencies** for fast loading
- **Mobile-first** responsive design

## 🛠️ Development

### Adding New Features

1. **New Sections**: Add HTML structure and corresponding CSS
2. **Animations**: Use CSS animations or JavaScript for complex interactions
3. **Dynamic Content**: Extend the JavaScript to load additional data

### Browser Support

- **Modern browsers**: Chrome, Firefox, Safari, Edge (latest versions)
- **Mobile browsers**: iOS Safari, Chrome Mobile
- **Fallbacks**: Graceful degradation for older browsers

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🤝 Contributing

While this is a personal portfolio, suggestions and improvements are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests

## 📞 Contact

- **LinkedIn**: [Jason Merefield](https://www.linkedin.com/in/jasonmerefield)
- **GitHub**: [jasebris03](https://github.com/jasebris03)
- **Portfolio**: [Live Site](https://jasebris03.github.io/jm-portfolio)

---

Built with ❤️ and probably some ☕ by Jason Merefield 