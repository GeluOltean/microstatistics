import numpy as np
import os
from math import ceil
from matplotlib import pyplot as plt
from matplotlib.ticker import MaxNLocator
from matplotlib.ticker import AutoMinorLocator
from .diversities import dfProportion
from scipy.cluster import hierarchy as hc
from scipy.spatial import distance as dist
from sklearn.manifold import MDS

plt.style.use("seaborn-whitegrid")
plt.rcParams['pdf.fonttype'] = 42
plt.rcParams['ps.fonttype'] = 42
plt.rcParams['svg.fonttype'] = 'none'

def graphIndex(lst, title: str, saveloc: str, labels: list):
	"""Represents the list resulted from the calculation of an index. Requires
	an iterable collection and a title as input."""
	holder = lst
	plt.figure(dpi = 200, figsize=(3,12))
	yaxis = [x+1 for x in range(len(holder))]
	plt.plot(holder, yaxis)
	plt.title(title)
	plt.gca().yaxis.set_major_locator(MaxNLocator(integer=True))
	plt.gca().set_ylim(1, len(yaxis))
	plt.gca().set_xlim(0, max(holder)*1.5)
	plt.yticks(yaxis, labels)
	plt.ylabel("Sample number")
	plt.fill_betweenx(yaxis, holder)

	savename = f"/{title}.svg"
	plt.savefig(saveloc + savename)

def graphPercentages(frame, index, title: str, saveloc: str, labels: list):
	"""Represents a row from a dataframe (a chosen species) by their proportion
	in a sample (column). Requires a dataframe object, an index, and a title as
	input. """
	holder = dfProportion(frame) * 100
	holder = holder.replace(np.nan, 0)
	plt.figure(dpi = 200, figsize=(3,12))
	yaxis = [x+1 for x in range(len(holder.T))]
	plt.title(title)
	plt.gca().yaxis.set_major_locator(MaxNLocator(integer=True))
	plt.gca().set_ylim(1, len(yaxis))
	plt.gca().set_xlim(0, 100)
	plt.yticks(yaxis, labels)
	plt.plot(holder.iloc[index], yaxis)
	plt.ylabel("Sample number")
	plt.fill_betweenx(yaxis, holder.iloc[index])

	# savename = "/" + f"Abundance of species on row {index+2}" + ".svg"
	savename = f"/{title}.svg"
	plt.savefig(saveloc + savename)

def graphMorphogroups(frame, saveloc: str, labels: list):
	"""Represents the proportion of each morphogroup, displaying foram
	distribution by morphogroup. Requires a dataframe object as input."""
	holder = dfProportion(frame.copy())
	holder = holder.transpose() * 100
	morphogroups = ('M1', 'M2a', 'M2b', 'M2c', 'M3a', 'M3b', 'M3c', 'M4a',
	'M4b')

	globalMax = max(holder.max().values)
	yaxis = [x + 1 for x in range(len(holder[1]))]

	if (not os.path.isdir(saveloc + "/morphogroups")):
		os.mkdir(saveloc + "/morphogroups")
	saveLocationMorphs = saveloc + "/morphogroups"

	morphoDict = {}
	for i in range(len(morphogroups)):
		morphoDict[morphogroups[i]] = holder.T.values[i]

	for k in morphoDict:
		# ensure the same scale
		localSize = 5 if max(morphoDict[k]) < 5 else max(morphoDict[k])
		localMax = ((localSize * 100) / globalMax) / 100

		plt.figure(dpi=300, figsize=[localMax * 3, 12])
		plt.plot(morphoDict[k], yaxis)
		plt.title(k)
		plt.gca().set_xlim(0)
		if (ceil(max(morphoDict[k])) < 5):
			plt.gca().set_xlim(0, 5)
		else:
			plt.gca().set_xlim(0)
		plt.gca().set_ylim(1, len(yaxis))
		plt.gca().xaxis.set_minor_locator(AutoMinorLocator(n=5))
		plt.gca().yaxis.set_major_locator(MaxNLocator(integer=True))
		plt.yticks(yaxis, labels)
		plt.fill_betweenx(yaxis, morphoDict[k])
		plt.savefig(saveLocationMorphs+f"/{k}.svg")
		plt.close(k)

def graphEpiInfDetailed(frame, saveloc: str):
	"""Represents the epifaunal to infaunal proportions by displaying foram
	proportions by their respective environment. Requires a dataframe object
	as input. """
	holder = dfProportion(frame) * 100
	# holder.iloc[0] gets the first row
	epifaunal = holder.iloc[0]
	infShallow = holder.iloc[1] + epifaunal
	infDeep = holder.iloc[2] + infShallow
	infUndetermined = holder.iloc[3] + infDeep

	plt.figure(dpi = 200, figsize = (3,12))
	yaxis = [x+1 for x in range(len(holder.T))]
	plt.title("Detailed Epifaunal to Infaunal proportions")
	plt.ylabel("Sample number")
	plt.xlabel("Percentage")

	plt.plot(epifaunal, yaxis, '#52A55C', label='Epifaunal')
	plt.plot(infShallow, yaxis, '#236A62', label='Inf. Shallow')
	plt.plot(infDeep, yaxis, '#2E4372', label='Inf. Deep')
	plt.plot(infUndetermined, yaxis, '#535353', label='Inf. Undetermined')

	plt.fill_betweenx(yaxis, epifaunal, facecolor='#52A55C')
	plt.fill_betweenx(yaxis, epifaunal, infShallow, facecolor='#236A62')
	plt.fill_betweenx(yaxis, infShallow, infDeep, facecolor='#2E4372')
	plt.fill_betweenx(yaxis, infDeep, infUndetermined, facecolor='#535353')

	plt.gca().yaxis.set_major_locator(MaxNLocator(integer=True))
	plt.yticks(yaxis)
	plt.gca().set_xlim(0, 100)
	plt.gca().set_ylim(1, len(yaxis))

	plt.subplot(111).legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),
          fancybox=True, shadow=True, ncol=5, borderaxespad=2)

	savename = "/Detailed Epi-Infaunal.svg"
	plt.savefig(saveloc + savename)

##### MULTIVARIATE INDICES #####

def graphSampleDendrogram(frame, saveloc: str, labels: list):
	labl = list(range(1, len(frame.T)+1))
	sampleDistance = dist.pdist(frame.T, metric="braycurtis")
	plt.figure(dpi=500)
	linkage = hc.linkage(sampleDistance, method="average")
	dendrog = hc.dendrogram(linkage, labels=labl)
	plt.suptitle("R-mode Dendrogram (Bray-Curtis)")

	savename = "/R-mode Dendrogram.svg"
	plt.savefig(saveloc + savename)

def graphSpeciesDendrogram(frame, saveloc: str):
	labl = list(range(1, len(frame)+1))
	speciesDistance = dist.pdist(frame, metric="braycurtis")
	plt.figure(dpi=800)
	linkage = hc.linkage(speciesDistance, method="average")
	dendrog = hc.dendrogram(linkage, orientation="left", labels=labl)
	plt.suptitle("Q-mode Dendrogram (Bray-Curtis)")

	savename = "/Q-mode Dendrogram.svg"
	plt.savefig(saveloc + savename)

def graphNMDS(frame, dim, runs, saveloc: str, labels: list):
	# labl = list(range(1, len(frame.T)+1))
	sampleDistance = dist.pdist(frame.T, metric="braycurtis")
	squareDist = dist.squareform(sampleDistance)

	nmds = MDS(n_components=dim, metric=False, dissimilarity="precomputed",
	max_iter=runs, n_init=30)
	pos = nmds.fit(squareDist).embedding_
	stress = nmds.fit(squareDist).stress_

	pos0 = pos[:,0].tolist()
	pos1 = pos[:,1].tolist()
	fig, ax = plt.subplots()
	ax.scatter(pos0, pos1)
	for i, x in enumerate(labels):
		ax.annotate(x, (pos0[i], pos1[i]))
	fig.suptitle("nMDS (Bray-Curtis)")
	ax.set_title(f"Stress = {str(stress)}")

	savename = "/nMDS.svg"
	plt.savefig(saveloc + savename)
