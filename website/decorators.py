from django.shortcuts import redirect

def allowed_user(allowed_roles=[]):
    def deccorators(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_roles or request.user.is_superuser:
                return view_func(request, *args, **kwargs)
            else:
                return redirect("home")

        return wrapper_func

    return deccorators