from crud.line_communication_state import LineCommunicationStateCrud
from crud.schemas import LINECommunicationStateSchema


# redisに保存されたデータを取得
def get_saved_data(line_id: str) -> LINECommunicationStateSchema | None:
    with LineCommunicationStateCrud() as line_communication_state_crud:
        data = line_communication_state_crud.get(line_id)
    return data


# line_idに紐づくデータを登録、ステータスの更新
def set_saved_data(line_id: str, schema: LINECommunicationStateSchema):
    with LineCommunicationStateCrud() as line_communication_state_crud:
        line_communication_state_crud.set(
            line_id,
            schema
        )


# ステータスを削除
def delete_saved_data(line_id: str):
    with LineCommunicationStateCrud() as line_communication_state_crud:
        line_communication_state_crud.delete(line_id)
