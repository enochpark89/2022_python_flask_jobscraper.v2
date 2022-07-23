# FindMeJobs.com

- FindMeJobs scrapes job information from stackoverflow.com and present them.

# Preview

URL: https://flask-jobscraper-2022.herokuapp.com/

Screenshot:
![FindMejobs screen](/img/FindMeJobs.p2.jpg)

# Stacks used

- Front-end: HTML, CSS, Bootstrap
- Back-end: Python, Flask, BeautifulSoup4
- Deploy: Heroku

# Frameworks/Libraries

- **Render_template**: allows HTML template rendering in Flask.
- **Redirect**: it returns a response object and redirects the user to another target location with specified status code.
- **BeautifulSoup**: a Python library for pulling data out of HTML and XML files. It works with your favorite parser to provide idiomatic ways of navigating, searching, and modifying the parse tree.

# Development Progress

1. Create a Flask app
2. Write a python script to scrape jobs.
3. Create routes ( /, `/<keyword>`)
4. Create HTML templates.
5. Create a form that takes in keywords from the user.
6. Form will request data to the `/<keyword>` route and it will initiate the script that scrapes jobs from stackoverflow.com.
7. Create a loading bar using a CSS/Javascript so that users would know that the script is running from the back-end.