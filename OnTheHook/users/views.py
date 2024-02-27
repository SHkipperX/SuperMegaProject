from django.conf import settings
from django.contrib.auth import login
from django.shortcuts import render
from django.views import generic
from django.views import View

from users.forms import CustomUserCreateForm, EditProfile
from users.models import User

__all__ = []

PATH = "users/"


class ProfileView(View):
    template = PATH + "profile.html"
    context = {}

    def get(self, request, *args, **kwargs):
        self.context["model"] = request.user
        self.context["form"] = EditProfile(instance=request.user)
        return render(request, self.template, self.context)

    def post(self, request, *args, **kwargs):
        form = EditProfile(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            file = request.FILES.get("avatar")
            if file:
                request.user.avatar = file
                request.user.save()
        self.context["form"] = form
        return render(request, self.template, self.context)


class RegisterView(generic.FormView):
    template_name = PATH + "auth/register.html"
    form_class = CustomUserCreateForm
    success_url = "/auth/profile/"

    def form_valid(self, form):
        normalize_email = User.objects.normalize_email(
            form.cleaned_data["email"],
        )
        form.is_active = settings.DEFAULT_USER_IS_ACTIVE
        form.email = normalize_email
        form.save()

        login(
            self.request,
            User.objects.get(username=form.cleaned_data["username"]),
            backend="OnTheHook.backends.ModifyLogin",
        )
        return super().form_valid(form)


class ActivateView(generic.View):
    tempalte_name = ...
    context = ...
    model = User

    def get(self, request):
        ...
        return render(request, self.tempalte_name, self.context)
