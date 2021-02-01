from sklearn import cluster

class Grouper:
    def __init__(self):
        self.dbscan = cluster.DBSCAN() 
