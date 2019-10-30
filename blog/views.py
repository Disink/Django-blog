from django.shortcuts import render
from django.views import generic
from blog.models import Post, Comment, Tag
from blog.forms import CommentForm
from django.shortcuts import render, get_object_or_404

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

#class PostDetail(generic.DetailView):
#    model = Post
#    template_name = 'post_detail.html'

def post_detail(request, slug):
    template_name = 'post_detail.html'
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True, replay=None)
    comments_all = post.comments.filter(active=True)
    tags = post.tags.all()
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST, slug=slug)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            #print(request.POST.get('replay'))

            replay_id = request.POST.get('replay')
            if replay_id == '':
                floor = comments.count() + 1
                new_comment.floor = floor
            else:
                floor = comments_all.filter(replay_id).count()+1
                new_comment.floor = floor
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm(slug=slug)

    return render(request, template_name, {'post': post,
                                           'tags': tags,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})

def tag_detail(request, slug):
    template_name = 'tag_detail.html'
    tag = get_object_or_404(Tag, slug=slug)
    posts = tag.post_set.all()

    return render(request, template_name, {'posts': posts})
