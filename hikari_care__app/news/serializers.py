from rest_framework.serializers import ModelSerializer, SerializerMethodField, CharField

from sa_gallery import image_url_or
from .models import News

class NewsSerializer(ModelSerializer):
	uuid = CharField(source="seo_name")
	title_image = SerializerMethodField()

	class Meta:
		model = News
		fields = ("uuid", "title", "desc", "small_desc", "title_image", "created_at_ed")

	def __init__(self, *args, **kwargs):
		# вызов оригинального init
		super().__init__(*args, **kwargs)

		# если передали context['exclude_desc'], убираем поле
		if self.context.get("exclude_desc"):
			self.fields.pop("desc", None)

	get_title_image = lambda self, obj: image_url_or(self.context.get('request'), obj.title_image)
