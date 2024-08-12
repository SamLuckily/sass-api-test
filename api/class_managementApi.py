# -*- coding: utf-8 -*-
from api.BaseApi import BaseApi


class ClassManageApi(BaseApi):
    """
    班级管理
    """

    def add_class(self, name, teacher_uuids):
        """新增班级"""
        path = "backend/grade/add"
        data = {
            "name": name,
            "teacher_uuids": teacher_uuids
        }
        return self.send("post", path, json=data)

    def delete_class(self, uuid):
        """删除班级"""
        path = "backend/grade/delete"
        data = {
            "uuid": uuid
        }
        return self.send("post", path, json=data)

    def edit_class(self, uuid, name, teacher_uuids):
        """编辑班级"""
        path = "backend/grade/edit"
        data = {
            "uuid": uuid,
            "name": name,
            "teacher_uuids": teacher_uuids

        }
        return self.send("post", path, json=data)

    def class_list(self):
        """班级列表"""
        path = "backend/grade/list"
        return self.send("get", path)

    def class_course_name(self, uuid):
        """班级的课程名称列表"""
        path = "backend/grade/course-name"
        data = {
            "uuid": uuid
        }
        return self.send("get", path, params=data)

    def class_name_list(self):
        """班级名称列表"""
        path = "backend/grade/grade-name"
        return self.send("get", path)

    def unbound_classes_student(self):
        """获取当前机构中未绑定班级的学生"""
        path = "backend/grade/user-org-list"
        return self.send("get", path)

    def get_student_list_class(self, uuid):
        """获取班级下的学生列表"""
        path = "backend/grade/user-list"
        data = {
            "uuid": uuid
        }
        return self.send("get", path, params=data)

    def add_class_students(self, uuid, user_uuids):
        """添加班级学生"""
        path = "backend/grade/user-add"
        data = {
            "uuid": uuid,
            "user_uuids": user_uuids
        }
        return self.send("post", path, json=data)

    def del_class_student(self, uuid, user_uuid):
        """删除班级学生"""
        path = "backend/grade/user-delete"
        data = {
            "uuid": uuid,
            "user_uuid": user_uuid
        }
        return self.send("post", path, json=data)

    def edit_class_student(self, user_uuid, gender):
        """编辑班级学生"""
        path = "backend/grade/user-edit"
        data = {
            "user_uuid": user_uuid,
            "gender": gender
        }
        return self.send("post", path, json=data)

    def class_teacher_list(self, grade_uuid):
        """班级老师列表"""
        path = "backend/grade/teachers"
        data = {
            "grade_uuid": grade_uuid
        }
        return self.send("get", path, params=data)

    def class_disassociation_teacher(self, grade_uuid, teacher_uuid):
        """班级取消关联老师"""
        path = "backend/grade/unbind-teacher"
        data = {
            "grade_uuid": grade_uuid,
            "teacher_uuid": teacher_uuid
        }
        return self.send("post", path, json=data)
