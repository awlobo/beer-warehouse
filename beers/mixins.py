

class AddMyBirthdayToCOntextMixin(object):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bday'] = "mi cumple es el 25 de noviembre"

        return context

