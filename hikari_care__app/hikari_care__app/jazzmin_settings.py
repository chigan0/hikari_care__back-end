from django.utils.translation import gettext_lazy as _

# Jazzmin Admin Panel Settings

JAZZMIN_SETTINGS = {
	"project_name": "Hikari Care",
	"project_version": "0.0.6",

	# title of the window (Will default to current_admin_site.site_title if absent or None)
	"site_title": "Hikari Care",

	# Title on the login screen (19 chars max) (defaults to current_admin_site.site_header if absent or None)
	"site_header": "Hikari Care",

	# Title on the brand (19 chars max) (defaults to current_admin_site.site_header if absent or None)
	"site_brand": "Hikari Care",

	# Logo to use for your site, must be present in static files, used for brand on top left
	"site_logo": "img/logo.png",

	# Logo to use for your site, must be present in static files, used for login form logo (defaults to site_logo)
	"login_logo": "img/logo.png",

	# Logo to use for login form in dark themes (defaults to login_logo)
	"login_logo_dark": None,

	# CSS classes that are applied to the logo above
	"site_logo_classes": "img-circle",

	# Relative path to a favicon for your site, will default to site_logo if absent (ideally 32x32 px)
	"site_icon": "img/logo.png",

	# Welcome text on the login screen
	"welcome_sign": _("Wellcome to Hikari Care"),

	# Copyright on the footer
	"copyright": "Hikari Care",

	# List of model admins to search from the search bar, search bar omitted if excluded
	# If you want to use a single search field you dont need to use a list, you can use a simple string
	"search_model": ["auth.User", "auth.Group"],

	# Field name on user model that contains avatar ImageField/URLField/Charfield or a callable that receives the user
	"user_avatar": None,

	############
	# Top Menu #
	############

	# Links to put along the top menu
	"topmenu_links": [
		{"name": _("Home"),  "url": "admin:index", "permissions": ["auth.view_user"]},
		{"model": "auth.User"},
		{"app": "projects"}
	],

	#############
	# User Menu #
	#############

	# Additional links to include in the user menu on the top right ("app" url type is not allowed)
	"usermenu_links": [
		# {"name": "Support", "url": "https://github.com/farridav/django-jazzmin/issues", "new_window": True},
		{"model": "auth.user"}
	],

	#############
	# Side Menu #
	#############

	# Whether to display the side menu
	"show_sidebar": True,

	# Whether to aut expand the menu
	"navigation_expanded": False,
	"show_ui_builder": True,

	"order_with_respect_to": [
		"auth",
		"core",
		"employees",
		"news",
		"sa_gallery",
		"core.MIND",
		"core.Procedure",
		"core.PriceList"
		# "auth",
		# "macro",
		# "macro.MacroHousess",
		# "macro.MacroLayouts",
		# "projects",
		# "projects.Project",
		# "projects.Promotions",
		# "projects.ProjectConstProgressElement",
		# "mortgage",
		# "media_scope",
		# "vacancy",
		# "vacancy.VacancyCategory",
		# "vacancy.Vacancies",
		# "core",
		# "core.PrivacyPolicy",
		# "core.CompanyHistory",
		# "core.Translation",
		# "core.CoreImages",
	],

	"side_drop_menu": {
		"projects": {
			"icon": "fas fa-comments"
		}
	},
	"icons": {
		"auth": "fas fa-users-cog",
		"auth.Group": "fas fa-users",
		"auth.user": "fas fa-user",
		"auth.Group": "fas fa-users",
		"core": "fas fa-cogs",
		"core.MIND": "fas fa-stethoscope",
		"sa_gallery": "fas fa-images",
		"sa_gallery.SaGalleryImage": "fas fa-image",
		"employees": "fas fa-users",
		"employees.employee": "fas fa-user-md",
		"news": "fas fa-bullhorn",
		"news.News": "fas fa-newspaper",
		"core.Procedure": "fas fa-syringe",
		"core.PriceList": "fas fa-clipboard-list",
		"core.MINDType": "fas fa-hospital"
		# "auth.user": "fas fa-user",
		# "auth.Group": "fas fa-users",
		# "projects.Project": "fas fa-building",
		# "projects.Promotions": "fa fa-ad",
		# "projects.ProjectInfraLocationCats": "fa fa-map-marker-alt",
		# "projects.ProjectConstProgressElement": "fa fa-tasks",
		# "macro.MacroHousess": "fas fa-city",
		# "macro.MacroLayouts": "fas fa-drafting-compass",
		# "core.CoreImages": "fas fa-image",
		# "core.HomeLargeBanners": "fas fa-solid fa-images",
		# "core.Translation": "fas fa-solid fa-language",
		# "core.Management": "fas fa-user-tie",
		# "core.DropMenuBanners": "fas fa-images",
		# "core.PrivacyPolicy": "fas fa-gavel",
		# "core.CompanyHistory": "fas fa-archive",
		# "media_scope.MediaScopeCategory": "fas fa-list-alt fa-cube",
		# "media_scope.News": "fas fa-newspaper fa-cube",
		# "mortgage.Banks": "fas fa-piggy-bank",
		# "mortgage.Mortgage": "fas fa-percent",
		# "vacancy.VacancyCategory": "fas fa-folder-open",
		# "vacancy.Vacancies": "fas fa-briefcase",
	},

	"default_icon_parents": "fas fa-chevron-circle-right",
	"default_icon_children": "fas fa-circle",
	"related_modal_active": False,

	"custom_css": None,
	"custom_js": None,
	# Whether to link font from fonts.googleapis.com (use custom_css to supply font otherwise)
	"use_google_fonts_cdn": True,
	"changeform_format": "horizontal_tabs",
	"changeform_format_overrides": {"auth.user": "collapsible", "auth.group": "vertical_tabs"},
	"language_chooser": True,
}

# Style config
JAZZMIN_UI_TWEAKS = {
	"navbar_small_text": False,
	"footer_small_text": False,
	"body_small_text": True,
	"brand_small_text": False,
	"brand_colour": False,
	"accent": "accent-navy",
	"navbar": "navbar-white navbar-light",
	"no_navbar_border": False,
	"navbar_fixed": False,
	"layout_boxed": False,
	"footer_fixed": True,
	"sidebar_fixed": True,
	"sidebar": "sidebar-dark-navy",
	"sidebar_nav_small_text": False,
	"sidebar_disable_expand": True,
	"sidebar_nav_child_indent": True,
	"sidebar_nav_compact_style": True,
	"sidebar_nav_legacy_style": False,
	"sidebar_nav_flat_style": True,
	"theme": "default",
	"dark_mode_theme": None,
	"button_classes": {
		"primary": "btn-primary",
		"secondary": "btn-secondary",
		"info": "btn-info",
		"warning": "btn-warning",
		"danger": "btn-danger",
		"success": "btn-success"
	},
	'actions_sticky_top': True
}


JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": True,
    "brand_small_text": False,
    "brand_colour": False,
    "accent": "accent-navy",
    "navbar": "navbar-white navbar-light",
    "no_navbar_border": True,
    "navbar_fixed": False,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": True,
    "sidebar": "sidebar-dark-navy",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": True,
    "sidebar_nav_child_indent": True,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": False,
    "theme": "litera",
    "dark_mode_theme": None,
    "button_classes": {
        "primary": "btn-primary",
        "secondary": "btn-outline-secondary",
        "info": "btn-info",
        "warning": "btn-warning",
        "danger": "btn-danger",
        "success": "btn-success"
    },
    "actions_sticky_top": False
}
