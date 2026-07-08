from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


#1. lokasi database sqlite
SQLALCHEMY_DATABASE_URL = "sqlite:///./cashier.db"

#2. Membuat mesin utama (engine) untuk mengelola koneksi ke SQLite
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args = {"check_same_thread" : False}

)

# 3. membuat pabrik sesi (SessionLocal) untuk transaksi data (Insert, Update, Select, Delete)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 4. bikin base class. Semua model tabel database nanti wajib warisan dari Base ini
Base = declarative_base()

#5 fungsi bantuan (Depency) buat ngebuka dan nutup koneksi database secara otomatis
def get_db():
    db = SessionLocal()
    try :
        yield db
    finally :
        db.close()