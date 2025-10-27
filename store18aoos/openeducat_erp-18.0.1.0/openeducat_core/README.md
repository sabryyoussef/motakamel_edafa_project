# OpenEduCat Core Module

## Overview
The OpenEduCat Core module is the foundational module of the OpenEduCat ERP system. It provides the essential functionality for managing students, faculties, courses, and educational institutions. This module serves as the base for all other OpenEduCat modules and contains the core data models and business logic.

## Version
- **Version**: 18.0.1.0
- **License**: LGPL-3
- **Category**: Education
- **Sequence**: 1 (Base module)

## Dependencies
- `board` - Dashboard functionality
- `hr` - Human Resources management
- `web` - Web framework
- `website` - Website functionality

## Key Features

### 1. Student Management
- **Student Registration**: Complete student profile management with personal details, contact information, and academic records
- **Student Course Enrollment**: Track student enrollment in courses, batches, and subjects
- **Academic Progress**: Monitor student academic years, terms, and course completion status
- **Student Portal**: Web-based portal for students to access their information

### 2. Faculty Management
- **Faculty Profiles**: Comprehensive faculty information management
- **Employee Integration**: Link faculty with HR employee records
- **User Account Creation**: Automatic user account creation for faculty members
- **Subject Assignment**: Assign subjects and courses to faculty members

### 3. Course & Academic Management
- **Course Management**: Create and manage academic courses
- **Batch Management**: Organize students into batches for better management
- **Subject Management**: Define subjects and their relationships to courses
- **Academic Year/Term**: Manage academic calendars and terms
- **Program Management**: Define academic programs and levels

### 4. Institution Management
- **Company Configuration**: Educational institution setup and configuration
- **Department Management**: Organize academic and administrative departments
- **Category Management**: Classify students, faculty, and other entities

### 5. Reporting & Documentation
- **Student Bonafide Certificates**: Generate official student certificates
- **Student ID Cards**: Create student identification cards
- **Academic Reports**: Various academic and administrative reports

## Data Models

### Core Models
- `op.student` - Student information
- `op.faculty` - Faculty information
- `op.course` - Course details
- `op.batch` - Student batches
- `op.subject` - Subject information
- `op.department` - Department management
- `op.category` - Category classification
- `op.program` - Academic programs
- `op.program.level` - Program levels
- `op.academic.year` - Academic years
- `op.academic.term` - Academic terms
- `op.student.course` - Student-course relationships

## Workflow

### Student Enrollment Workflow
1. **Student Registration**
   - Create student profile with personal details
   - Assign unique student ID
   - Set up contact information and emergency contacts

2. **Course Enrollment**
   - Select academic program and course
   - Assign to appropriate batch
   - Generate roll number
   - Set academic year and term

3. **Subject Registration**
   - Register for required subjects
   - Track subject completion status
   - Monitor academic progress

### Faculty Management Workflow
1. **Faculty Registration**
   - Create faculty profile
   - Link with HR employee record
   - Create user account for system access

2. **Subject Assignment**
   - Assign subjects to faculty
   - Set teaching responsibilities
   - Track faculty workload

### Academic Management Workflow
1. **Academic Year Setup**
   - Define academic calendar
   - Set start and end dates
   - Configure terms and semesters

2. **Course Configuration**
   - Define course structure
   - Set prerequisites and requirements
   - Configure assessment methods

## Security & Access Control
- Role-based access control for different user types
- Student portal access with limited permissions
- Faculty access to assigned courses and students
- Administrative access for full system management

## Integration Points
- **HR Module**: Faculty-employee integration
- **Website Module**: Student and faculty portals
- **Board Module**: Dashboard functionality
- **Mail System**: Communication and notifications

## Configuration
- Company settings for educational institution
- Academic year and term configuration
- Student and faculty category setup
- Portal access configuration

## Reports Available
- Student Bonafide Certificate
- Student ID Card
- Academic Progress Reports
- Faculty Assignment Reports
- Course Enrollment Reports

## Technical Specifications
- Built on Odoo 18.0 framework
- Uses PostgreSQL database
- Responsive web interface
- RESTful API support
- Multi-language support

## Installation Requirements
- Odoo 18.0 or higher
- PostgreSQL database
- Python 3.8+
- Required Odoo modules: board, hr, web, website

## Usage Guidelines
1. **Initial Setup**: Configure company information and academic calendar
2. **Department Setup**: Create academic and administrative departments
3. **Program Configuration**: Define academic programs and levels
4. **Course Creation**: Set up courses and subjects
5. **Faculty Registration**: Add faculty members and assign subjects
6. **Student Enrollment**: Register students and enroll in courses

## Best Practices
- Maintain consistent naming conventions for courses and subjects
- Regular backup of student and academic data
- Proper user role assignment for security
- Regular academic year and term updates
- Consistent batch management for better organization

## Troubleshooting
- **Student Portal Issues**: Check user account creation and portal access settings
- **Course Enrollment Problems**: Verify academic year and term configuration
- **Faculty Access Issues**: Ensure proper HR integration and user account setup
- **Report Generation**: Check data completeness and report configuration

## Support & Documentation
- Official OpenEduCat documentation
- Community forums and support
- Technical documentation for developers
- User guides and tutorials

## Future Enhancements
- Enhanced student portal features
- Advanced reporting capabilities
- Mobile application support
- Integration with external systems
- AI-powered academic analytics
