# -*- encoding: utf-8 -*-

f = open('test.txt', 'w')

from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser
import sys
import os
import json
import urllib

API_KEY = "AIzaSyC67Fpe6DqMEmGo-GC_VLz1Ezx5NVkF7NA"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"
QUERY_TERM = "Автомобиль"

def youtube_search(options):
  youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    developerKey=API_KEY)

  # Call the search.list method to retrieve results matching the specified
  # query term.
  search_response = youtube.search().list(
    q=options.q,
    type="video",
    location=options.location,
    locationRadius=options.location_radius,
    part="id,snippet",
    maxResults=options.max_results
  ).execute()

  search_videos = []

  # Merge video ids
  for search_result in search_response.get("items", []):
    search_videos.append(search_result["id"]["videoId"])
  video_ids = ",".join(search_videos)

  # Call the videos.list method to retrieve location details for each video.
  video_response = youtube.videos().list(
    id=video_ids,
    part='snippet,contentDetails,statistics'
  ).execute()

  videos = []

  # Add each result to the list, and then display the list of matching videos.
  for video_result in video_response.get("items", []):
        videos.append(video_result)

  t_videos = []

  for i in range(len(videos)):
      t_videos.append(json.dumps(videos[i], ensure_ascii=False).encode('utf8'))

  print(json.loads(t_videos[0], ensure_ascii = False)["snippet"])


if __name__ == "__main__":
  argparser.add_argument("--q", help="Search term", default=QUERY_TERM)
  argparser.add_argument("--location", help="Location", default="58.469983,44.394051")
  argparser.add_argument("--location-radius", help="Location radius", default="500km")
  argparser.add_argument("--max-results", help="Max results", default=40)
  args = argparser.parse_args()


  try:
    youtube_search(args)
  except HttpError, e:
    print "An HTTP error %d occurred:\n%s" % (e.resp.status, e.content)

f.close()
