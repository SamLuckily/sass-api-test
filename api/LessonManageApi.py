# -*- coding: utf-8 -*-
from api.BaseApi import BaseApi


class LessonManageApi(BaseApi):
    def lesson_add(self, name, course_uuid, chapter_uuid, view):
        """新增课时"""
        path = "backend/lesson/add"
        data = {
            "name": name,
            "course_uuid": course_uuid,
            "chapter_uuid": chapter_uuid,
            "view": view
        }
        return self.send("post", path, json=data)

    def lesson_edit(self, uuid, name):
        """课时编辑"""
        path = "backend/lesson/edit"
        data = {
            "uuid": uuid,
            "name": name
        }
        return self.send("post", path, json=data)

    def lesson_delete(self):
        pass

    def lesson_create_update_live(self):
        pass

    def stop_live_early(self):
        pass

    def lesson_sorting(self):
        pass

    def lesson_move_to(self):
        pass
