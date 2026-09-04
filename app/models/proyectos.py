from typing import Optional
from sqlalchemy import Boolean, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database import Base

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from app.models.categorias import Categorias
    from app.models.tecnologias import Tecnologias
    
class Proyectos(Base):
    __tablename__ = "proyectos"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nombre: Mapped[str] = mapped_column(String(50), nullable=False)
    id_categoria: Mapped[int] = mapped_column(ForeignKey("categorias.id"), nullable=False) 
    descripcion: Mapped[Optional[str]] = mapped_column(String(200), nullable=True) 
    link: Mapped[str] = mapped_column(String(100), nullable = False)
    link_demo: Mapped[Optional[str]] = mapped_column(String(100), nullable = True)
    imagen: Mapped[str] = mapped_column(String(100), nullable = False)
    estado: Mapped[bool] = mapped_column(Boolean, default = True, nullable = False)
    
    tecnologias: Mapped[list["Tecnologias"]] = relationship(
        secondary="proyecto_tecnologia",
        back_populates="proyectos"
    )
        
    categoria: Mapped["Categorias"] = relationship(back_populates="proyectos")
