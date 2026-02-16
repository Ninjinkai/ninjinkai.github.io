# Nick Petty's Portfolio

A modern, modular portfolio built with Jekyll for GitHub Pages. Features responsive design, AI/ML focus, and a clean component-based architecture.

## ✨ Features

- **Jekyll-powered**: Native GitHub Pages support, automatic builds
- **Component-driven**: Modular includes for easy maintenance
- **Responsive Grid Layout**: Compact, side-by-side cards (Work 2-col, Education 3-col)
- **Modern Styling**: Clean, contemporary design with smooth interactions
- **Accessibility**: Semantic HTML5 and ARIA attributes
- **SEO Optimized**: Proper meta tags via `_config.yml`
- **AI/ML Focus**: Highlighted expertise in QA automation and AI-driven testing
- **Complete Sections**: Hero, Experience, Education, About (with Skills/Languages), and Contact

## 🛠️ Tech Stack

- **Static Site Generator**: Jekyll
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Framework**: Bootstrap 5.3.0
- **Deployment**: GitHub Pages (automatic)
- **Version Control**: Git

## 📁 Project Structure

```
ninjinkai.github.io/
├── _config.yml              # Jekyll configuration & site metadata
├── _layouts/
│   └── default.html         # Base HTML template
├── _includes/               # Reusable page components
│   ├── header.html          # Navigation header
│   ├── hero.html            # Hero/intro section
│   ├── featured.html        # Featured cards (Experience, About, Education, Contact)
│   ├── work.html            # Work history in 2-column grid
│   ├── education.html       # Education degrees in 3-column grid
│   ├── about.html           # About section with skills & languages
│   ├── contact.html         # Contact information
│   └── footer.html          # Footer
├── index.md                 # Main page (uses default layout)
├── css/
│   ├── bootstrap.css        # Bootstrap framework
│   └── custom.css           # Site-specific styles
├── img/
│   ├── mac.jpg              # Featured images
│   ├── alligator.jpg
│   ├── contact.jpg
│   └── favicon.ico
├── .gitignore               # Build artifacts excluded
├── README.md                # This file
└── README_JEKYLL.md         # Detailed Jekyll workflow doc
```

## 🚀 Getting Started

### View Live

Visit: **https://ninjinkai.github.io**

### Local Development (requires Jekyll)

```bash
git clone https://github.com/ninjinkai/ninjinkai.github.io.git
cd ninjinkai.github.io
bundle install
bundle exec jekyll serve
```

Visit `http://localhost:4000` to preview.

### Editing Content

- **Hero/About/Skills**: Edit `_includes/about.html`
- **Work Experience**: Edit `_includes/work.html` (2-column grid layout)
- **Education**: Edit `_includes/education.html` (3-column grid layout)
- **Featured Cards**: Edit `_includes/featured.html`
- **Contact Links**: Edit `_includes/contact.html`
- **Navigation**: Edit `_includes/header.html`
- **Site Metadata**: Edit `_config.yml`

Changes are reflected automatically when you `git push`.

## 📋 Page Sections

### Home (Hero)
Introduction with professional headline and call-to-action summary.

### Featured Cards
Quick-access navigation cards (2x2 grid):
- **Experience** — Links to detailed work history
- **About** — Links to skills and professional summary
- **Education** — Links to degree details
- **Contact** — Call-to-action for get in touch

### Experience
Work history in a dense **2-column grid layout**:
- **Modernizing Medicine** — Senior QA Engineer (8+ years)
- **DSS, Inc.** — QA Analyst roles
- **Unify** — Co-op in QA & Software Engineering
- **Apple** — Family Room Specialist
- **Berlitz Japan** — English Instructor

Each card shows key responsibilities and technologies.

### Education
Education in a **3-column grid layout** (most recent first):
- **Master of Science** — Computer Science (Florida Atlantic, 2016-2017)
- **Bachelor of Science** — Computer Science (Florida Atlantic, 2014-2015)
- **Bachelor of Science** — Mathematics (University of Florida, 1999-2003)

### About
Professional summary with organized skills:
- **Technical Skills**: Test Automation, Java, Selenium, TestRail, Git
- **QA Expertise**: Manual/Automated Testing (UI & API), Interviewing, Mentoring, AI/ML in QA
- **Languages**: English (Native), Japanese (Elementary), French (Limited)

### Contact
Direct links to:
- Email (nickpetty@hotmail.com)
- GitHub (github.com/ninjinkai)
- LinkedIn (linkedin.com/in/nicholasepetty)

## 🎯 Key Skills & Focus

- **QA Expertise**: Manual testing, test automation (Java/Selenium, UI & API)
- **Test Tools**: TestRail, Jira, Git
- **AI/ML**: Test optimization, intelligent test case generation
- **Soft Skills**: Interviewing, mentoring, team leadership
- **Languages**: English (Native), Japanese (Elementary), French (Limited)
- **Education**: M.S. & B.S. Computer Science, B.S. Mathematics

## � Layout & Design

- **Compact Design**: Reduced padding and spacing to minimize scrolling
- **Grid Layouts**: Work experience (2 columns), Education (3 columns) for dense information display
- **Skills Badges**: Organized skills by category using clean badge styling instead of progress bars
- **Responsive**: Mobile-first (1 column), tablet (2 columns), desktop (full grid)
- **Feature Cards**: 2x2 grid for quick navigation to all major sections

Push any changes to the `main` branch. GitHub Pages automatically builds and deploys via Jekyll.

```bash
git add .
git commit -m "Your message here"
git push origin main
```

## 📧 Contact

- **Email**: nickpetty@hotmail.com
- **LinkedIn**: [linkedin.com/in/nicholasepetty](https://www.linkedin.com/in/nicholasepetty/)
- **GitHub**: [github.com/ninjinkai](https://github.com/ninjinkai)

---

*Built with Jekyll • Hosted on GitHub Pages • Updated Feb 2026*

2. Open `index.html` in your web browser or use a local server:
```bash
# Using Python 3
python -m http.server 8000

# Using Node.js (with http-server)
npx http-server

# Using PHP
php -S localhost:8000
```

3. Visit `http://localhost:8000` in your browser

### Deployment

This site is automatically deployed to GitHub Pages when changes are pushed to the main branch.

## 📝 Customization

### Update Personal Information

Edit the following in `index.html`:

- **Contact Email**: Search for `nick@example.com` and replace with your email
- **Social Links**: Update GitHub and LinkedIn URLs in the Contact section
- **Project Descriptions**: Customize project titles and descriptions in the Work section
- **About Section**: Update personal bio and skill levels

### Customize Styling

Edit `css/custom.css` to modify:

- Color scheme (update CSS custom properties in `:root`)
- Font sizes and typography
- Animations and transitions
- Layout and spacing

## 🎯 Browser Support

- Chrome/Edge (latest)
- Firefox (latest)
- Safari (latest)
- Mobile browsers (iOS Safari, Chrome Mobile)

## 📱 Responsive Breakpoints

- **Mobile**: < 576px
- **Tablet**: 576px - 768px
- **Desktop**: > 768px

## ✨ Recent Updates

- ✅ Upgraded to Bootstrap 5
- ✅ Modernized HTML structure
- ✅ Enhanced CSS with animations and transitions
- ✅ Updated copyright to 2026
- ✅ Improved accessibility with descriptive alt text
- ✅ Added real content sections
- ✅ Fixed all broken navigation links
- ✅ Added skill progress bars
- ✅ Implemented contact section with social links
- ✅ Created comprehensive README

## 🐛 Known Issues

None currently. Please report issues via GitHub Issues.

## 📄 License

© 2026 Nick Petty. All rights reserved.

## 🤝 Contributing

Feel free to fork this repository and submit pull requests for any improvements.

---

**Last Updated**: February 2026

**Hosted at**: https://ninjinkai.github.io
