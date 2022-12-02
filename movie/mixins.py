class GetSerializerMixin:
	def get_serializer(self, *args, **kwargs):
		if self.action in ['create', 'update']:
			return self.create_update_serializer(*args, **kwargs)
		return self.serializer_class(*args, **kwargs)