from django.views.generic import ListView, DetailView

from .models import Post, Topic


class BlogListView(ListView):
    template_name = 'blog/list.html'
    paginate_by = 6

    def get_queryset(self):
        search = self.request.GET.get('search')
        topic = self.request.GET.get('topic')
        if search is not None:
            queryset = Post.objects.filter(title__icontains=search).order_by('-publish_date') | Post.objects.filter(
                content__in=search).order_by('-publish_date') | Post.objects.filter(
                topic__name__icontains=search).order_by('-publish_date')
        elif topic is not None:
            queryset = Post.objects.filter(topic__name=topic).order_by('-publish_date')
        else:
            queryset = Post.objects.all().order_by('-publish_date')

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        topics = Topic.objects.all()
        context['top_topics'] = topics[:4]
        context['search'] = self.request.GET.get('search', "")
        context['topics'] = topics
        return context


class BlogDetailView(DetailView):
    template_name = 'blog/detail.html'
    model = Post

    def get(self, request, *args, **kwargs):
        # Get the post object
        post = self.get_object()

        # Check if this post has already been visited in the current session
        if f'viewed_post_{post.pk}' not in request.session:
            # If not, increment the views count by 1
            post.views += 1
            post.save()
            # Mark this post as visited in the current session
            request.session[f'viewed_post_{post.pk}'] = True

        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        topics = Topic.objects.all()
        context['topics'] = topics
        return context

