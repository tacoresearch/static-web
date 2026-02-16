## Overview
This document outlines the approach for hosting a static website built from Markdown files on Linux. The solution will automatically convert Markdown files into HTML pages and serve them through a web server.

## Architecture
- **Content Source**: Markdown files (.md) in a dedicated directory
- **Build Process**: Convert Markdown to HTML
- **Hosting**: Linux web server (Apache or Nginx)
- **Deployment**: Manual or automated process

## Directory Structure
```
project/
├── content/
│   ├── index.md
│   ├── about.md
│   ├── blog/
│   │   ├── post1.md
│   │   └── post2.md
├── templates/
│   ├── base.html
│   └── post.html
├── static/
│   ├── css/
│   ├── js/
│   └── images/
├── build/
│   └── (generated HTML files)
└── README.md
```

## Implementation Options

### Option 1: Simple Script Approach
1. Create a build script that converts Markdown to HTML
2. Use a simple Python script or shell script
3. Deploy to web server manually

### Option 2: Static Site Generator
1. Use a tool like Jekyll, Hugo, or MkDocs
2. Configure for automatic build and deployment
3. Set up CI/CD pipeline for updates

### Option 3: Custom Solution
1. Write Python/Node.js script to process Markdown files
2. Generate HTML with proper templating
3. Handle navigation, styling, and assets

## Required Tools

### For Markdown Processing
- `pandoc` - for Markdown conversion
- `markdown` Python package
- `commonmark` for parsing

### For Web Server
- Apache or Nginx
- Python's built-in HTTP server for development

## Deployment Steps

1. **Setup Linux Environment**
   ```bash
   sudo apt update
   sudo apt install apache2
   # or
   sudo apt install nginx
   ```

2. **Create Content Structure**
   - Create content directory with Markdown files
   - Set up templates directory
   - Create static assets directory

3. **Build Process**
   - Run build script to convert Markdown to HTML
   - Place generated files in web server directory

4. **Configure Web Server**
   - Point web server to build directory
   - Set proper permissions
   - Configure virtual host if needed

## Sample Build Script (Python)

```python
#!/usr/bin/env python3
import os
import markdown
from shutil import copytree

def build_site():
    # Read Markdown files and convert to HTML
    # Copy static assets
    # Generate navigation
    pass

if __name__ == "__main__":
    build_site()
```

## Hosting Considerations

### Security
- Set proper file permissions
- Configure firewall
- Use HTTPS with Let's Encrypt

### Performance
- Enable compression (gzip)
- Set up caching
- Optimize static assets

### Automation
- Set up cron jobs for regular builds
- Use Git hooks for automatic deployment
- Implement CI/CD pipeline

## File Permissions
```
chmod 644 content/*.md
chmod 644 static/css/*.css
chmod 755 build/
```

## Testing
1. Test locally with Python's HTTP server
2. Verify all links work
3. Check responsive design
4. Validate HTML output
```

```markdown content/index.md
# Welcome to My Static Site

This is the homepage of my static website built from Markdown files.

## Features

- **Simple**: Built with Markdown
- **Fast**: Static HTML files
- **Secure**: No server-side processing
- **Flexible**: Easy to customize

## Getting Started

1. Create Markdown files in the `content` directory
2. Run the build script to generate HTML
3. Deploy to your web server

## Sample Content

Here's a sample paragraph with **bold** and *italic* text.

### Code Example

```python
def hello_world():
    print("Hello, World!")
```

## Navigation

- [About](about.html)
- [Blog](blog/index.html)
```

```markdown content/about.md
# About This Site

This static website demonstrates how to build a simple website using Markdown files.

## Purpose

The purpose of this project is to show how easy it is to create a website using:
- Markdown for content
- Simple HTML templates
- Linux hosting

## Technologies Used

- Markdown for content authoring
- Python for processing
- Apache/Nginx for hosting
- Linux for deployment

## How It Works

1. Write content in Markdown
2. Use a build script to convert to HTML
3. Serve static files with web server
4. Deploy to production

## Contact

For questions about this site, contact the maintainer.
```

```markdown templates/base.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% title %}</title>
    <link rel="stylesheet" href="/static/css/style.css">
</head>
<body>
    <header>
        <h1>My Static Site</h1>
        <nav>
            <a href="/">Home</a>
            <a href="/about.html">About</a>
            <a href="/blog/index.html">Blog</a>
        </nav>
    </header>
    
    <main>
        {% content %}
    </main>
    
    <footer>
        <p>&copy; 2023 My Static Site</p>
    </footer>
</body>
</html>
```

```markdown templates/post.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% title %}</title>
    <link rel="stylesheet" href="/static/css/style.css">
</head>
<body>
    <header>
        <h1>My Static Site</h1>
        <nav>
            <a href="/">Home</a>
            <a href="/about.html">About</a>
            <a href="/blog/index.html">Blog</a>
        </nav>
    </header>
    
    <main>
        <article>
            <h1>{% title %}</h1>
            <p class="meta">Published on {% date %}</p>
            {% content %}
        </article>
    </main>
    
    <footer>
        <p>&copy; 2023 My Static Site</p>
    </footer>
</body>
</html>
```

```bash build.sh
#!/bin/bash

# Static site build script
# This script converts Markdown files to HTML

echo "Building static site..."

# Create build directory if it doesn't exist
mkdir -p build

# Copy static assets
cp -r static/* build/

# Convert Markdown to HTML
for file in content/*.md; do
    if [ -f "$file" ]; then
        filename=$(basename "$file" .md)
        echo "Converting $filename.md..."
        # Simple conversion - in production use proper markdown processor
        pandoc "$file" -f markdown -t html -s -o "build/$filename.html"
    fi
done

# Handle index file specifically
if [ -f "content/index.md" ]; then
    pandoc "content/index.md" -f markdown -t html -s -o "build/index.html"
fi

echo "Build complete! Files are in the build/ directory."
```

```markdown DEPLOYMENT.md
# Deployment Guide

## Prerequisites

- Linux server (Ubuntu/Debian recommended)
- Web server (Apache or Nginx)
- Git
- Python (for build scripts)

## Initial Setup

1. **Install Web Server**
```bash
sudo apt update
sudo apt install apache2
# or
sudo apt install nginx
```

2. **Install Markdown Processing Tools**
```bash
sudo apt install pandoc
pip3 install markdown
```

3. **Set Up Project Directory**
```bash
mkdir /var/www/mysite
cd /var/www/mysite
git clone <your-repo> .
```

## Deployment Process

1. **Build the Site**
```bash
./build.sh
```

2. **Copy Files to Web Directory**
```bash
sudo cp -r build/* /var/www/html/
```

3. **Set Permissions**
```bash
sudo chown -R www-data:www-data /var/www/html/
sudo chmod -R 755 /var/www/html/
```

## Automated Deployment

### Using Git Hooks
1. Create a post-receive hook in your git repository
2. The hook runs the build script
3. Copies files to web directory

### Using Cron Jobs
1. Set up a cron job to run build script periodically
2. Deploy changes automatically

## Security Considerations

1. **File Permissions**
   - Set proper ownership for web directory
   - Restrict write access to web server

2. **Web Server Configuration**
   - Disable directory listing
   - Configure proper MIME types
   - Set up HTTPS with Let's Encrypt

## Monitoring

1. **Check Web Server Logs**
```bash
sudo tail -f /var/log/apache2/error.log
```

2. **Monitor Disk Space**
```bash
df -h
```

3. **Verify Site Accessibility**
```bash
curl -I http://yoursite.com
```