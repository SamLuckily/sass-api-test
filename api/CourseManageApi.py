# -*- coding: utf-8 -*-
from api.BaseApi import BaseApi


class CourseManageApi(BaseApi):
    def course_add(self, name, teacher_uuid, publish, about):
        """新增课程"""
        path = "backend/course/add"
        data = {
            "name": name,
            "teacher_uuid": teacher_uuid,
            "publish": publish,
            "about": about,
        }
        return self.send("post", path, json=data)

    def course_listing_and_removal(self):
        pass

    def course_edit(self):
        pass

    def course_delete(self, uuid):
        """删除课程"""
        path = "backend/course/delete"
        data = {
            "uuid": uuid
        }
        return self.send("post", path, json=data)

    def course_list(self):
        pass

    def course_details(self):
        pass

    def get_teacher(self):
        pass

    def get_course_name_list(self):
        pass
