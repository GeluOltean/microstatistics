import os
from math import ceil
from matplotlib import pyplot as plt
from matplotlib.ticker import MaxNLocator
from matplotlib.ticker import AutoMinorLocator
from scipy.cluster import hierarchy as hc
from scipy.spatial import distance as dist
from sklearn.manifold import MDS
from pandas import DataFrame

from microstatistics.util.diversities import *

plt.style.use("seaborn-whitegrid")
plt.rcParams['pdf.fonttype'] = 42
plt.rcParams['ps.fonttype'] = 42
plt.rcParams['svg.fonttype'] = 'none'


class GraphingService(object):
    def __init__(self):
        self.df: DataFrame = DataFrame([])
        self.sample_labels: list = []
        self.species_labels: list = []
        self.save_location: str = ""

    def graph_index(self, lst: list, title: str):
        plt.figure(dpi=200, figsize=(3, 12))
        yaxis = [x + 1 for x in range(len(lst))]
        plt.plot(lst, yaxis)
        plt.title(title)
        plt.gca().yaxis.set_major_locator(MaxNLocator(integer=True))
        plt.gca().set_ylim(1, len(yaxis))
        plt.gca().set_xlim(0, max(lst) * 1.5)
        plt.yticks(yaxis, self.sample_labels)
        plt.ylabel("Sample number")
        plt.fill_betweenx(yaxis, lst)

        save_name = f"/{title}.svg"
        plt.savefig(self.save_location + save_name)
        plt.close()

    def graph_percentages(self, index: int, title: str):
        holder = self.df_proportion(self.df.copy())
        holder = holder.replace(np.nan, 0)
        plt.figure(dpi=200, figsize=(3, 12))
        yaxis = [x + 1 for x in range(len(holder.T))]
        plt.title(title)
        plt.gca().yaxis.set_major_locator(MaxNLocator(integer=True))
        plt.gca().set_ylim(1, len(yaxis))
        plt.gca().set_xlim(0, 100)
        plt.yticks(yaxis, self.sample_labels)
        plt.plot(holder.iloc[index], yaxis)
        plt.ylabel("Sample number")
        plt.fill_betweenx(yaxis, holder.iloc[index])

        save_name = f"/{title}.svg"
        plt.savefig(self.save_location + save_name)
        plt.close()

    def graph_morphogroups(self):
        holder = self.df_proportion(self.df.copy())
        holder = holder.transpose() * 100
        morphogroups = ('M1', 'M2a', 'M2b', 'M2c', 'M3a', 'M3b', 'M3c', 'M4a',
                        'M4b')

        global_max = max(holder.max().values)
        yaxis = [x + 1 for x in range(len(holder[1]))]

        if not os.path.isdir(self.save_location + "/morphogroups"):
            os.mkdir(self.save_location + "/morphogroups")
        save_location_morphs = self.save_location + "/morphogroups"

        morphogroup_dict = {}
        for i in range(len(morphogroups)):
            morphogroup_dict[morphogroups[i]] = holder.T.values[i]

        for k in morphogroup_dict:
            # ensure the same scale
            local_size = 5 if max(morphogroup_dict[k]) < 5 else max(morphogroup_dict[k])
            local_max = ((local_size * 100) / global_max) / 100

            plt.figure(dpi=300, figsize=[local_max * 3, 12])
            plt.plot(morphogroup_dict[k], yaxis)
            plt.title(k)
            plt.gca().set_xlim(0)
            if ceil(max(morphogroup_dict[k])) < 5:
                plt.gca().set_xlim(0, 5)
            else:
                plt.gca().set_xlim(0)
            plt.gca().set_ylim(1, len(yaxis))
            plt.gca().xaxis.set_minor_locator(AutoMinorLocator(n=5))
            plt.gca().yaxis.set_major_locator(MaxNLocator(integer=True))
            plt.yticks(yaxis, self.sample_labels)
            plt.fill_betweenx(yaxis, morphogroup_dict[k])
            plt.savefig(save_location_morphs + f"/{k}.svg")
            plt.close(k)

    def graph_epi_inf_detailed(self):
        """Represents the epifaunal to infaunal proportions by displaying foram
        proportions by their respective environment. Requires a dataframe object
        as input. """
        frame = self.df.copy()
        holder = self.df_proportion(frame) * 100
        # holder.iloc[0] gets the first row
        epifaunal = holder.iloc[0]
        inf_shallow = holder.iloc[1] + epifaunal
        inf_deep = holder.iloc[2] + inf_shallow
        inf_undetermined = holder.iloc[3] + inf_deep

        plt.figure(dpi=200, figsize=(3, 12))
        yaxis = [x + 1 for x in range(len(holder.T))]
        plt.title("Detailed Epifaunal to Infaunal proportions")
        plt.ylabel("Sample number")
        plt.xlabel("Percentage")

        plt.plot(epifaunal, yaxis, '#52A55C', label='Epifaunal')
        plt.plot(inf_shallow, yaxis, '#236A62', label='Inf. Shallow')
        plt.plot(inf_deep, yaxis, '#2E4372', label='Inf. Deep')
        plt.plot(inf_undetermined, yaxis, '#535353', label='Inf. Undetermined')

        plt.fill_betweenx(yaxis, epifaunal, facecolor='#52A55C')
        plt.fill_betweenx(yaxis, epifaunal, inf_shallow, facecolor='#236A62')
        plt.fill_betweenx(yaxis, inf_shallow, inf_deep, facecolor='#2E4372')
        plt.fill_betweenx(yaxis, inf_deep, inf_undetermined, facecolor='#535353')

        plt.gca().yaxis.set_major_locator(MaxNLocator(integer=True))
        plt.yticks(yaxis)
        plt.gca().set_xlim(0, 100)
        plt.gca().set_ylim(1, len(yaxis))

        plt.subplot(111).legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),
                                fancybox=True, shadow=True, ncol=5, borderaxespad=2)

        save_name = "/Detailed Epi-Infaunal.svg"
        plt.savefig(self.save_location + save_name)

        # MULTIVARIATE INDICES

    def graph_sample_dendrogram(self):
        frame = self.df.copy()
        label = list(range(1, len(frame.T) + 1))
        sample_distance = dist.pdist(frame.T, metric="braycurtis")
        plt.figure(dpi=500)
        linkage = hc.linkage(sample_distance, method="average")
        hc.dendrogram(linkage, labels=label)
        plt.suptitle("R-mode Dendrogram (Bray-Curtis)")

        save_name = "/R-mode Dendrogram.svg"
        plt.savefig(self.save_location + save_name)

    def graph_species_dendrogram(self):
        frame = self.df.copy()
        label = list(range(1, len(frame) + 1))
        species_distance = dist.pdist(frame, metric="braycurtis")
        plt.figure(dpi=800)
        linkage = hc.linkage(species_distance, method="average")
        hc.dendrogram(linkage, orientation="left", labels=label)
        plt.suptitle("Q-mode Dendrogram (Bray-Curtis)")

        save_name = "/Q-mode Dendrogram.svg"
        plt.savefig(self.save_location + save_name)

    def graph_nmds(self, frame, dim, runs, saveloc: str, labels: list):
        sample_distance = dist.pdist(frame.T, metric="braycurtis")
        square_dist = dist.squareform(sample_distance)

        nmds = MDS(n_components=dim, metric=False, dissimilarity="precomputed",
                   max_iter=runs, n_init=30)
        pos = nmds.fit(square_dist).embedding_
        stress = nmds.fit(square_dist).stress_

        pos0 = pos[:, 0].tolist()
        pos1 = pos[:, 1].tolist()
        fig, ax = plt.subplots()
        ax.scatter(pos0, pos1)
        for i, x in enumerate(labels):
            ax.annotate(x, (pos0[i], pos1[i]))
        fig.suptitle("nMDS (Bray-Curtis)")
        ax.set_title(f"Stress = {str(stress)}")

        save_name = "/nMDS.svg"
        plt.savefig(self.save_location + save_name)

    def df_proportion(self):
        holder = self.df.copy()
        for i in range(len(holder.T)):
            holder[i] = holder[i].apply(lambda x: x if x == 0 else x / holder[i].sum())
        return holder

    def df_bfoi(self, frame: DataFrame):
        results = []
        holder = frame.copy()
        for i in range(len(holder.T)):
            oxic = holder[i][1]
            disoxic = holder[i][2]
            suboxic = holder[i][3]
            if oxic == 0:
                bfoi = 50 * (suboxic / (disoxic + suboxic) - 1)
            else:
                bfoi = 100 * oxic / (oxic + disoxic)
            results.append(bfoi)
        return results
