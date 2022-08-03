# -*- coding:utf-8 -*-
from sqlalchemy import Column, String, TIMESTAMP, INTEGER, text

from src.models import db


class CabinetWorkStatistics(db.Model):
    __tablename__ = "cabinet_work_statistics"

    id = Column(INTEGER, primary_key=True)
    asset_id = Column(String(64), nullable=False, comment="资产编号")
    created_at = Column(
        TIMESTAMP,
        nullable=False,
        server_default=text("CURRENT_TIMESTAMP"),
        comment="创建时间",
    )
    updated_at = Column(
        TIMESTAMP,
        nullable=False,
        server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"),
        comment="更新时间",
    )
    total_online_time = Column(
        INTEGER, nullable=False, server_default=text("'0'"), comment="累计开机时间"
    )

    @classmethod
    def get_by_asset_id(cls, asset_id):
        result = db.session.query(cls).filter_by(asset_id=asset_id).one_or_none()
        if not result:
            raise Exception(
                f"Cannot find CabinetWorkStatistics by asset_id: {asset_id}"
            )
        return result

    @classmethod
    def create(cls, asset_id, online_time):
        obj = cls(asset_id=asset_id, total_online_time=online_time)
        with db.auto_commit():
            db.session.add(obj)
            print(type(obj))
        print(hasattr(obj, "id"))
        if hasattr(obj, "id"):
            print(obj.id)
        if hasattr(obj, "created_at"):
            print(obj.created_at)
