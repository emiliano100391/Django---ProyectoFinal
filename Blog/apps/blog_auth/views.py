from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import FormView
from Blog.apps.blog_auth.forms import SignUpForm

class SignUpView(FormView):
    template_name = 'registration/registro.html'
    form_class = SignUpForm
    success_url = reverse_lazy("apps.blog_auth:login")
    def form_valid(self,form):
        form.save()
        return super().form_valid(form)

    def register_view(request):
        if request.method == 'POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('apps.blog.auth:login')
        else:
            form = SignUpForm()
        return render(request, 'registration/registro.html', {'form':form})