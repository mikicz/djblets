"""An avatar service for providing Gravatars."""

from __future__ import unicode_literals

from django.utils.html import mark_safe

from djblets.avatars.services.base import AvatarService
from djblets.gravatars import get_gravatar_url_for_email


class GravatarService(AvatarService):
    """An avatar service for providing Gravatars."""

    avatar_service_id = 'gravatar'
    name = 'Gravatar'

    def get_avatar_urls_uncached(self, request, user, size):
        """Return the avatar URLs for the requested user.

        Args:
            request (django.http.HttpRequest):
                The current HTTP request.

            user (django.contrib.auth.models.User):
                The user whose avatar URLs are to be fetched.

            size (int):
                The size (in pixels) the avatar is to be rendered at.

        Returns
            dict:
            A dictionary containing the URLs of the user's avatars at normal-
            and high-DPI.
        """
        return {
            '%dx' % resolution: mark_safe(get_gravatar_url_for_email(
                request, user.email, size * resolution))
            for resolution in (1, 2, 3)
        }
