from django.shortcuts import render
from django.views import generic
from news.models import NewsModel
import time

# Create your views here.

class MainIndex(generic.TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = {}
        context["news_list"] = NewsModel.objects.all()
        return context


class NewsDetail(generic.DetailView):
    template_name = "detail.html"
    model = NewsModel

    def get_context_data(self, **kwargs):
        context = super(NewsDetail, self).get_context_data(**kwargs)
        now = time.time()
        if self.request.session.get(f"preview_{self.object.pk}", False):
            # Have preview
            session_time = self.request.session[f"preview_{self.object.pk}"]
            if(now - session_time) > 10:
                today = time.time()
                self.request.session[f"preview_{self.object.pk}"] = today
                self.object.preview_count += 1
                self.object.save()
                context["object"] = self.object
        else:
            # not preview
            today = time.time()
            self.request.session[f"preview_{self.object.pk}"] = today
            self.object.preview_count += 1
            self.object.save()
            context["object"] = self.object
        return context
