import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', title="Conrad's Portfolio", url=os.getenv("URL"))

@app.route('/experience')
def experience():
    title = "Conrad Uyakonwu's Portfolio"
    work_experiences = [
        {
            "title": "System Administrator and Technical Support",
            "company": "Computer Science Instructional Lab (CSIL)",

            "description": "As part of my role, I conducted a mini-course on AI \
             and data science, educating patrons on various methodologies. I \
             spearheaded a CSIL-wide wiki audit, ensuring the accuracy and \
             relevance of documentation, which resulted in streamlined access \
             to critical information for all users. Additionally, I coordinated \
             with the education instruction team to organize and facilitate \
             inter-departmental courses, significantly enhancing the overall \
             technical proficiency of CSIL staff.",

            "duration": "March 2024 - Present"
        },
        {
            "title": "WIP",
            "company": "Major League Hacking",
            "description": "WIP",
            "duration": "June 2024 - September 2024"
        },
        {

        }
    ]

    education = [
        {
            "degree": "Bachelor's in Computer Science",
            "institution": "University of Chicago",
            "description": "Specialized in Machine Learning",
            "year": "Expected 2026"
        }
    ]
    return render_template('experience.html', title=title, work_experiences=work_experiences, education=education,)

@app.route('/about')
def about():
    hobbies = [
        "Playing the piano",
        "Hiking",
        "Reading science fiction novels"
    ]
    return render_template('about.html', title=title, hobbies=hobbies)
