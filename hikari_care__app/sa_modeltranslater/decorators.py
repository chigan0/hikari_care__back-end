from .translator import sa_translator, SaTranslationOptions

def register(model_or_iterable, **options):
	def wrapper(opts_class):
		if not issubclass(opts_class, SaTranslationOptions):
			raise ValueError("Wrapped class must subclass TranslationOptions.")

		sa_translator.register(model_or_iterable, opts_class, **options)
		return opts_class
	
	return wrapper
