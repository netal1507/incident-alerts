from googleapiclient.discovery import build
from django.conf import settings

CHANNEL_ID = "UCqdWIh-42E1KU4njz4b-O3Q"


def fetch_shorts(max_results=10):
    youtube = build(
        "youtube",
        "v3",
        developerKey=settings.YOUTUBE_API_KEY
    )

    # Step 1: Search recent SHORT videos
    search_response = youtube.search().list(
        part="snippet",
        channelId=CHANNEL_ID,
        maxResults=max_results,
        type="video",
        videoDuration="short",
        order="date"
    ).execute()

    video_ids = [
        item["id"]["videoId"]
        for item in search_response.get("items", [])
        if item["id"].get("videoId")
    ]

    if not video_ids:
        return []

    # Step 2: Get video details (required for embed & stats)
    video_response = youtube.videos().list(
        part="snippet,statistics",
        id=",".join(video_ids)
    ).execute()

    return video_response.get("items", [])
