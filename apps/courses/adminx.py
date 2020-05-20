import xadmin
from apps.courses.models import Course,CourseResource,Lesson,Video

class CourseAdmin(object):
    list_display = ['id']
    pass
class CourseResourceAdmin(object):
    pass
class LessonAdmin(object):
    pass
class VideoAdmin(object):
    pass
xadmin.site.register(Course,CourseAdmin)
xadmin.site.register(CourseResource,CourseResourceAdmin)
xadmin.site.register(Lesson,LessonAdmin)
xadmin.site.register(Video,VideoAdmin)