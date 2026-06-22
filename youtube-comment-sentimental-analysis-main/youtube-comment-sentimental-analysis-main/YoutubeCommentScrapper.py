import csv
import requests
import warnings
warnings.filterwarnings('ignore')

DEVELOPER_KEY = "AIzaSyCKLHl3BiDAHMCkw2xgdwbzB67bva8R5Xk"
BASE = "https://www.googleapis.com/youtube/v3"
SESSION = requests.Session()
SESSION.verify = False  # bypass SSL

def _get(endpoint, params):
    params['key'] = DEVELOPER_KEY
    r = SESSION.get(f"{BASE}/{endpoint}", params=params)
    return r.json()

def get_channel_id(video_id):
    data = _get("videos", {"part": "snippet", "id": video_id})
    return data['items'][0]['snippet']['channelId']

def save_video_comments_to_csv(video_id):
    comments = []
    params = {"part": "snippet", "videoId": video_id, "textFormat": "plainText", "maxResults": 100}
    while True:
        data = _get("commentThreads", params)
        for item in data.get('items', []):
            s = item['snippet']['topLevelComment']['snippet']
            comments.append([s['authorDisplayName'], s['textDisplay']])
        if 'nextPageToken' in data:
            params['pageToken'] = data['nextPageToken']
        else:
            break
    filename = video_id + '.csv'
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        w = csv.writer(f)
        w.writerow(['Username', 'Comment'])
        w.writerows(comments)
    return filename

def get_video_stats(video_id):
    data = _get("videos", {"part": "statistics", "id": video_id})
    return data['items'][0]['statistics']

def get_channel_info(youtube, channel_id):
    data = _get("channels", {"part": "snippet,statistics", "id": channel_id})
    item = data['items'][0]
    return {
        'channel_title':        item['snippet']['title'],
        'video_count':          item['statistics']['videoCount'],
        'channel_logo_url':     item['snippet']['thumbnails']['high']['url'],
        'channel_created_date': item['snippet']['publishedAt'],
        'subscriber_count':     item['statistics']['subscriberCount'],
        'channel_description':  item['snippet']['description']
    }

# dummy for compatibility
youtube = None