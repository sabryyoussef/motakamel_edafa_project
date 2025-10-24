#!/bin/bash

# Setup Git Repository for Motakamel Edafa Project
# Run this script after installing git

echo "🚀 Setting up Git repository for Motakamel Edafa Project..."

# Check if git is installed
if ! command -v git &> /dev/null; then
    echo "❌ Git is not installed. Please install git first:"
    echo "sudo apt update && sudo apt install git -y"
    exit 1
fi

# Initialize git repository
echo "📁 Initializing git repository..."
git init

# Configure git user
echo "👤 Configuring git user..."
git config user.name "sabryyoussef"
git config user.email "vendorah2@gmail.com"

# Set default branch to main
echo "🌿 Setting default branch to main..."
git config init.defaultBranch main

# Add all files
echo "📝 Adding files to repository..."
git add .

# Create initial commit
echo "💾 Creating initial commit..."
git commit -m "Initial commit: Odoo 18 Academic Management System

- Added comprehensive implementation plan (48 steps, 15 phases)
- Created SSH setup guide for GitHub
- Added project documentation and README
- Set up gitignore for Odoo development
- Included requirements document and project structure"

# Add remote origin
echo "🔗 Adding remote origin..."
git remote add origin git@github.com:sabryyoussef/motakamel_edafa_project.git

# Set upstream branch
echo "⬆️ Setting upstream branch..."
git branch -M main

echo "✅ Repository setup complete!"
echo ""
echo "📋 Next steps:"
echo "1. Add your SSH key to GitHub (if not already done)"
echo "2. Test SSH connection: ssh -T git@github.com"
echo "3. Push to GitHub: git push -u origin main"
echo ""
echo "🔑 Your SSH public key:"
cat ~/.ssh/id_ed25519_github.pub
echo ""
echo "📖 For detailed instructions, see: github-ssh-setup.md"
