from locust import HttpLocust, TaskSet, task
import subprocess
import json

class UserBehavior(TaskSet):
    def on_start(self):
        pass

    @task(1)
    def list_header(self):
        r = self.client.get('url')
        if json.loads((r.content))['']!=100:
            r.failure("Got wrong response:"+r.content)
    @task(2)
    def list_goods(self):
        r = self.client.get('url')
        if json.loads((r.content))[''] !=100:
            r.failure("Got wrong response:" +r.content)
class WebUserLocust(HttpLocust):
    weight = 1
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 15000
class MobileUserLocust(HttpLocust):
    weight = 3
    task_set = UserBehavior
    min_wait = 3000
    max_wait = 6000
