from django.shortcuts import render
from django.conf import settings
from django.urls import reverse, NoReverseMatch


def installed_apps_view(request):
    installed_apps = settings.INSTALLED_APPS
    app_urls = []

    # Map any app config class names to actual app names as needed
    app_name_map = {
        "UsersConfig": "users",
        "CourtsConfig": "courts",
        # Map UsersConfig to users namespace
        # Add other mappings as needed
    }

    for app in installed_apps:
        print("APP NAME: ", app)
        app_config_name = app.split(".")[-1]
        app_name = app_name_map.get(
            app_config_name, app_config_name.lower()
        )  # Use lowercase if no map exists

        try:
            url = reverse(f"{app_name}:index")
            print("URL: ", url)
            app_urls.append({"name": app_name, "url": url})
        except NoReverseMatch:
            continue

    context = {"app_urls": app_urls}
    return render(request, "installed_apps.html", context)
