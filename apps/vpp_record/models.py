from django.db import models

# Create your models here.


class AdminUser(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=False, unique=True)
    password = models.CharField(max_length=255, blank=False)

    # def summary_json(self):
    #     nursing_org = self.nursing_org
    #     return {
    #         'id': self.id,
    #         'name': self.name,
    #         'age': utils.birthday_to_age(self.birthday),
    #         'gender': self.gender,
    #         'phone': self.phone,
    #         'birthday': self.birthday,
    #         # 'state': self.state,
    #         # 'stateName': NursingOrgEnum.NursingOrgStaffTypeEnum.DISPLAY_NAME[self.state],
    #         'remark': self.remark,
    #         'nursingOrgId': nursing_org.id,
    #         'nursingOrgName': nursing_org.name,
    #         'type': self.type,
    #         'typeName': NursingOrgEnum.NursingOrgStaffTypeEnum.DISPLAY_NAME[self.type],
    #         'position': NursingOrgEnum.NursingOrgStaffTypeEnum.DISPLAY_NAME[self.type],
    #         'avatar': self.avatar_url if self.avatar_url else default_avatar_url
    #     }

    @classmethod
    def get_user_by_name(cls, name):
        return AdminUser.objects.get(name=name)


    class Meta:
        db_table = 'vpp_user'


