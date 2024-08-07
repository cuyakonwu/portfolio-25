import unittest
import os
from app import TimelinePost
os.environ["TESTING"] = 'true'

from app import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.client=app.test_client()
        TimelinePost.delete().execute()

    def test_home(self):
        response = self.client.get("/")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "<title>Conrad's Portfolio - Home</title>" in html
        assert '<a class="navbar-brand" href="/">Conrad Uyakonwu</a>' in html

        #testing navbar links
        assert '<a class="nav-link active" href="/">Home</a>' in html
        assert not '<a class="nav-link active" href="/about">About</a>' in html
        assert not '<a class="nav-link active" href="/experience">Experience</a>' in html
        assert not '<a class="nav-link active" href="/hobbies">Hobbies</a>' in html
        assert not '<a class="nav-link active" href="/map">World Map</a>'in html

        #testing index.html page links for homepage
        assert '<a href="https://github.com/cuyakonwu"><img class="landing-pics" src="/static/img/github-logo.png" alt="github logo">' in html
        assert '<a href="https://www.linkedin.com/in/conrad-uyakonwu/"><img src="/static/img/linkedin-logo.png" class="landing-pics" alt="linkedin logo"></a>' in html
        assert '<a href="mailto:conraduyakonwu@gmail.com"><img class="landing-pics" src="/static/img/envelope.png" alt="email"></a>' in html
        assert '<a href="https://docs.google.com/document/d/1D1xJ0MXw-0z4y0GzIXNdV04OOrKifBNIKJgo4cbvKoI/edit?usp=sharing" id="resume-link"><img class="landing-pics" src="/static/img/text-file.png" alt="Resume"></a>' in html

    def test_timeline_post(self):
        response = self.client.get("/api/timeline_post")
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert "timeline_posts" in json
        assert len(json["timeline_posts"]) == 0

        demo_post_data={
            "name":"Jane Doe",
            "email":"jane@example.com",
            "content":"Lorem ipsum dolor sit amet..."
        }

        #testing timeline POST api endpoint
        response_post = self.client.post("/api/timeline_post", data=demo_post_data)
        assert response_post.status_code == 200
        assert response_post.is_json
        json_response = response_post.get_json()
        assert json_response["name"] == demo_post_data["name"]
        assert json_response["email"] == demo_post_data["email"]
        assert json_response["content"] == demo_post_data["content"]

        #testing if the data has been received
        response_get = self.client.get("/api/timeline_post")
        assert response_get.status_code == 200
        assert response_get.is_json
        json_get_response = response_get.get_json()
        assert json_get_response['timeline_posts'][0]['name'] == demo_post_data['name']
        assert json_get_response['timeline_posts'][0]['email'] == demo_post_data['email']
        assert json_get_response['timeline_posts'][0]['content'] == demo_post_data['content']

    def test_timeline(self):
        #testing timeline page
        response = self.client.get("/timeline")
        assert response.status_code==200
        html = response.get_data(as_text=True)
        assert '<input type="text" class="form-control" id="name" name="name" required>' in html
        assert '<button type="submit" class="btn btn-primary">Submit</button>' in html
        assert '<div id="timeline-posts"></div>' in html

    def test_malformed_timeline_post(self):
        response = self.client.post("/api/timeline_post", data={"email": "john@example.com", "content":"Hello World, I\'m John!"})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid name" in html

        response = self.client.post("/api/timeline_post", data={"name":"John Doe", "email":"john@example.com", "content":""})
        assert response.status_code==400
        html = response.get_data(as_text=True)
        assert "Invalid content" in html

        response = self.client.post("/api/timeline_post", data={"name":"John Doe", "email":"not-an-email", "content":"Hello World, I\'m John!"})
        assert response.status_code==400
        html = response.get_data(as_text=True)
        assert "Invalid email" in html