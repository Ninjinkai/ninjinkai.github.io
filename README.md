# Nick Petty's Portfolio

A modern, modular portfolio built with Jekyll for GitHub Pages. Features responsive design, optimized hero section, and a clean component-based architecture.

## ✨ Features

- **Jekyll-powered**: Native GitHub Pages support, automatic builds
- **Component-driven**: Modular includes for easy maintenance
- **Responsive Grid Layout**: Compact, side-by-side cards (Work 2-col, Education 3-col)
- **Modern Styling**: Clean, contemporary design with smooth interactions
- **Optimized Hero**: Tight, engaging intro section with professional headline
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
│   ├── hero.html            # Hero/intro section with engaging summary
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
│   └── favicon.svg          # Site favicon
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

- **Hero Section**: Edit `_includes/hero.html` (name, headline, summary)
- **Featured Cards**: Edit `_includes/featured.html` (Experience, About, Education, Contact links)
- **Work Experience**: Edit `_includes/work.html` (2-column grid layout)
- **Education**: Edit `_includes/education.html` (3-column grid layout)
- **About/Skills**: Edit `_includes/about.html` (professional summary, skills, languages)
- **Contact Links**: Edit `_includes/contact.html` (email, GitHub, LinkedIn)
- **Navigation**: Edit `_includes/header.html`
- **Site Metadata**: Edit `_config.yml` (site title, email, author, social usernames)

Changes are reflected automatically when you `git push`.

## 📋 Page Sections

### Home (Hero)
Professional headline with engaging summary highlighting QA expertise and AI/ML focus. Optimized for quick impact with tight spacing.

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

## 🎨 Layout & Design

- **Optimized Hero**: Compact, engaging intro with professional headline and AI/ML focus
- **Compact Design**: Reduced padding and spacing to minimize scrolling
- **Grid Layouts**: Work (2 columns), Education (3 columns) for dense information display
- **Skills Badges**: Organized skills by category using clean badge styling
- **Responsive**: Mobile-first (1 column), tablet (2 columns), desktop (full grid)
- **Feature Cards**: 2x2 grid for quick navigation to major sections
- **Clean Images**: Removed unnecessary images for faster load times and cleaner design

## 🔧 Deployment

Push any changes to the main branch. GitHub Pages automatically builds and deploys via Jekyll.

```bash
git add .
git commit -m "Your message here"
git push origin main
```

## 📧 Contact

- **Email**: nickpetty@hotmail.com
- **LinkedIn**: [linkedin.com/in/nicholasepetty](https://www.linkedin.com/in/nicholasepetty/)
- **GitHub**: [github.com/ninjinkai](https://github.com/ninjinkai)

## ✨ Recent Updates

- ✅ Refactored to Jekyll modular architecture
- ✅ Extracted LinkedIn profile data (work history, education, skills)
- ✅ Optimized hero section with engaging summary
- ✅ Added AI/ML focus to professional headline
- ✅ Converted work experience to 2-column grid layout
- ✅ Converted education to 3-column grid layout
- ✅ Replaced progress bars with organized skill badges
- ✅ Added featured cards for quick navigation
- ✅ Removed unnecessary images for cleaner design
- ✅ Compact layout to minimize scrolling
- ✅ Improved accessibility and SEO

---

*Built with Jekyll • Hosted on GitHub Pages • Updated Feb 2026*
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

## ✨ Recent Updates

- ✅ Refactored to Jekyll modular architecture
- ✅ Extracted LinkedIn profile data (work history, education, skills)
- ✅ Optimized hero section with engaging summary
- ✅ Added AI/ML focus to professional headline
- ✅ Converted work experience to 2-column grid layout
- ✅ Converted education to 3-column grid layout
- ✅ Replaced progress bars with organized skill badges
- ✅ Added featured cards for quick navigation
- ✅ Removed unnecessary images for cleaner design
- ✅ Compact layout to minimize scrolling
- ✅ Improved accessibility and SEO

---

*Built with Jekyll • Hosted on GitHub Pages • Updated Feb 2026*
