from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import User

# Create your models here.
class UserChat(models.Model):
    user_id = models.ForeignKey(User, verbose_name=_("유저 아이디"), on_delete=models.CASCADE)
    question = models.DateField(_("최근 질문 날짜"), auto_now_add=True)
    today_quiz = models.PositiveSmallIntegerField(_("질문한 횟수"), default=5)
