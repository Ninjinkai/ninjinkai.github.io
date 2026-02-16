# Nick Petty's Portfolio

A modern, modular portfolio built with Jekyll for GitHub Pages.

## Project Structure

```
ninjinkai.github.io/
├── _config.yml              # Jekyll configuration
├── _layouts/
│   └── default.html         # Base HTML template
├── _includes/               # Reusable components
│   ├── header.html          # Navigation header
│   ├── hero.html            # Hero/intro section
│   ├── featured.html        # Featured cards (Experience, About, Contact)
│   ├── work.html            # Work history section
│   ├── about.html           # About & skills section
│   ├── contact.html         # Contact section
│   └── footer.html          # Footer
├── index.md                 # Main page (front matter + includes)
├── css/
│   ├── bootstrap.css        # Bootstrap framework
│   └── custom.css           # Site-specific styles
├── img/                     # Images (favicon, rounded profile images)
├── scripts/                 # Build/helper scripts
└── README.md                # This file
```

## Key Features

- **Jekyll-based**: Native GitHub Pages support, no build step required
- **Component-driven**: Each section is a reusable include
- **Clean separation**: Content, layouts, and styling are modular
- **Bootstrap 5**: Responsive CSS framework
- **GitHub Pages ready**: Just push to `main` branch, site builds automatically

## How It Works

1. **index.md** — The main page with front matter that specifies the layout
2. **_layouts/default.html** — Base template that includes header, footer, and renders content
3. **_includes/*.html** — Individual page sections loaded in index.md
4. **CSS** — Bootstrap + custom styles for theming

### Adding/Modifying Content

- **To update a section** (e.g., Work Experience): Edit `_includes/work.html`
- **To change layout/structure**: Edit `_layouts/default.html`
- **To style**: Update `css/custom.css`
- **To add metadata** (title, description): Update `_config.yml`

## Local Development

To preview locally (if Jekyll is installed):

```bash
bundle install
bundle exec jekyll serve
# Visit http://localhost:4000
```

## GitHub Pages Deployment

Push changes to the `main` branch. GitHub Pages automatically builds and deploys.

## Skills & Experience

- **LinkedIn**: [nicholasepetty](https://www.linkedin.com/in/nicholasepetty/)
- **GitHub**: [ninjinkai](https://github.com/ninjinkai)
- **Email**: nickpetty@hotmail.com
