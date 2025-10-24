# GitHub SSH Setup Guide for sabryyoussef

## SSH Key Information
- **Email**: vendorah2@gmail.com
- **Key Type**: ED25519
- **Key Location**: ~/.ssh/id_ed25519_github
- **Public Key**: 
```
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIKUKb2enEpwjimqqScG3kPwFJ0ew7xeTBZPZD7227Wf7 vendorah2@gmail.com
```

## Next Steps

### 1. Add SSH Key to GitHub
1. Copy the public key above
2. Go to GitHub.com → Settings → SSH and GPG keys
3. Click "New SSH key"
4. Paste the key and give it a name like "Ubuntu Development Machine"
5. Click "Add SSH key"

### 2. Test SSH Connection
```bash
ssh -T git@github.com
```

### 3. Repository URLs
Use these SSH URLs for your repositories:

#### Main Repositories
- **Motakamel Edafa**: `git@github.com:sabryyoussef/motakamel-edafa.git`
- **Hospital Management**: `git@github.com:sabryyoussef/hospital-mgt.git`
- **Cybro Addons**: `git@github.com:sabryyoussef/CybroAddons.git`

#### Academic System Project
- **Academic System**: `git@github.com:sabryyoussef/odoo-18-academic-system.git`

### 4. Clone Commands
```bash
# Clone academic system project
git clone git@github.com:sabryyoussef/odoo-18-academic-system.git

# Clone hospital management
git clone git@github.com:sabryyoussef/hospital-mgt.git

# Clone Cybro addons
git clone git@github.com:sabryyoussef/CybroAddons.git
```

### 5. SSH Config Shortcuts
The SSH config file includes shortcuts for easier repository management:

```bash
# Using shortcuts
git clone git@github-motakamel-edafa:sabryyoussef/motakamel-edafa.git
git clone git@github-hospital-mgt:sabryyoussef/hospital-mgt.git
git clone git@github-cybro-addons:sabryyoussef/CybroAddons.git
```

## Repository Management

### Current Repositories (from GitHub profile)
1. **hospital-mgt** - Odoo hospital management module
2. **CybroAddons** - Odoo addons collection
3. **odoo-18-academic-system** - New academic management system

### Planned Repositories
- **motakamel-edafa-base** - Base module for academic system
- **motakamel-edafa-lms** - Learning Management System
- **motakamel-edafa-student** - Student Management
- **motakamel-edafa-crm** - CRM extensions
- **motakamel-edafa-accounting** - Accounting & Finance
- **motakamel-edafa-hr** - HR & Payroll
- **motakamel-edafa-loyalty** - Loyalty & Gamification
- **motakamel-edafa-portal** - Web Portal
- **motakamel-edafa-integrations** - Payment & Messaging
- **motakamel-edafa-reports** - Reporting System

## Git Configuration
```bash
# Set up git user
git config --global user.name "sabryyoussef"
git config --global user.email "vendorah2@gmail.com"

# Set up default branch
git config --global init.defaultBranch main

# Set up push strategy
git config --global push.default simple
```

## Troubleshooting

### If SSH connection fails:
1. Check if key is added to GitHub
2. Test connection: `ssh -T git@github.com`
3. Check SSH agent: `ssh-add -l`
4. Restart SSH agent: `eval "$(ssh-agent -s)"`

### If repository access is denied:
1. Verify repository exists
2. Check if you have access to the repository
3. Ensure SSH key is added to your GitHub account

## Security Notes
- Keep your private key secure (`~/.ssh/id_ed25519_github`)
- Never share your private key
- Use different keys for different purposes if needed
- Regularly rotate SSH keys for security

## Development Workflow
1. Create feature branches for new development
2. Use conventional commit messages
3. Test before pushing to main branch
4. Use pull requests for code review
5. Keep repositories organized with clear documentation
