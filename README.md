
**Animal Adoption Platform**

**Overview**

This project is an animal adoption platform developed using Python Django framework, HTML, CSS, and JavaScript. The database used is SQLite. The platform allows users to register, create accounts, browse animals available for adoption, apply for adoption, and for admins to manage users and pet information. 

Features

- User Registration: Users can register for an account on the platform.
- User Authentication: Users can log in to their accounts securely.
- Animal Browsing: Users can browse animals available for adoption.
- Filtering: Users can filter animals based on various factors such as type, area, and age.
- Animal Details: Users can view detailed information about a specific animal.
- Adoption Application: Users can apply for the adoption of a specific animal.
- Admin Panel: Admins have access to an admin panel for managing users and pet information.
- Application Management: Admins can view adoption applications, accept one, and inform other applicants about the decision.

Technologies Used

- Python Django: Backend framework for handling server-side logic.
- HTML: Markup language for creating the structure of web pages.
- CSS: Stylesheet language for styling HTML elements.
- JavaScript: Programming language for adding interactivity to web pages.
- SQLite: Database management system for storing application data.

Installation

1. Clone the repository:
    git clone https://github.com/WANJALAJNRIV/animal_adoption.git


2. Install dependencies:
    pip install -r requirements.txt


3. Run migrations:   
    python manage.py migrate

4. Create a superuser (admin):
    python manage.py createsuperuser

5. Start the development server:
    python manage.py runserver

6. Access the application in your web browser at `http://localhost:8000`.

Usage

1. Visit the homepage and register for an account if you're a new user.
2. Log in to your account.
3. Browse animals and filter them according to your preferences.
4. View detailed information about a specific animal.
5. Apply for the adoption of an animal.
6. Admins can access the admin panel at `http://localhost:8000/admin` to manage users and pet information.
7. Admins can view adoption applications, accept one, and inform other applicants about the decision.
