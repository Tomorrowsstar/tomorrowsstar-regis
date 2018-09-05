from django.db import models
from django.core import validators


class Item(models.Model):

    SEX_CHOICES = (
        (1, '男性'),
        (2, '女性'),
    )

    SCHOOL_CHOICES = (
        (1, '保良局梁周順琴小學'),
        (2, '湖景青松小學'),
    )

    name = models.CharField(
        verbose_name='姓名',
        max_length=200,
    )
    sex = models.IntegerField(
        verbose_name='性別',
        choices=SEX_CHOICES,
        default=1
    )
    school = models.IntegerField(
        verbose_name='學校',
        choices=SCHOOL_CHOICES,
        default=1
    )
    memo = models.TextField(
        verbose_name='備考',
        max_length=300,
        blank=True
    )
    created_at = models.DateTimeField(
        verbose_name='登録日期',
        auto_now_add=True
    )

    # 管理サイト上の表示設定
    def __str__(self):
        return self.name
        
    class Meta:
        verbose_name = '登記'
        verbose_name_plural = '登記'