Basic Python script to read a markdown file from a URL (e.g. a raw markdown file in a Github repository), strip the front matter/YAML, convert to HTML, and create as a blog post in Hubspot.

## How to use
It's a simple script that requires a few variables as arguments when running:
- The title of the post
- The publically accessible URL of the markdown file (e.g. a link to the raw file on Github with token as a parameter if private)
- API key for the Hubspot account you want to publish to
- The ID of the Hubspot blog you want to publish to (you can find this in the URL of the settings page for the blog in Hubspot, an 11 digit number)

**Simply run:**
```python hubspot-post-creator.py <title> <input URL> <Hubspot API key> <Hubspot blog ID>```

## Notes
- Your Hubspot account must have the required level to be able to create blogs
- The blog post will go in as unpublished allowing you to adjust meta information and custom settings
- Images must be added through the Hubspot UI into the blog post where applicable
