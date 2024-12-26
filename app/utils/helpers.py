import uuid

def generate_id():
    return str(uuid.uuid4())[:8]

def paginate(items, page, per_page):
    start = (page - 1) * per_page
    end = start + per_page
    return list(items.values())[start:end]

def search_items(items, query, keys):
    return {
        k: v for k, v in items.items()
        if any(query.lower() in v[key].lower() for key in keys)
    }
