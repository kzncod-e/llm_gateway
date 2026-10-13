from sqlalchemy.dialects.postgresql import JSONB
from ast import List
from sqlalchemy import Boolean
from datetime import datetime
from sqlalchemy import String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from llm_gateway.schemas.database import Base
class Team(Base):
    __tablename__="teams"
    id:Mapped[int]=mapped_column(Integer)
    name:Mapped[str]
    monthy_rate_limit:Mapped[int] =mapped_column(Integer,nullable=True,default=5000)
    created_at:Mapped[datetime] = mapped_column(DateTime,default=datetime.now())
    is_active:Mapped[bool] = mapped_column(Boolean,default=True)
    users:List["User"]=relationship(back_populates="team")

    

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True,index=True)
    name: Mapped[str]=mapped_column(String,nullable=False)
    email: Mapped[str] = mapped_column(String,unique=True,index=True)
    password: Mapped[str]=mapped_column(String,nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime)
    team_id:Mapped[int]=mapped_column(ForeignKey("teams.id"))
    team:Mapped["Team"]

class Rate_limit_policies(Base):
    __tablename__= "rate_limit_policies"
    id:Mapped[int]=mapped_column(Integer,primary_key=True,index=True)
    name:Mapped[str]
    max_rpm:Mapped[int]
    max_tpm:Mapped[int]
    created_at:Mapped[datetime] = mapped_column(DateTime,default=datetime.now())
    
    
    id:Mapped[int]=mapped_column(Integer,primary_key=True,index=True)
    user_id:Mapped[int] = mapped_column(ForeignKey("users.id"))
    


class Apikey(Base):
    __tablename__ = "apikeys"
    
    id:Mapped[int]=mapped_column(Integer,primary_key=True,index=True)
    name:Mapped[str]
    team_id:Mapped[int]=mapped_column(ForeignKey("teams.id"))
    key_hash:Mapped[str]=mapped_column(String)
    created_at:Mapped[datetime] = mapped_column(DateTime,default=datetime.now())
    expires_at:Mapped[datetime] = mapped_column(DateTime)
    is_active:Mapped[bool]=mapped_column(Boolean,default=True)
    allowoed_models:Mapped[List[str]] = mapped_column(JSONB)
    

class Request_logs(Base):
    __tablename__ = "request_logs"
    id:Mapped[int]=mapped_column(Integer,primary_key=True,index=True)
    requested_model:Mapped[str]
    team_id:Mapped[int]=mapped_column(ForeignKey("teams.id"))
    api_key_id:Mapped[int]=mapped_column(ForeignKey("apikeys.id"))
    response_time:Mapped[float]
    status_code:Mapped[int]
    completion_token:Mapped[int]
    prompt_token:Mapped[int]
    total_tokens:Mapped[int]
    created_at:Mapped[datetime] = mapped_column(DateTime,default=datetime.now())
    responded_at:Mapped[datetime] = mapped_column(DateTime,default=datetime.now())
    
    
    