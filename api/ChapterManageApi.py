# -*- coding: utf-8 -*-
from api.BaseApi import BaseApi


class ChapterManageApi(BaseApi):
    def chapter_add(self, title, course_uuid):
        path = "backend/chapter/add"
        data = {
            "title": title,
            "course_uuid": course_uuid
        }
        return self.send("post", path, json=data)

    def chapter_edit(self, title, uuid):
        path = "backend/chapter/edit"
        data = {
            "title": title,
            "uuid": uuid
        }
        return self.send("post", path, json=data)

    def chapter_delete(self):
        pass

    def chapter_list(self):
        pass

    def chapter_sorting(self):
        pass
