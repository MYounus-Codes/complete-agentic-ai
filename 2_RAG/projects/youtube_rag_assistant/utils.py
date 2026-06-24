import re
import yt_dlp
from youtube_transcript_api import (
    YouTubeTranscriptApi,
    NoTranscriptFound,
    TranscriptsDisabled,
)


def extract_video_id(url):
    patterns = [
        r"v=([a-zA-Z0-9_-]{11})",
        r"youtu\.be\/([a-zA-Z0-9_-]{11})",
        r"shorts\/([a-zA-Z0-9_-]{11})",
    ]

    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)

    if len(url) == 11:
        return url

    raise ValueError("Invalid YouTube URL")


def get_video_title(url):
    ydl_opts = {
        "quiet": True,
        "no_warnings": True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(
            url,
            download=False,
        )

        return info["title"]


def get_playlist_videos(url):
    ydl_opts = {
        "quiet": True,
        "extract_flat": True,
        "skip_download": True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(
            url,
            download=False,
        )

    videos = []

    if "entries" in info:
        for entry in info["entries"]:
            video_id = entry["id"]
            videos.append(
                f"https://www.youtube.com/watch?v={video_id}"
            )
    else:
        videos.append(url)

    return videos


def get_transcript(video_id):
    api = YouTubeTranscriptApi()

    languages = [
        "en",
        "en-US",
        "en-GB",
        "hi",
        "hi-IN",
        "ur",
    ]

    try:
        transcript = api.fetch(
            video_id,
            languages=languages,
        )
        return transcript

    except NoTranscriptFound:
        transcript_list = api.list(video_id)
        available = list(transcript_list)

        if not available:
            raise Exception("No transcript available.")

        print(
            f"Using transcript language: "
            f"{available[0].language}"
        )

        return available[0].fetch()

    except TranscriptsDisabled:
        raise Exception(
            "Transcripts are disabled."
        )