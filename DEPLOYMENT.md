# Deployment Guide

This guide will help you deploy your portfolio website to various hosting platforms.

## 🚀 Quick Deploy Options

### 1. GitHub Pages (Recommended - Free)

**Step 1: Push to GitHub**
```bash
git init
git add .
git commit -m "Initial portfolio commit"
git branch -M main
git remote add origin https://github.com/jasebris03/portfolio.git
git push -u origin main
```

**Step 2: Enable GitHub Pages**
1. Go to your repository on GitHub
2. Click "Settings" tab
3. Scroll down to "Pages" section
4. Under "Source", select "Deploy from a branch"
5. Choose "main" branch and "/ (root)" folder
6. Click "Save"

Your site will be available at: `https://jasebris03.github.io/portfolio`

### 2. Netlify (Free Tier)

**Option A: Drag & Drop**
1. Go to [netlify.com](https://netlify.com)
2. Sign up/login
3. Drag your project folder to the deploy area
4. Your site is live!

**Option B: Connect GitHub**
1. Go to [netlify.com](https://netlify.com)
2. Click "New site from Git"
3. Connect your GitHub account
4. Select your repository
5. Deploy settings: Build command: (leave empty), Publish directory: `.`
6. Click "Deploy site"

### 3. Vercel (Free Tier)

1. Go to [vercel.com](https://vercel.com)
2. Sign up/login with GitHub
3. Click "New Project"
4. Import your repository
5. Deploy settings: Framework Preset: "Other", Root Directory: `.`
6. Click "Deploy"

### 4. Surge.sh (Free)

```bash
# Install Surge globally
npm install --global surge

# Deploy
surge

# Follow the prompts to create account and deploy
```

## 🔧 Custom Domain Setup

### GitHub Pages
1. In repository settings → Pages
2. Add your custom domain
3. Update DNS records:
   - Type: CNAME
   - Name: www (or @)
   - Value: `jasebris03.github.io`

### Netlify
1. Go to Site settings → Domain management
2. Add custom domain
3. Update DNS records as instructed

## 📱 Testing Your Deployment

After deployment, test:
- [ ] Homepage loads correctly
- [ ] Navigation works
- [ ] Projects load from GitHub
- [ ] Mobile responsiveness
- [ ] Contact links work
- [ ] Performance (use Google PageSpeed Insights)

## 🔄 Updating Your Site

### Automatic Updates (GitHub Actions)
The included workflow will automatically:
1. Extract CV data
2. Deploy to GitHub Pages
3. Optionally deploy to Netlify

Just push changes to main branch:
```bash
git add .
git commit -m "Update portfolio"
git push origin main
```

### Manual Updates
1. Make your changes
2. Run `python extract_cv.py` to update data
3. Push to GitHub
4. Your hosting platform will automatically redeploy

## 🛠️ Troubleshooting

### Common Issues

**Projects not loading:**
- Check browser console for errors
- Verify `portfolio_data.json` exists
- Ensure GitHub username is correct

**Styling issues:**
- Clear browser cache
- Check CSS file paths
- Verify Font Awesome is loading

**Deployment fails:**
- Check GitHub Actions logs
- Verify file permissions
- Ensure all files are committed

### Performance Optimization

1. **Compress images** (if you add any)
2. **Minify CSS/JS** (optional)
3. **Enable gzip compression** (hosting dependent)
4. **Use CDN** for external resources

## 📊 Analytics Setup

### Google Analytics
1. Create Google Analytics account
2. Add tracking code to `<head>` in `index.html`:
```html
<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=GA_MEASUREMENT_ID"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'GA_MEASUREMENT_ID');
</script>
```

### GitHub Pages Analytics
- Available in repository settings
- Shows page views and referrers

## 🔒 Security Considerations

- Keep dependencies updated
- Use HTTPS (automatic on most platforms)
- Don't commit sensitive data
- Regular backups of your content

## 📞 Support

If you encounter issues:
1. Check the hosting platform's documentation
2. Review browser console for errors
3. Test locally first
4. Check GitHub Actions logs (if using)

---

**Happy Deploying! 🚀** 