from typing import Optional
from sqlalchemy import Boolean, DateTime, Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base
from datetime import datetime, timezone

class Mensajes(Base):
    __tablename__ = "mensajes"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nombre: Mapped[str] = mapped_column(String(50), nullable=False)
    email: Mapped[Optional[str]] = mapped_column(String(50), nullable=True) 
    telefono: Mapped[Optional[str]] = mapped_column(String(15), nullable=True) 
    mensaje: Mapped[str] = mapped_column(String(200), nullable = False)
    fecha: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=lambda: datetime.now(timezone.utc))
    estado: Mapped[bool] = mapped_column(Boolean, default = True, nullable = False)
