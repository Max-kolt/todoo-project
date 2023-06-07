from src.schema import RecordSchema
from uuid import uuid4
from datetime import datetime
from fastapi import HTTPException
from src.models.records import Record
from src.repository.records import RecordRepository


class RecordService:

    @staticmethod
    async def add_record_service(record: RecordSchema):
        _record_id = str(uuid4())

        if record.deadline - datetime.now() < 0:
            raise HTTPException(status_code=400, detail='Invalid data')

        _record = Record(
            id=_record_id,
            name=record.name,
            description=record.description,
            complited=False,
            archive=False,
            deadline=record.deadline,
            user_id=record.user.id
        )

        new_record = await RecordRepository.create(**Record.dict())
        return new_record

    @staticmethod
    def update_record_service(record: RecordSchema):
        if record.deadline - datetime.now() < 0:
            raise HTTPException(status_code=400, detail='Invalid data')

        _record = Record(
            name=record.name,
            description=record.description,
            complited=record.complited,
            archive=record.archive,
            deadline=record.deadline
        )

        updated_record = await RecordRepository.update(record.id, **Record.dict())
        return updated_record

