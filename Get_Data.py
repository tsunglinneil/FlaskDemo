import Leveldb_Util

# Get_Data方法說明：單純的對資料庫做一些操作(建資料庫、寫入資料、印出資料)
def get_data():
    flaskdb = Leveldb_Util.init("flaskdb")
    batch_data = Leveldb_Util.init_batch()

    Leveldb_Util.write_batch(batch_data, "customer1", "Bob")
    Leveldb_Util.write_batch(batch_data, "customer2", "Tim")
    Leveldb_Util.write_batch(batch_data, "customer3", "Ken")
    Leveldb_Util.commit_batch(flaskdb, batch_data)
    Leveldb_Util.dump(flaskdb)

    return Leveldb_Util.search(flaskdb, "customer1")