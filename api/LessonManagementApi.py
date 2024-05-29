# -*- coding: utf-8 -*-
from api.BaseApi import BaseApi


class LessonManagementApi(BaseApi):
    def lesson_add(self, name, course_uuid, chapter_uuid, view):
        path = "backend/lesson/add"
        data = {
            "name": name,
            "course_uuid": course_uuid,
            "chapter_uuid": chapter_uuid,
            "view": view,
        }
        return self.send("post", path, json=data)

    def lesson_edit(self):
        pass

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
