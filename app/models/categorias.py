from typing import Optional
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database import Base

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from app.models.proyectos import Proyectos

class Categorias(Base):
    __tablename__ = "categorias"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nombre: Mapped[str] = mapped_column(String(50), nullable=False)
    descripcion: Mapped[Optional[str]] = mapped_column(String(200), nullable=True)  
    
    proyectos: Mapped[list["Proyectos"]] = relationship(back_populates="categoria")
    
