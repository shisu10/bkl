from tortoise import Model, fields

class User(Model):
    username = fields.CharField(null=True, max_length=20, description="用户名")
    type = fields.BooleanField(default=False, description="用户类型 True:超级管理员 False:普通管理员")
    password = fields.CharField(null=True, max_length=255)
    nickname = fields.CharField(default='binkuolo', max_length=255, description='昵称')
    u_phone = fields.CharField(null=True, description="手机号", max_length=11)
    u_email = fields.CharField(null=True, description='邮箱', max_length=255)
    full_name = fields.CharField(null=True, description='姓名', max_length=255)
    u_status = fields.IntField(default=0, description='0未激活 1正常 2禁用')
    head_img = fields.CharField(null=True, max_length=255, description='头像')
    sex = fields.IntField(default=0, null=True, description='0未知 1男 2女')
    remarks = fields.CharField(null=True, max_length=30, description="备注")
    client_host = fields.CharField(null=True, max_length=19, description="访问IP")
    create_time = fields.DatetimeField(auto_now_add=True, description='创建时间')
    update_time = fields.DatetimeField(auto_now=True, description="更新时间")
#default=False    赋值python对象False，存入数据库时有相应的bool值
#auto_now         更新记录时自动更新时间
#auto_now_add     只在记录创建时赋值当前时间


    class Meta:
        table_description = "用户"
        table = "user"
# Meta类定义在User里面，作为User的属性
# sqlalchemy的meta实例可以容纳多个表
# tortoise的meta实例容纳单独一个表