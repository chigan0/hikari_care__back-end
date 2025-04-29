from rest_framework.serializers import ModelSerializer, SerializerMethodField

from .models import MIND, PriceList
from sa_gallery import image_url_or

class MINDSerializer(ModelSerializer):
	icon = SerializerMethodField()
	MINDType = SerializerMethodField(source='clinic_type')

	class Meta:
		model = MIND
		fields = ("uuid", "name", "MINDType", "icon")
	
	get_icon = lambda self, obj: image_url_or(self.context.get('request'), obj.icon)
	get_MINDType = lambda _, obj: [ c_type.name for c_type in obj.clinic_type.all() ] # [ {"id": c_type.id, "name": c_type.name} for c_type in obj.clinic_type.all() ]


class PriceListSerializer(ModelSerializer):
	mind = SerializerMethodField()
	procedure = SerializerMethodField()

	class Meta:
		model = PriceList
		fields = ("name", "price_in_kzt", "mind", "procedure")
		depth = 1

	get_mind = lambda _, obj: {"id": obj.mind.id, "name": obj.mind.name}
	get_procedure = lambda _, obj: obj.procedure.name
