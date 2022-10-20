from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from users.models import BotUser


def homeview(request):
    return render(request, 'admin_panel/admin_panel_home.html')


class BotUsersList(TemplateView):
    template_name = 'admin_panel/bot_users_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bot_users'] = BotUser.objects.all()
        return context
