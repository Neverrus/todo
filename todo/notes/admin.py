from django.contrib import admin

from django.contrib import admin

from django.contrib import admin

from notes.models import Note, Tags


@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    list_display = ("title",)
    fields = ("title",)
    search_fields = ("title",)


class TagsAdminInline(admin.TabularInline):
    model = Tags.posts.through


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at")
    fields = ("author", "title", "image", "slug", "text", "created_at")
    readonly_fields = ("created_at",)
    search_fields = ("title", "slug", "text")

    inlines = (TagsAdminInline,)
