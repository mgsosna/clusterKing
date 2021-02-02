import pandas as pd
from sklearn import cluster

class ClusterLabeler:

    def kmeans(self,
               data: dict) -> list:
        df = pd.DataFrame(data)

        x = cluster.KMeans(n_clusters=2).fit(df)
        df['cluster'] = x.labels_

        return df.to_json(orient='records')

    def kmeans_simple(self,
               data: dict) -> list:

        x = cluster.KMeans(n_clusters=2).fit(pd.DataFrame(data))
        return [int(val) for val in x.labels_]
