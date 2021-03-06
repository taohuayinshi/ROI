#!/usr/bin/env Python
# coding=utf-8

import tornado.web
import methods.readdb as mrd

class LoginHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("login.html")

    def post(self):
        username = self.get_argument("name")
        password = self.get_argument("password")
        user_infos = mrd.select_table(table="users",column="*",condition="username",value=username)
        if user_infos:
            db_pwd = user_infos[0][2]
            if db_pwd == password:
                self.write("welcome")
            else: 
                self.write("password error")
        else:
            self.write("user error")
        
