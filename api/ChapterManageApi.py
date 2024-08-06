# -*- coding: utf-8 -*-
from api.BaseApi import BaseApi


class ChapterManageApi(BaseApi):
    """
    章节管理
    """
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

    def chapter_delete(self, uuid):
        path = "/backend/chapter/delete"
        data = {
            "uuid": uuid
        }
        return self.send("post", path, json=data)

    def chapter_list(self, course_uuid):
        path = "/backend/chapter/list"
        data = {
            "course_uuid": course_uuid
        }
        return self.send("get", path, params=data)

    def chapter_sorting(self, sort, uuid, course_uuid):
        path = "/backend/chapter/sort"
        data = {
            "sort": sort,
            "uuid": uuid,
            "course_uuid": course_uuid
        }
        return self.send("post", path, json=data)
