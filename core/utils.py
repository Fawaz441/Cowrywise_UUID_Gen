from .models import UUID

def get_uuids():
    uuids = {}
    # fetch all uuids 
    uuid_qs = UUID.objects.all()
    for uuid in uuid_qs:
        uuids[str(uuid.timestamp)] = uuid.uuid
    return uuids