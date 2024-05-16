**Project Title: CSE Department Announcements Dashboard**

**Overview:**
- The CSE Department Announcements Dashboard project aims to enhance information dissemination within the Computer Science department through a centralized web platform.

**Problem Statement:**
- Traditional communication channels (notice boards, emails, informal channels) in the department lack efficiency, leading to information gaps and missed opportunities.
- Absence of a centralized, visually organized platform results in information overload, oversight of critical updates, and difficulties in accessing historical data.

**Solution:**
- Developed a comprehensive web dashboard using Django, HTML/CSS, SQLite3, and JavaScript.
- Django provided robust session management, user authentication, and ORM for database interactions.
- HTML/CSS created a visually appealing and well-structured interface, leveraging Bootstrap for responsiveness.
- SQLite3 served as the lightweight database engine for user data storage.
- JavaScript added dynamic functionality, enabling real-time updates and asynchronous form handling.

**Features:**
1. **Role-based Access:** Differentiates between student and teacher roles, providing tailored views.
2. **Announcements:** Displays important announcements in a visually organized manner.
3. **Notes:** Stores and presents course-related notes for easy access.
4. **Grades:** Provides a platform for viewing and tracking student grades.
5. **Interactive Interface:** Real-time updates and seamless navigation for enhanced user experience.

**How to Use:**
1. Clone the repository to your local machine.
2. Install required dependencies using `pip install -r requirements.txt`.
3. Configure database settings in `settings.py`.
4. Run the server using `python manage.py runserver`.
5. Access the dashboard through a web browser at `http://localhost:8000`.
