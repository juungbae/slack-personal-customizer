from notion.client import NotionClient
from api_keys import keys
from datetime import datetime
from dateutil import parser


# link of 'Article Drafts' page.
link = 'https://www.notion.so/juung/652232b8caae4e2ea24c7eafe5dc57ee?v=30deca991e6440fc9f9770d45a404b92'

def get_outdated_rows():
    # Get 'Article Drafts' page
    client = NotionClient(token_v2=keys['notion_v2'])
    view = client.get_collection_view(link)

    # Make parameter to filter unfinished drafts
    params = [{'property': 'Tags', 'comparator': 'enum_does_not_contain', 'value': 'uploaded'}]

    # Filter by parameter
    filtered_result = view.build_query(filter=params).execute()
    current = datetime.now()

    result = []

    for row in filtered_result:
        last_edited = row.last_edited
        days = (current - last_edited).days

        if days >= 2:
            url = row.get_browseable_url().replace('https://', 'notion://')

            temporary_save_obj = {
                "url": url,
                "title": row.title,
                "days": days
            }

            result.append(temporary_save_obj)
    
    return result

