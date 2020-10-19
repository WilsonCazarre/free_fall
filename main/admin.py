from django.contrib import admin

import main.models as models

admin.site.register([
    models.Hero,
    models.GameMap,
])

