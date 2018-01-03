 # -*- coding: utf-8 -*- 

from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

class Post(models.Model):
    title = models.CharField('TITLE', max_length=50)
    slug = models.SlugField('SLUG', unique=True, allow_unicode=True, help_text='one word for title alias')
    description = models.CharField('DESCRIPTION', max_length=100, blank=True, help_text='simple description text')
    content = models.TextField('CONTENT')
    create_date = models.DateTimeField('Create Date', auto_now_add=True)
    modify_date = models.DateTimeField('modify_date', auto_now=True)
    owner = models.ForeignKey(User, null=True)

    class Meta:
        verbose_name = 'post' #테이블의 별칭을 단수와 복수로 가질 수 있는데, 단수 별칭을 post로
        verbose_name_plural = 'post_list' #복수의 별칭을 posts로
        db_table = 'my_post'
        ordering = ('-modify_date',) #모델 객체의 리스트 출력시 modify_date 컬러을 기준으로 내림차순 정렬

    def __str__(self):
        return self.title

    def get_absolute_url(self): #이 매소드가 정의된 객체를 지칭하는 url을 반환
        return reverse('blog:post_detail', args=(self.slug,)) #매소드 내에서는 장고의 내장함수인 reverse() 호출

    def get_previous_post(self): #modify_date 컬럼을 기준으로 이전 포스트 반환
        return self.get_previous_by_modify_date()

    def get_next_post(self): #modify_date 컬럼을 기준으로 다음 포스트 반환
        return self.get_next_by_modify_date()

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title, allow_unicode=True) #처음으로 저장하는 경우에만 slug 필드를 title 필드의 단어로 변환해 자동으로 저장
        super(Post, self).save(*args, **kwargs)

    def approved_comments(self):
    return self.comments.filter(approved_comment=True)

class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
# Create your models here.
