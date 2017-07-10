from django.db import models


# 用户管理
class User(models.Model):
    username = models.CharField('账户', max_length=32, unique=True)
    password = models.CharField('密码', max_length=64)
    oldpwd = models.CharField('旧密码', max_length=64)

    class Meta:
        verbose_name_plural = '1-1用户账户表'

    def __str__(self):
        return '%s' % self.username


class UserInfo(models.Model):
    status_choice = ((0, '未激活'), (1, '正常'), (2, '锁定'))
    user = models.OneToOneField('User', related_name='账户信息')
    name = models.CharField('姓名', max_length=32, null=True)
    email = models.EmailField('邮箱', unique=True)
    phone = models.CharField('手机', max_length=11, unique=True)
    company = models.CharField('公司', max_length=128, null=True)
    department = models.CharField('部门', max_length=64, null=True)
    position = models.CharField('职位', max_length=64, null=True)
    status = models.SmallIntegerField('状态', choices=status_choice)
    creat_at = models.DateTimeField('创建时间', auto_now_add=True)
    last_at = models.DateTimeField('最后登录', auto_now_add=True)

    class Meta:
        verbose_name_plural = '1-2用户信息表'

    def __str__(self):
        return self.name


class Role(models.Model):
    name = models.CharField('角色名称', max_length=32)

    class Meta:
        verbose_name_plural = '1-3角色表'

    def __str__(self):
        return self.name


class Role2User(models.Model):
    user = models.ForeignKey('User')
    role = models.ForeignKey('Role')

    class Meta:
        verbose_name_plural = '1-4用户与角色表'
        unique_together = ('user', 'role')

    def __str__(self):
        return '%s-%s' % (self.user, self.role)


# 权限
class Action(models.Model):
    caption = models.CharField(max_length=32)
    code = models.CharField(max_length=32)

    class Meta:
        verbose_name_plural = '2-1权限操作表'
        unique_together = ('caption', 'code')

    def __str__(self):
        return self.caption


class AdminMenu(models.Model):
    caption = models.CharField(max_length=32)
    parent = models.ForeignKey('self', related_name='p', null=True, blank=True)

    def __str__(self):
        return "%s" % (self.caption,)

    class Meta:
        verbose_name_plural = '2-1菜单表'

        # 系统配置


# 轮播图
class Rotation(models.Model):
    name = models.CharField('名称', max_length=64)

    class Meta:
        verbose_name_plural = '8-轮播名称'

    def __str__(self):
        return '%s' % self.name


class Carousel(models.Model):
    weight = models.SmallIntegerField('权重', default=1)
    status = models.BooleanField('状态', default=0)
    orgid = models.ForeignKey('Rotation', verbose_name='所属')
    title = models.CharField('标题', max_length=64, null=True)
    content = models.TextField('文本', null=True)
    url = models.URLField('链接')
    img = models.ImageField('图片', upload_to='banner')

    class Meta:
        verbose_name_plural = '8-轮播图信息'

    def __str__(self):
        return '%s' % self.url


# 邮件管理
class Email(models.Model):
    mail_type_choices = ((0, 'SMTP'), (1, 'IMAP'))
    mail_type = models.SmallIntegerField('类型', choices=mail_type_choices, default=0)
    addr = models.CharField('地址', max_length=128)
    user = models.EmailField('邮件账户')
    password = models.CharField('邮件密码', max_length=64)
    port = models.IntegerField('端口', default=25)
    is_ssh = models.BooleanField('是否ssh', default=1)

    class Meta:
        verbose_name_plural = '8-邮件设置'

    def __str__(self):
        return '%s' % self.user


class EmailTemplate(models.Model):
    effect_choices = ((1, '用户注册'), (2, '找回密码'), (3, '企业会员'), (4, '其他模板'))
    effect = models.IntegerField('作用', choices=effect_choices)
    sendmail = models.ForeignKey('Email', verbose_name='发件箱')
    name = models.CharField('名称', max_length=32, unique=True)
    status = models.BooleanField('状态', default=0)
    content = models.TextField('内容')

    class Meta:
        verbose_name_plural = '8-邮件模板'

    def __str__(self):
        return '%s' % self.name


class Emaillog(models.Model):
    send_status = ((0, '发送成功'), (1, '发送失败'))
    title = models.CharField('标题', max_length=64)
    receive = models.EmailField('接收邮件')
    content = models.TextField('内容')
    issend = models.SmallIntegerField(choices=send_status)
    send_at = models.DateTimeField('创建时间', auto_now_add=True)

    class Meta:
        verbose_name_plural = '8-邮件日志'

    def __str__(self):
        return '%s' % self.title


# 活动配置
class Menu(models.Model):
    weight = models.SmallIntegerField('权重', default=1)
    status = models.BooleanField('状态', default=0)
    name = models.CharField('导航名称', max_length=32, unique=True)
    url = models.CharField('链接', max_length=128, null=True, blank=True)

    class Meta:
        verbose_name_plural = '8-导航设置'

    def __str__(self):
        return '%s' % self.name


# 活动类型
class ActivityClass(models.Model):
    menu = models.ForeignKey('Menu', verbose_name='所属菜单')
    alias = models.CharField('URL别名', max_length=32, unique=True)
    name = models.CharField('活动名称', max_length=64)
    content = models.TextField('活动介绍', null=True, default='正在整理中')

    class Meta:
        verbose_name_plural = '7-活动类型'

    def __str__(self):
        return '%s' % self.name


class Activity(models.Model):
    activityclass = models.ForeignKey('ActivityClass', verbose_name='活动类别')
    img = models.ImageField('图片', upload_to='activity', null=True)
    title = models.CharField('标题', max_length=128)
    summary = models.CharField('简介', max_length=255)
    content = models.TextField('内容', default='正在添加中')
    author = models.CharField('作者', max_length=64, default='admin')
    up = models.IntegerField('点击量', default=0, null=True)
    status = models.BooleanField('状态', default=0)
    create_at = models.DateField('创建时间', auto_now=True)

    class Meta:
        verbose_name_plural = '7-活动内容管理'

    def __str__(self):
        return '%s-%s' % (self.aclass, self.title)


# 新闻管理
class News(models.Model):
    title = models.CharField('标题', max_length=128)
    img = models.ImageField('首页展示图', upload_to='news', null=True, blank=True)
    content = models.TextField('内容', null=True)
    summary = models.CharField('摘要', max_length=255)
    author = models.CharField('作者', max_length=64, null=True, default='admin')
    up = models.IntegerField('点击量', null=True, default=0)
    creat_at = models.CharField('创建时间', max_length=32)
    status = models.BooleanField('状态', default=0)

    class Meta:
        verbose_name_plural = '5-新闻管理'

    def __str__(self):
        return '%s-%s' % (self.title, self.creat_at)


# 企业会员
class CompanyMember(models.Model):
    status_choices = ((0, '申请中'), (1, '已沟通'), (2, '垃圾信息'), (3, '有意向合作'), (4, '已展开合作'), (5, '未通过'))
    name = models.CharField('姓名', max_length=32)
    phone = models.CharField('电话', max_length=12)
    company = models.CharField('公司名称', max_length=128)
    position = models.CharField('职位', max_length=32)
    email = models.EmailField('邮箱')
    status = models.SmallIntegerField('状态', choices=status_choices, default=0)
    creat_at = models.DateTimeField('创建时间', auto_now_add=True)

    class Meta:
        verbose_name_plural = '6-企业会员咨询'

    def __str__(self):
        return '%s-%s' % (self.name, self.company)


class MemberFollow(models.Model):
    followay_choices = ((0, '电话'), (1, '邮箱'), (2, '线下沟通'))
    company = models.ForeignKey('CompanyMember', verbose_name='跟进企业')
    followay = models.SmallIntegerField('跟进方式', choices=followay_choices, default=0)
    contenet = models.TextField('跟进内容')
    creat_at = models.DateTimeField('创建时间', auto_now_add=True)

    class Meta:
        verbose_name_plural = '6-会员跟进信息'

    def __str__(self):
        return '%s-%s' % (self.company, self.company)
