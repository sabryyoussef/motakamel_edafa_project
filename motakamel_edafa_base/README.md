# Motakamel Edafa Academic System - Base Module

## Overview
This is the base module for the Motakamel Edafa Academic Management System built on Odoo 18. It provides the foundation for all other academic system modules.

## Features
- **Security Groups**: Comprehensive role-based access control
- **Base Models**: Abstract models for common academic functionality
- **Configuration Management**: System-wide academic settings
- **Portal Integration**: Student and instructor portal interfaces
- **Responsive Design**: Mobile-friendly interface
- **Multi-language Support**: Arabic and English support

## Module Structure
```
motakamel_edafa_base/
├── __init__.py
├── __manifest__.py
├── models/
│   ├── __init__.py
│   └── base_models.py
├── controllers/
│   ├── __init__.py
│   └── main.py
├── security/
│   ├── ir.model.access.csv
│   └── security_groups.xml
├── data/
│   └── ir_sequence_data.xml
├── demo/
│   └── demo_data.xml
├── static/
│   ├── src/
│   │   ├── css/
│   │   │   ├── base.css
│   │   │   └── portal.css
│   │   ├── js/
│   │   │   └── base.js
│   │   └── xml/
│   │       └── academic_templates.xml
│   └── description/
└── README.md
```

## Security Groups
- **Academic System Administrator**: Full system access
- **Academic Manager**: Academic operations management
- **Academic User**: Basic system access
- **Student**: Student portal access
- **Instructor**: Instructor portal access
- **Content Manager**: Content management access
- **Financial Manager**: Financial operations access
- **HR Manager**: Human resources management

## Installation
1. Place the module in your Odoo addons directory
2. Update the app list in Odoo
3. Install the module from the Apps menu
4. Configure the academic system settings

## Configuration
After installation, configure the system through:
- Academic System Configuration (academic.config)
- Security groups assignment
- User role configuration

## Dependencies
- base
- web
- portal
- website

## Version
18.0.1.0.0

## License
LGPL-3

## Author
Motakamel Edafa

## Website
https://www.motakamel-edafa.com
