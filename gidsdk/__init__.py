import requests as r

class Login:
    def __init__(self, email="", token=""):
        if token != "":
            ld = r.post("https://id.gudupao.top/api/v1/user/info_user", data={"token": token})
            if ld.json():
                self.token = token
            else:
                raise Exception("TokenErr")
        self.email = email
        ld = r.post("https://id.gudupao.top/api/v1/user/login", data={"email": self.email,"code": ""})
        self.code = ld.json()["code"]
    
    def confirm(self):
        ld = r.post("https://id.gudupao.top/api/v1/user/login", data={"email": self.email,"code": self.code})
        if ld.json()["login"] == "ok":
            self.token = ld.json()["token"]
            return True
        return False