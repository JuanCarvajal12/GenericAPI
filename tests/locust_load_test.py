from email import header
from locust import HttpUser, TaskSet, task
from utils.const import APP_HOST, APP_PORT, TESTING
from tests.all_test import insert_user, clear_db


class GenericapiLocustTask(TaskSet):
    #

    # @task
    # def token_test(self):
    #     #
    #     test_user = {
    #     "username": "test_user",
    #     "password": "test_pass"
    #     }
    #     response = self.client.post("/token", test_user)
    #     my_token = response["access_token"]
    #     return my_token


    @task
    def test_post_user(self):
        user_dict = {
            "name": "personel1",
            "password": "pass1",
            "mail": "sample@mail.dom",
            "role": "admin"
        }
        # my_token = self.token_test()
        my_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ0ZXN0X3VzZXIiLCJyb2xlIjoiYWRtaW4iLCJleHAiOjE2NDQyNjgxNzF9.iYtes3TxT-h--W_ApSZ8SHDNU5pWpmz67zqBQ-8Lw7U"
        auth_header = {"Authorization": f"Bearer {my_token}"}
        self.client.post("/v2/user", json=user_dict,
            headers=auth_header)

class GenericapiLoadTest(HttpUser):
    #
    tasks = [GenericapiLocustTask]
    host = f"http://{APP_HOST}:{APP_PORT}"