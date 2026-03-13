from django.contrib import admin
from .models import News, Project, CodigoSocialCard, HealthcareJuniorCard, Product, TeamMember, Eventos, CodigoSocialFoto


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'is_featured')
    search_fields = ('title', 'summary')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'created_at')
    list_filter = ('is_active',)
    search_fields = ('title', 'summary')

@admin.register(CodigoSocialCard)
class CodigoSocialCardAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'is_active', 'created_at')
    list_filter = ('status', 'is_active')
    search_fields = ('title', 'description')

@admin.register(HealthcareJuniorCard)
class HealthcareJuniorCardAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'is_active', 'created_at')
    list_filter = ('status', 'is_active')
    search_fields = ('title', 'description')
    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'is_active', 'created_at')
    list_filter = ('is_active',)
    search_fields = ('title', 'description')

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'order');
    ordering = ('order',);
    
@admin.register(Eventos)
class EventosAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'is_featured', 'created_at');
    list_filter = ('is_active', 'is_featured');
    search_fields = ('title', 'description');
    list_editable = ('is_active', 'is_featured');
    ordering = ('-created_at',);
    
admin.site.register(CodigoSocialFoto)