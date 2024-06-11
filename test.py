# -*- coding: utf-8 -*-
import jsonpath
import pytest
import requests


class TestLogin:
    def setup_class(self):
        headers = {"Content-Type": "application/json"}
        data = {
            "login_type": "username",
            "username": "15830344885",
            "password": "admin123"
        }
        url = "http://api.boweiedu.test/v1/user/login"
        # url = "http://192.168.0.210/v1/user/login"
        r = requests.request("POST", url, headers=headers, json=data)
        self.token = jsonpath.jsonpath(r.json(), "$..token")[0]
        self.uuid = jsonpath.jsonpath(r.json(), "$..user_base.uuid")[0]

    def test_resource_list(self):
        """资源列表"""
        headers = {"Content-Type": "application/json", "Authorization": "Bearer " + self.token}
        url = "http://api.boweiedu.test/backend/resource/list"
        r = requests.request("GET", url, headers=headers)
        assert r.json()["code"] == 0

    """资源绑定"""

    @pytest.mark.parametrize("name, publish, about, title, name_lesson,expect",
                             [["课程002", "publish", "课程介绍", "第一章节", "第一课时", 0]])
    def test_resource_binding(self, name, publish, about, title, name_lesson, expect):
        """
        1.创建课程
        2.创建章节
        3.创建课时
        4.上传资源
        5.资源绑定
        6.删除课程
        :return:
        """
        headers = {"Content-Type": "application/json", "Authorization": "Bearer " + self.token}
        create_course_url = "http://api.boweiedu.test/backend/course/add"
        create_course_data = {
            "name": name,
            "teacher_uuid": self.uuid,
            "publish": publish,
            "about": about
        }
        r = requests.request("POST", create_course_url, headers=headers, json=create_course_data)
        course_uuid = jsonpath.jsonpath(r.json(), "$..uuid")[0]
        create_chapter_url = "http://api.boweiedu.test/backend/chapter/add"
        create_chapter_data = {
            "title": title,
            "course_uuid": course_uuid
        }
        r = requests.request("POST", create_chapter_url, headers=headers, json=create_chapter_data)
        chapter_uuid = jsonpath.jsonpath(r.json(), "$..uuid")[0]
        create_lesson_url = "http://api.boweiedu.test/backend/lesson/add"
        create_lesson_data = {
            "name": name_lesson,
            "course_uuid": course_uuid,
            "chapter_uuid": chapter_uuid,
            "view": 10
        }
        r = requests.request("POST", create_lesson_url, headers=headers, json=create_lesson_data)
        lesson_uuid = jsonpath.jsonpath(r.json(), "$..uuid")[0]
        headers_up = {"Authorization": "Bearer " + self.token}
        upload_file_url = "http://api.boweiedu.test/comm/upload"
        files = {
            "upload-file": ("dog.jpeg",
                            open(r"E:\python_project\own_project\web_ui\sass_apiauto\files\dog.jpeg", "rb"),
                            "application/octet-stream",
                            )
        }
        res = requests.request("POST", upload_file_url, headers=headers_up, files=files)
        file_uuid = jsonpath.jsonpath(res.json(), "$..uuid")[0]
        resource_binding_url = "http://api.boweiedu.test/backend/resource/bind"
        resource_binding_data = {
            "target_type": "course_lesson",
            "target_uuid": lesson_uuid,
            "uuid": file_uuid
        }
        r = requests.request("POST", resource_binding_url, headers=headers, json=resource_binding_data)
        delete_course_url = "http://api.boweiedu.test/backend/course/delete"
        delete_data = {
            "uuid": course_uuid
        }
        r = requests.request("POST", delete_course_url, headers=headers, json=delete_data)
        assert r.json()["code"] == expect
