const URLS = {
    data: {
        blobs: "/data/blobs",
        moons: "/data/moons",
        rings: "/data/rings",
        uniform: "/data/uniform"
    },
    algo: {
        kmeans: "/cluster/kmeans",
        gauss: "/cluster/gauss",
        dbscan: "/cluster/dbscan"
    }
};

const ALGO_NAMES = {
    kmeans: "k-means",
    gauss: "Gaussian Mixture Model",
    dbscan: "DBSCAN"
};

// More than two in case algo thinks there's more
const colors = ['orange', 'purple', 'red', 'green'];
const names = ['A', 'B', 'C', 'D'];
