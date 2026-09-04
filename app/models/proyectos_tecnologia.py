from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base

class ProyectosTecnologia(Base):
    __tablename__ = "proyecto_tecnologia"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    id_proyecto: Mapped[int] = mapped_column(ForeignKey("proyectos.id"), nullable=False) 
    id_tecnologia: Mapped[int] = mapped_column(ForeignKey("tecnologias.id"), nullable=False)
    
