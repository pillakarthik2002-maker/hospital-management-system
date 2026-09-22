
# Hospital Management System

A web-based Hospital Management System developed using **Python and Django**.

This project provides a simple platform for managing hospital-related activities such as doctors, patients, appointments, health tips, health campaigns, job openings, reviews, and contact messages.

---

## About The Project

The Hospital Management System is a Django-based web application developed to practice and demonstrate the fundamentals of web application development using Python and Django.

The application provides different modules for doctors and patients and allows hospital-related information to be added, viewed, updated, and managed through the system.

The project uses **SQLite3** as the database and Django's built-in features for handling models, forms, templates, authentication, and administration.

---

## Features

### Doctor Management

- Add doctor details
- View doctor details
- Update doctor information
- Doctor login
- Doctor dashboard
- Doctor profile information

### Patient Management

- Patient information
- Patient appointment functionality
- Patient reviews and feedback
- Patient-related pages

### Appointment Management

- Add appointments
- View appointments
- Manage appointment information
- Appointment-related pages

### Calendar Management

- Add calendar events
- View calendar information
- Manage calendar details

### Health Tips

- Add health tips
- View health tips
- Manage health-related information

### Health Campaigns

- Add health campaigns
- View health campaigns
- Update health campaign information
- Display campaign information

### Job Openings

- Add hospital job openings
- View available job openings
- Manage job information

### Reviews and Feedback

- Patients can submit reviews
- View patient feedback
- Manage review information

### Contact Management

- Contact form
- Submit contact messages
- View contact information
- Manage contact messages

### Django Admin

- Built-in Django Admin panel
- Manage application data
- Manage doctors
- Manage appointments
- Manage health information
- Manage other application records

---

## Technologies Used

- **Python**
- **Django**
- **HTML5**
- **CSS3**
- **SQLite3**
- **Django Templates**
- **Git**
- **GitHub**

---

## Project Structure

```text
hospital-management-system/
│
├── hospitalapp/
│   ├── migrations/
│   │   ├── 0001_initial.py
│   │   ├── 0002_contact.py
│   │   ├── 0003_contact_message.py
│   │   ├── 0004_alter_calendar_title_alter_healthcampaign_content_and_more.py
│   │   ├── 0005_doctor_password_doctor_username.py
│   │   └── __init__.py
│   │
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
│
├── hospitalpro/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── static/
│   ├── css/
│   │   └── styles.css
│   │
│   └── images/
│       ├── logo.png
│       └── mainbanner.png
│
├── templates/
│   ├── add_appointment.html
│   ├── add_calendar.html
│   ├── add_doctor.html
│   ├── contact.html
│   ├── contact_thanks.html
│   ├── contactdata.html
│   ├── doctor.html
│   ├── doctor_dashboard.html
│   ├── doctor_login.html
│   ├── form.html
│   ├── health_campaign.html
│   ├── health_campaign_data.html
│   ├── health_tips.html
│   ├── health_tips_data_view.html
│   ├── home.html
│   ├── job_open.html
│   ├── job_open_data.html
│   ├── myapp.html
│   ├── patient.html
│   ├── profiledata.html
│   ├── registration/
│   │   └── login.html
│   ├── revie.html
│   ├── reviewdata.html
│   ├── thanks.html
│   ├── thankspage.html
│   ├── update_doctor.html
│   ├── update_health_campaign.html
│   ├── v_calendar.html
│   ├── v_campaign.html
│   ├── v_doctors.html
│   ├── v_job.html
│   ├── v_tips.html
│   ├── view_appointments.html
│   ├── view_calendar.html
│   └── view_doctors.html
│
├── .gitignore
├── manage.py
└── README.md
````

---

## Requirements

Before running the project, make sure the following are installed:

* Python 3.x
* Django
* Git

---

## Installation and Setup

### Step 1: Clone the Repository

```bash
git clone https://github.com/pillakarthik2002-maker/hospital-management-system.git
```

### Step 2: Open the Project Folder

```bash
cd hospital-management-system
```

### Step 3: Create a Virtual Environment

```bash
python -m venv venv
```

### Step 4: Activate the Virtual Environment

For Windows:

```bash
venv\Scripts\activate
```

For macOS/Linux:

```bash
source venv/bin/activate
```

### Step 5: Install Django

```bash
pip install django
```

### Step 6: Apply Migrations

```bash
python manage.py migrate
```

### Step 7: Run the Development Server

```bash
python manage.py runserver
```

### Step 8: Open the Application

Open your browser and visit:

```text
http://127.0.0.1:8000/
```

---

## Django Admin Panel

This project uses Django's built-in Admin Panel to manage application data.

Create a superuser:

```bash
python manage.py createsuperuser
```

Enter the requested username, email, and password.

Then start the development server:

```bash
python manage.py runserver
```

Open the Django Admin Panel:

```text
http://127.0.0.1:8000/admin/
```

Log in using your superuser credentials.

---

## Database

The project uses **SQLite3** as its database.

Django migrations are used to create and update the database structure.

To create migrations:

```bash
python manage.py makemigrations
```

To apply migrations:

```bash
python manage.py migrate
```

---

## Main Django Components

### Models

Django models are used to define and store hospital-related data.

### Views

Views contain the application logic and handle requests and responses.

### Forms

Django forms are used to collect and validate user input.

### Templates

HTML templates are used to create the user interface.

### URLs

Django URL routing connects application URLs with their corresponding views.

### Static Files

CSS and image files are stored inside the `static` directory.

### Migrations

Django migrations are used to manage changes to the database structure.

---

## Application Modules

The project contains several hospital-related modules.

### Doctor Module

The doctor module provides functionality for managing doctor information, doctor login, doctor dashboard, and doctor profiles.

### Patient Module

The patient module provides pages and functionality related to patients and their appointments.

### Appointment Module

The appointment module allows appointment information to be added and viewed.

### Calendar Module

The calendar module provides functionality for adding and viewing hospital calendar information.

### Health Tips Module

The health tips module allows health-related tips to be managed and displayed.

### Health Campaign Module

The health campaign module allows hospital health campaigns to be created, updated, and displayed.

### Job Opening Module

The job opening module allows hospital job opportunities to be added and displayed.

### Review Module

The review module allows patients to submit feedback and reviews.

### Contact Module

The contact module allows users to submit messages through a contact form.

---

## What I Learned From This Project

This project helped me gain practical experience with:

* Python programming
* Django framework
* Django project structure
* Django applications
* Django models
* Django views
* Django forms
* URL routing
* Django templates
* Template rendering
* SQLite database
* Database migrations
* CRUD operations
* Django Admin
* Authentication
* Static files
* HTML
* CSS
* Git
* GitHub

---

## Future Enhancements

The project can be further improved by adding:

* Online doctor appointment scheduling
* Doctor availability management
* Email notifications
* Online payment integration
* Patient medical history
* Prescription management
* Medical report management
* Advanced authentication
* Role-based access control
* Improved responsive design
* Search and filtering functionality

---

## Author

**Pilla Karthik**

MCA Graduate | Python & Django Learner

### GitHub

[https://github.com/pillakarthik2002-maker](https://github.com/pillakarthik2002-maker)

---

## Project Repository

[https://github.com/pillakarthik2002-maker/hospital-management-system](https://github.com/pillakarthik2002-maker/hospital-management-system)

---

## License

This project is created for educational and learning purposes.

````

### Update it on GitHub

Since your project is **already pushed**, after replacing the README run:

```bash
git add README.md
````

Then:

```bash
git commit -m "Update Hospital Management System README"
```

Finally:

```bash
git push
```

After that, refresh your GitHub repository and the complete README will be displayed.
