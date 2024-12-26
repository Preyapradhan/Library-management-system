# Sample members data
member = {
    "1": {
        "id": "1",
        "name": "Alice Johnson",
        "email": "alice.johnson@example.com",
        "join_date": "2023-05-15"
    },
    "2": {
        "id": "2",
        "name": "Bob Smith",
        "email": "bob.smith@example.com",
        "join_date": "2023-06-10"
    },
    "3": {
        "id": "3",
        "name": "Charlie Brown",
        "email": "charlie.brown@example.com",
        "join_date": "2023-07-20"
    },
    "4": {
        "id": "4",
        "name": "David Lee",
        "email": "david.lee@example.com",
        "join_date": "2023-08-05"
    }
}


def add_member(member_id, data):
    member[member_id] = data

def get_member(member_id):
    return member.get(member_id)

def update_member(member_id, data):
    if member_id in member:
        member[member_id].update(data)

def delete_member(member_id):
    if member_id in member:
        del member[member_id]
