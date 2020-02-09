from django.shortcuts import render
from django.views import generic

from transfers.utils import get_context_data


class HODHomeView(generic.TemplateView):
    template_name = 'transfers/hod_supervisor_common.html'
    context = {}

    def get(self, request, *args, **kwargs):
        self.context = get_context_data(request.user, designation='HOD')
        return render(request, self.template_name, self.context)
