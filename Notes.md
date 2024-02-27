1. Project Structure
    1. settings.py
        1. Don't share this file when your project is online - it can be used for attacks
2. Apps
    1. python manage.py startapp generator
        1. Creates generator folder in project for generator app
3. https://www.pythonanywhere.com/user/TedRose/consoles/32506785/
    - `~/Django_course/personal_portfolio-project (main)$ mkvirtualenv portfoliovenv --python=/usr/bin/python3.10`
        - `~/Django_course/personal_portfolio-project (main)$ workon portfoliovenv`
        - `pip install django pillow`
        - Go to the Web tab, and in the Virtualenv section, enter the path: `/home/TedRose/.virtualenvs/portfoliovenv`
    - `python manage.py collectstatic`
        - Add this under "Static files" in Web tab:
            - `/static/`	`/home/TedRose/Django_course/personal_portfolio-project/static`
        - Add this under "Static files" in Web tab:
            - `/media/`	`/home/TedRose/Django_course/personal_portfolio-project/media`
