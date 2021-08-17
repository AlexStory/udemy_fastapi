from sqlalchemy import column, BigInteger, String, Boolean, Date, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import Column, Index
from sqlalchemy.sql.sqltypes import DateTime
from uuid import uuid4

from server.db.base_class import BaseClass


class Job(BaseClass):
    id = Column(BigInteger, primary_key=True, index=True)
    title = Column(String, nullable=False)
    company = Column(String, nullable=False)
    company_url = Column(String)
    location = Column(String, nullable=False)
    description = Column(String)
    date_posted = Column(Date)
    is_active = Column(Boolean, default=True)
    owner_id = Column(BigInteger, ForeignKey("user.id"))
    owner = relationship("User", back_populates="jobs")
