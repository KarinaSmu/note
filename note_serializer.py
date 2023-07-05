from note import Note


class NoteSerializer:
    @staticmethod
    def serialize(note):
        return {
            "id": note.id,
            "title": note.title,
            "body": note.body,
            "created_at": note.created_at,
            "updated_at": note.updated_at
        }

    @staticmethod
    def deserialize(data):
        return Note(
            id=data["id"],
            title=data["title"],
            body=data["body"],
            created_at=data["created_at"],
            updated_at=data["updated_at"]
        )
