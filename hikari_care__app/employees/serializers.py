from rest_framework.serializers import ModelSerializer, SerializerMethodField, CharField

from sa_gallery import image_url_or
from .models import Employee

class EmployeeSerializer(ModelSerializer):
	mind = SerializerMethodField()
	photo = SerializerMethodField()

	lastName = CharField(source='last_name')
	firstName = CharField(source='first_name')
	middleName = CharField(source='middle_name')
	qualification = CharField()  # source совпадает — удаляем
	medicalExperience = CharField(source='med_total_exp')
	departmentExperience = CharField(source='exp_in_the')
	jobTitle = CharField(source='job_title')
	bio = CharField(source='about_employee')

	def __init__(self, *args, **kwargs):
		# вызов оригинального init
		super().__init__(*args, **kwargs)

		for field_name in self.context.get("exclude_fields", ()):
			self.fields.pop(field_name, None)

	class Meta:
		model = Employee
		fields = (
			"uuid",
			"lastName",
			"firstName",
			"middleName",
			"qualification",
			"medicalExperience",
			"departmentExperience",
			"jobTitle",
			"bio",
			"photo",
			"mind"
		)

	get_mind = lambda self, obj: [m.get_json(self.context.get('request')) for m in obj.mind.all()]
	get_photo = lambda self, obj: image_url_or(self.context.get('request'), obj.photo)
