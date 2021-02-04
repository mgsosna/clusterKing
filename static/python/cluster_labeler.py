import pandas as pd
from sklearn import cluster, mixture
from typing import Union

N_CLUSTERS = 2
EPS = 0.25   # Max distance between two points of same cluster (DBSCAN)
JSON_ORIENT = "records"

class ClusterLabeler:

    def kmeans(self,
               df: pd.DataFrame) -> str:
        """
        | Cluster data using k-means
        |
        | -----------------------------------------------------------
        | Parameters
        | ----------
        |  df : pd.DataFrame
        |    The data. Two columns with x- and y-coordinates
        |
        |
        | Returns
        | -------
        |  JSON string in JSON_ORIENT format, with fields for original
        |  df columns, and 'cluster'
        """
        x = cluster.KMeans(n_clusters=N_CLUSTERS).fit(df)
        df['cluster'] = x.labels_

        return df.to_json(orient=JSON_ORIENT)

    def gauss(self,
              df: pd.DataFrame) -> str:
        """
        | Cluster data using a Gaussian mixture model
        |
        | -----------------------------------------------------------
        | Parameters
        | ----------
        |  df : pd.DataFrame
        |    The data. Two columns with x- and y-coordinates
        |
        |
        | Returns
        | -------
        |  JSON string in JSON_ORIENT format, with fields for original
        |  df columns, and 'cluster'
        """
        gmm = mixture.GaussianMixture(n_components=N_CLUSTERS)
        gmm.fit(df)
        df['cluster'] = gmm.predict(df)

        return df.to_json(orient=JSON_ORIENT)

    def dbscan(self,
               df: pd.DataFrame,
               eps: Union[int, float] = EPS) -> str:
        """
        | Cluster data using DBSCAN (density-based spatial clustering
        | of applications with noise)
        |
        | -----------------------------------------------------------
        | Parameters
        | ----------
        |  df : pd.DataFrame
        |    The data. Two columns with x- and y-coordinates
        |
        |  eps : int, float
        |    Maximum distance between two points within same cluster
        |
        |
        | Returns
        | -------
        |  JSON string in JSON_ORIENT format, with fields for original
        |  df columns, and 'cluster'
        """
        dbs = cluster.DBSCAN(eps=eps)
        dbs.fit(df)
        df['cluster'] = dbs.labels_

        return df.to_json(orient=JSON_ORIENT)
