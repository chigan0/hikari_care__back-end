from typing import Any

from django.http import HttpRequest

image_url_or = lambda req, img, default_val=None: req.build_absolute_uri(img.original.url) if img else default_val
