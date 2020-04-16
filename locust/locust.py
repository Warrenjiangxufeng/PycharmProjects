from  locusts import Httplocust , TaskSet, task

class WebsiteTasks(TaskSet):
    def on_start(self):
        self.client.post("/login", {"username": "tes_user", "password": ""})
    @task
    def index(self):
        self.client.get("/")
    @task
    def about(self):
        self.client.get("/about/")
class websiteUser(Httplocust):
    task_set = WebsiteTasks
    min_wait = 5000
    max_wait = 15000