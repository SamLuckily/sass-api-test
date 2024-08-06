# -*- coding: utf-8 -*-
from api.BaseApi import BaseApi


class CourseManageApi(BaseApi):
    """
    课程管理
    """
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

    def course_on_and_off(self, uuid, status):
        """课程上下架"""
        path = "backend/course/update-status"
        data = {
            "uuid": uuid,
            "status": status
        }
        return self.send("post", path, json=data)

    def course_edit(self, uuid, name):
        """课程编辑"""
        path = "backend/course/edit"
        data = {
            "uuid": uuid,
            "name": name
        }
        return self.send("post", path, json=data)

    def course_delete(self, uuid):
        """删除课程"""
        path = "backend/course/delete"
        data = {
            "uuid": uuid
        }
        return self.send("post", path, json=data)

    def course_list(self):
        """课程列表"""
        path = "backend/course/list"
        return self.send("get", path)

    def course_details(self, uuid):
        """课程详情"""
        path = "backend/course/detail"
        data = {
            "uuid": uuid
        }
        return self.send("get", path, params=data)

    def get_teacher(self):
        """获取教师接口"""
        path = "backend/user/teacher-list"
        return self.send("get", path)

    def get_course_name_list(self):
        """课程名称列表"""
        path = "backend/course/list-name"
        return self.send("get", path)
