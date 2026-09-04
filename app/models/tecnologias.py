from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database import Base

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from app.models.proyectos import Proyectos

class Tecnologias(Base):
    __tablename__ = "tecnologias"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nombre: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    
    proyectos: Mapped[list["Proyectos"]] = relationship(
            secondary="proyecto_tecnologia",
            back_populates="tecnologias"
        )