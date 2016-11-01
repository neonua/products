from .settings.base import PORTAL_URL


def portal_url_proc(request):
    """Glogal url-link for project"""
    return {'PORTAL_URL': PORTAL_URL}
