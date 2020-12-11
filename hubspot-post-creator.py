# run: python hubspot-post-creator.py <title> <link to raw post in Github with token> <hubspot API key>

import requests
import markdown
import re
import sys
import json

if len(sys.argv) != 5:
    print ('error')
    sys.exit(1)

title = sys.argv[1]
inputUrl = sys.argv[2]
hubspotApiKey = sys.argv[3]
hubspotBlogId = sys.argv[4]

print("Creating post '{}' in Hubspot".format(title))

github_url = inputUrl
r = requests.get(github_url, allow_redirects=True)
html = r.content.decode('utf-8')
r = re.sub('^---[\s\S]+?---', '', html)

htmlForHubspot = markdown.markdown(r, encoding='utf8')
hubspotUrl = 'https://api.hubapi.com/content/api/v2/blog-posts?hapikey={}'.format(hubspotApiKey)

postBody = {
  "name": title,
  "content_group_id": hubspotBlogId,
  "post_body": htmlForHubspot
}
headers = {'Content-Type': "application/json"}
response = requests.request("POST", hubspotUrl, data=json.dumps(postBody), headers=headers)
if response.status_code == 201:
    print ('\nHubspot: Post successfully created in Hubspot\n')
else:
    print ('\nHubspot: Error {} occured. See the response below\n'.format(response.status_code))
    print (response.json())