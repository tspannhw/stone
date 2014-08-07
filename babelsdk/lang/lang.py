
class TargetLanguage(object):

    _language_short_name = 'unk'

    def get_language_short_name(self):
        return self._language_short_name

    def get_supported_extensions(self):
        raise NotImplemented

    def format_method(self, words):
        raise NotImplemented

    def format_class(self, words):
        raise NotImplemented

    def format_variable(self, words):
        raise NotImplemented

    def format_type(self, data_type):
        raise NotImplemented

    def format_obj(self, o):
        raise NotImplemented
