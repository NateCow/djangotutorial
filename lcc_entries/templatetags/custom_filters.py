from django import template
import re

register = template.Library()

@register.filter
def youtube_embed(url):
    """
    Extracts the YouTube video ID from the URL and returns the embed URL.
    """
    match = re.search(r'(https?://)?(www\.)?(youtube|youtu|youtube-nocookie)\.(com|be)/(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})', url)
    video_id = match.group(6) if match else None
    return f"https://www.youtube.com/embed/{video_id}" if video_id else None