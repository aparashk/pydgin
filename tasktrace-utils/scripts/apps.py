#! /usr/bin/env python
#============================================================================
# apps
#============================================================================
#
# This file defines the app_list and app_dict:
#
# - app_list: this is the list of apps that will be simulated
# - app_dict: this dictionary contains app options for each simulation group
#
# Here is an example entry for 'bfs' in app_dict:
#
#   'bfs'                 : { 'mt'     : [ '--impl mt --warmup' ],
#                             'mtpull' : [ '--impl mtpull --warmup', ],
#                             'scalar' : [ '--impl scalar --warmup', ] },
#
# This entry describes three groups ('mt', 'mtpull', 'scalar') that
# make it easy to sim entire groups at once in a sim workflow. For
# example, "simdict['app_group'] = ['scalar']" will sim the scalar
# versions of all apps.
#
# Within each group is a list of application options. In this example,
# each app group has only one set of options. If there were multiple,
# each sim would be uniquely labeled (automatically) so that build
# directory names do not conflict.

from doit_pydgin_utils import appdir, appinputdir

#----------------------------------------------------------------------------
# Application List
#----------------------------------------------------------------------------

# Use app_list to specify which of the apps in app_dict to actually sim

app_list = [
  'px-fib',
  'ubmark-vvadd',
  # pbbs apps
  'pbbs-bfs-deterministicBFS-parc-mtpull',
  'pbbs-bfs-ndBFS-parc-mtpull',
  'pbbs-csort-quickSort-parc-mtpull',
  'pbbs-csort-sampleSort-parc-mtpull',
  'pbbs-dict-deterministicHash-parc-mtpull',
  #'pbbs-hull-quickHull-parc-mtpull', -- can't support nested pfor within a task yet
  'pbbs-isort-blockRadixSort-parc-mtpull',
  'pbbs-knn-octTree2Neighbors-parc-mtpull',
  'pbbs-mis-ndMIS-parc-mtpull',
  #'pbbs-nbody-parallelBarnesHut-parc-mtpull',
  'pbbs-rdups-deterministicHash-parc-mtpull',
  'pbbs-sa-parallelRange-parc-mtpull',
  'pbbs-st-ndST-parc-mtpull',
  # cilk apps
  #'cilk-cholesky-parc-mtpull', -- can't build task-graph correctly
  'cilk-cilksort-parc-mtpull',
  'cilk-heat-parc-mtpull',
  #'cilk-knapsack-parc-mtpull',
  'cilk-matmul-parc-mtpull',
]

#----------------------------------------------------------------------------
# Application Dictionary
#----------------------------------------------------------------------------

# Use app_list to specify which of the apps in app_dict to actually sim

app_dict = {

    #........................................................................
    # maven-app-misc
    #........................................................................

    'ubmark-vvadd'        : { 'mtpull' : [ '--impl mtpull', ] },
    'px-fib'              : { 'mtpull' : [ '--impl mt --n 4', ] },
    'bilateral'           : { 'mt'     : [ '--impl mt', ],
                              'mtpull' : [ '--impl mtpull', ],
                              'scalar' : [ '--impl scalar --warmup', ] },

    'dct8x8m'             : { 'mt'     : [ '--impl mt', ],
                              'scalar' : [ '--impl scalar --warmup', ] },

    'dither'              : { 'mt'     : [ '--impl mt', ],
                              'scalar' : [ '--impl scalar --warmup', ] },

    'mriq'                : { 'mt'     : [ '--impl mt', ],
                              'scalar' : [ '--impl scalar --warmup', ] },

    'rgb2cmyk'            : { 'mt'     : [ '--impl mt', ],
                              'mtpull' : [ '--impl mtpull', ],
                              'scalar' : [ '--impl scalar --warmup', ] },

    'sgemm'               : { 'mt'     : [ '--impl mt', ],
                              'mtpull' : [ '--impl mtpull', ],
                              'scalar' : [ '--impl scalar --warmup', ] },

    'strsearch'           : { 'mt'     : [ '--impl mt', ],
                              'mtpull' : [ '--impl mtpull', ],
                              'scalar' : [ '--impl scalar --warmup', ] },

    'uts'                 : { 'mt'     : [ '--impl mt', ],
                              'mtpull' : [ '--impl mtpull', ],
                              'scalar' : [ '--impl scalar', ], },

    'viterbi'             : { 'mt'     : [ '--impl mt', ],
                              'mtpull' : [ '--impl mtpull', ],
                              'scalar' : [ '--impl scalar', ] },

    'ubmark-cmplx-mult'   : { 'mt'     : [ '--impl mt --warmup', ],
                              'mtpull' : [ '--impl mtpull --warmup', ],
                              'scalar' : [ '--impl scalar --warmup', ] },

    'bfs'                 : { 'mt'     : [ '--impl mt --warmup', ],
                              'mtpull' : [ '--impl mtpull --warmup', ],
                              'scalar' : [ '--impl scalar --warmup', ] },

    'kmeans'              : { 'mt'     : [ '--impl mt --warmup', ],
                              'mtpull' : [ '--impl mtpull --warmup', ],
                              'scalar' : [ '--impl scalar --warmup', ] },

    'rsort'               : { 'mt'     : [ '--impl mt --warmup', ],
                              'scalar' : [ '--impl scalar --warmup', ] },

    'ubmark-bin-search'   : { 'mt'     : [ '--impl mt --warmup', ],
                              'scalar' : [ '--impl scalar --warmup', ] },

    'ubmark-masked-filter': { 'mt'     : [ '--impl mt --warmup', ],
                              'scalar' : [ '--impl scalar --warmup', ] },

    'ubmark-grow'         : { 'mt'     : [ '--impl mt --warmup', ],
                              'mtpull' : [ '--impl mtpull --warmup', ],
                              'scalar' : [ '--impl scalar --warmup', ] },

    'ubmark-mugtask'      : { 'mt'     : [ '--impl mt --warmup', ],
                              'mtpull' : [ '--impl mtpull --warmup', ] },

    'ubmark-parallel'     : { 'mt'     : [ '--impl mt --warmup', ],
                              'mtpull' : [ '--impl mtpull --warmup', ],
                              'scalar' : [ '--impl scalar --warmup', ] },

    'ubmark-swap'         : { 'mt'     : [ '--impl mt --warmup', ] },

    'parsec-scluster'     : { 'mt'     : [ '--impl mt --warmup', ],
                              'scalar' : [ '--impl scalar --warmup', ] },

    'splash2-fft'         : { 'mt'     : [ '-p%(num_cpus)s -m8 -n512 -l5', ] },

    'splash2-lu'          : { 'mt'     : [ '-p%(num_cpus)s -n32 -b8', ] },

    #........................................................................
    # pbbs awsteal pruned apps
    #........................................................................

    "pbbs-bfs-deterministicBFS-parc": {
        "small": [
            " " + appinputdir + "/randLocalGraph_J_5_150000",
        ],
        "tiny": [
            " " + appinputdir + "/randLocalGraph_J_5_10000",
        ]
    },
    "pbbs-bfs-deterministicBFS-parc-mtpull": {
        "small": [
            " " + appinputdir + "/randLocalGraph_J_5_150000",
        ],
        "tiny": [
            " " + appinputdir + "/randLocalGraph_J_5_10000",
        ]
    },
    "pbbs-bfs-ndBFS-parc": {
        "small": [
            " " + appinputdir + "/randLocalGraph_J_5_150000",
        ],
        "tiny": [
            " " + appinputdir + "/randLocalGraph_J_5_10000",
        ]
    },
    "pbbs-bfs-ndBFS-parc-mtpull": {
        "small": [
            " " + appinputdir + "/randLocalGraph_J_5_150000",
        ],
        "tiny": [
            " " + appinputdir + "/randLocalGraph_J_5_10000",
        ]
    },
    "pbbs-bfs-serialBFS-parc": {
        "small": [
            " " + appinputdir + "/randLocalGraph_J_5_150000",
        ],
        "tiny": [
            " " + appinputdir + "/randLocalGraph_J_5_10000",
        ]
    },
    "pbbs-csort-quickSort-parc": {
        "small": [
            " " + appinputdir + "/exptSeq_10000_double",
            " " + appinputdir + "/almostSortedSeq_10000_double",
            " " + appinputdir + "/trigramSeq_50000"
        ],
        "tiny": [
            " " + appinputdir + "/exptSeq_1000_double",
            " " + appinputdir + "/almostSortedSeq_1000_double",
            " " + appinputdir + "/trigramSeq_7000"
        ]
    },
    "pbbs-csort-quickSort-parc-mtpull": {
        "small": [
            " " + appinputdir + "/exptSeq_10000_double",
            " " + appinputdir + "/almostSortedSeq_10000_double",
            " " + appinputdir + "/trigramSeq_50000"
        ],
        "tiny": [
            " " + appinputdir + "/exptSeq_1000_double",
            " " + appinputdir + "/almostSortedSeq_1000_double",
            " " + appinputdir + "/trigramSeq_7000"
        ]
    },
    "pbbs-csort-sampleSort-parc": {
        "small": [
            " " + appinputdir + "/exptSeq_10000_double",
            " " + appinputdir + "/almostSortedSeq_10000_double",
            " " + appinputdir + "/trigramSeq_50000"
        ],
        "tiny": [
            " " + appinputdir + "/exptSeq_1000_double",
            " " + appinputdir + "/almostSortedSeq_1000_double",
            " " + appinputdir + "/trigramSeq_7000"
        ]
    },
    "pbbs-csort-sampleSort-parc-mtpull": {
        "small": [
            " " + appinputdir + "/exptSeq_10000_double",
            " " + appinputdir + "/almostSortedSeq_10000_double",
            " " + appinputdir + "/trigramSeq_50000"
        ],
        "tiny": [
            " " + appinputdir + "/exptSeq_1000_double",
            " " + appinputdir + "/almostSortedSeq_1000_double",
            " " + appinputdir + "/trigramSeq_7000"
        ]
    },
    "pbbs-csort-serialSort-parc": {
        "small": [
            " " + appinputdir + "/exptSeq_10000_double",
            " " + appinputdir + "/almostSortedSeq_10000_double",
            " " + appinputdir + "/trigramSeq_50000"
        ],
        "tiny": [
            " " + appinputdir + "/exptSeq_1000_double",
            " " + appinputdir + "/almostSortedSeq_1000_double",
            " " + appinputdir + "/trigramSeq_7000"
        ]
    },
    "pbbs-dict-deterministicHash-parc": {
        "small": [
            " " + appinputdir + "/exptSeq_1000000_int",
        ],
        "tiny": [
            " " + appinputdir + "/exptSeq_100000_int",
        ],
        "test": [
            " " + appinputdir + "/exptSeq_1000_int",
        ]
    },
    "pbbs-dict-deterministicHash-parc-mtpull": {
        "small": [
            " " + appinputdir + "/exptSeq_1000000_int",
        ],
        "tiny": [
            " " + appinputdir + "/exptSeq_100000_int",
        ],
        "test": [
            " " + appinputdir + "/exptSeq_1000_int",
        ]
    },
    "pbbs-dict-serialHash-parc": {
        "small": [
            " " + appinputdir + "/exptSeq_1000000_int",
        ],
        "tiny": [
            " " + appinputdir + "/exptSeq_100000_int",
        ],
        "test": [
            " " + appinputdir + "/exptSeq_1000_int",
        ]
    },
    "pbbs-hull-quickHull-parc": {
        "small": [
            " " + appinputdir + "/2Dkuzmin_100000"
        ],
        "tiny": [
            " " + appinputdir + "/2Dkuzmin_500"
        ]
    },
    "pbbs-hull-quickHull-parc-mtpull": {
        "small": [
            " " + appinputdir + "/2Dkuzmin_100000"
        ],
        "tiny": [
            " " + appinputdir + "/2Dkuzmin_500"
        ]
    },
    "pbbs-hull-serialHull-parc": {
        "small": [
            " " + appinputdir + "/2Dkuzmin_100000"
        ],
        "tiny": [
            " " + appinputdir + "/2Dkuzmin_500"
        ]
    },
    "pbbs-isort-blockRadixSort-parc": {
        "small": [
            " " + appinputdir + "/randomSeq_1000000_int",
            " " + appinputdir + "/exptSeq_500000_int",
        ],
        "tiny": [
            " " + appinputdir + "/randomSeq_40000_int",
            " " + appinputdir + "/exptSeq_25000_int",
        ]
    },
    "pbbs-isort-blockRadixSort-parc-mtpull": {
        "small": [
            " " + appinputdir + "/randomSeq_1000000_int",
            " " + appinputdir + "/exptSeq_500000_int",
        ],
        "tiny": [
            " " + appinputdir + "/randomSeq_40000_int",
            " " + appinputdir + "/exptSeq_25000_int",
        ]
    },
    "pbbs-isort-serialRadixSort-parc": {
        "small": [
            " " + appinputdir + "/randomSeq_1000000_int",
            " " + appinputdir + "/exptSeq_500000_int",
        ],
        "tiny": [
            " " + appinputdir + "/randomSeq_40000_int",
            " " + appinputdir + "/exptSeq_25000_int",
        ]
    },
    "pbbs-knn-octTree2Neighbors-parc": {
        "small": [
            "-d 2 -k 1 " + appinputdir + "/2DinCube_10000",
        ],
        "tiny": [
            "-d 2 -k 1 " + appinputdir + "/2DinCube_100",
        ]
    },
    "pbbs-knn-octTree2Neighbors-parc-mtpull": {
        "small": [
            "-d 2 -k 1 " + appinputdir + "/2DinCube_10000",
        ],
        "tiny": [
            "-d 2 -k 1 " + appinputdir + "/2DinCube_100",
        ]
    },
    "pbbs-knn-serialNeighbors-parc": {
        "small": [
            "-d 2 -k 1 " + appinputdir + "/2DinCube_10000",
        ],
        "tiny": [
            "-d 2 -k 1 " + appinputdir + "/2DinCube_100",
        ]
    },
    "pbbs-mis-ndMIS-parc": {
        "small": [
            " " + appinputdir + "/randLocalGraph_J_5_400000",
        ],
        "tiny": [
            " " + appinputdir + "/randLocalGraph_J_5_5000",
        ]
    },
    "pbbs-mis-ndMIS-parc-mtpull": {
        "small": [
            " " + appinputdir + "/randLocalGraph_J_5_400000",
        ],
        "tiny": [
            " " + appinputdir + "/randLocalGraph_J_5_5000",
        ]
    },
    "pbbs-mis-serialMIS-parc": {
        "medium": [
            " " + appinputdir + "/randLocalGraph_J_5_400000",
            " " + appinputdir + "/rMatGraph_J_5_350000",
            " " + appinputdir + "/3Dgrid_J_600000"
        ],
        "small": [
            " " + appinputdir + "/randLocalGraph_J_5_400000",
        ],
        "tiny": [
            " " + appinputdir + "/randLocalGraph_J_5_5000",
        ]
    },
    "pbbs-mm-ndMatching-parc": {
        "small": [
            " " + appinputdir + "/randLocalGraph_E_5_400000",
        ],
        "tiny": [
            " " + appinputdir + "/randLocalGraph_E_5_20000",
        ]
    },
    "pbbs-mm-ndMatching-parc-mtpull": {
        "small": [
            " " + appinputdir + "/randLocalGraph_E_5_400000",
        ],
        "tiny": [
            " " + appinputdir + "/randLocalGraph_E_5_20000",
        ]
    },
    "pbbs-mm-serialMatching-parc": {
        "small": [
            " " + appinputdir + "/randLocalGraph_E_5_400000",
        ],
        "tiny": [
            " " + appinputdir + "/randLocalGraph_E_5_20000",
        ]
    },
    "pbbs-nbody-serialBarnesHut-parc": {
        "small": [
            " " + appinputdir + "/3DinCube_1000",
        ],
        "tiny": [
            " " + appinputdir + "/3DinCube_20",
        ]
    },
    "pbbs-nbody-parallelBarnesHut-parc": {
        "small": [
            " " + appinputdir + "/3DinCube_1000",
        ],
        "tiny": [
            " " + appinputdir + "/3DinCube_20",
        ]
    },
    "pbbs-nbody-parallelBarnesHut-parc-mtpull": {
        "small": [
            " " + appinputdir + "/3DinCube_1000",
        ],
        "tiny": [
            " " + appinputdir + "/3DinCube_20",
        ]
    },
    "pbbs-rdups-deterministicHash-parc": {
        "small": [
            " " + appinputdir + "/trigramSeq_300000_pair_int"
        ],
        "tiny": [
            " " + appinputdir + "/trigramSeq_30000_pair_int"
        ]
    },
    "pbbs-rdups-deterministicHash-parc-mtpull": {
        "small": [
            " " + appinputdir + "/trigramSeq_300000_pair_int"
        ],
        "tiny": [
            " " + appinputdir + "/trigramSeq_30000_pair_int"
        ]
    },
    "pbbs-rdups-serialHash-parc": {
        "small": [
            " " + appinputdir + "/trigramSeq_300000_pair_int"
        ],
        "tiny": [
            " " + appinputdir + "/trigramSeq_30000_pair_int"
        ]
    },
    "pbbs-sa-parallelRange-parc": {
        "small": [
            " " + appinputdir + "/trigramString_200000"
        ],
        "tiny": [
            " " + appinputdir + "/trigramString_20000"
        ]
    },
    "pbbs-sa-parallelRange-parc-mtpull": {
        "small": [
            " " + appinputdir + "/trigramString_200000"
        ],
        "tiny": [
            " " + appinputdir + "/trigramString_20000"
        ]
    },
    "pbbs-sa-serialKS-parc": {
        "small": [
            " " + appinputdir + "/trigramString_200000"
        ],
        "tiny": [
            " " + appinputdir + "/trigramString_20000"
        ]
    },
    "pbbs-st-ndST-parc": {
        "small": [
            " " + appinputdir + "/randLocalGraph_E_5_100000",
        ],
        "tiny": [
            " " + appinputdir + "/randLocalGraph_E_5_10000",
        ]
    },
    "pbbs-st-ndST-parc-mtpull": {
        "small": [
            " " + appinputdir + "/randLocalGraph_E_5_100000",
        ],
        "tiny": [
            " " + appinputdir + "/randLocalGraph_E_5_10000",
        ]
    },
    "pbbs-st-serialST-parc": {
        "small": [
            " " + appinputdir + "/randLocalGraph_E_5_100000",
        ],
        "tiny": [
            " " + appinputdir + "/randLocalGraph_E_5_10000",
        ]
    },

    #........................................................................
    # cilk awsteal pruned apps
    #........................................................................

   "cilk-cholesky-parc": {
        "small": [
            "-n 128 -z 256 ",
        ],
        "tiny": [
            "-n 128 -z 173 "
        ]
    },
    "cilk-cholesky-parc-mtpull": {
        "small": [
            "-n 128 -z 256 ",
        ],
        "tiny": [
            "-n 64 -z 128 "
        ]
    },
    "cilk-cilksort-parc": {
        "small": [
            "-n 300000 "
        ],
        "tiny": [
            "-n 50000 "
        ]
    },
    "cilk-cilksort-parc-mtpull": {
        "small": [
            "-n 300000 "
        ],
        "tiny": [
            "-n 50000 "
        ]
    },
    "cilk-heat-parc": {
        "small": [
            "-g 1 -nx 256 -ny 64 -nt 1 "
        ],
        "tiny": [
            "-g 1 -nx 64 -ny 8 -nt 4 "
        ]
    },
    "cilk-heat-parc-mtpull": {
        "small": [
            "-g 1 -nx 256 -ny 64 -nt 1 "
        ],
        "tiny": [
            "-g 1 -nx 64 -ny 8 -nt 4 "
        ]
    },
    "cilk-knapsack-parc": {
        "small": [
            "-f /work/global/ss2783/github/awsteal-new-apps/cilk-knapsack/inputs/knapsack-small-1.input ",
        ],
        "tiny": [
            "-f /work/global/ss2783/github/awsteal-new-apps/cilk-knapsack/inputs/knapsack-example1.input "
        ]
    },
    "cilk-knapsack-parc-mtpull": {
        "small": [
            "-f /work/global/ss2783/github/awsteal-new-apps/cilk-knapsack/inputs/knapsack-small-1.input ",
        ],
        "tiny": [
            "-f /work/global/ss2783/github/awsteal-new-apps/cilk-knapsack/inputs/knapsack-example1.input "
        ]
    },
    "cilk-lu-parc": {
        "small": [
            "-n 64 "
        ],
        "tiny": [
            "-n 32 "
        ]
    },
    "cilk-lu-parc-mtpull": {
        "small": [
            "-n 64 "
        ],
        "tiny": [
            "-n 32 "
        ]
    },
    "cilk-matmul-parc": {
        "small": [
            "200 "
        ],
        "tiny": [
            "95 "
        ]
    },
    "cilk-matmul-parc-mtpull": {
        "small": [
            "200 "
        ],
        "tiny": [
            "95 "
        ]
    },
    "parsec-blackscholes-serial-parc": {
        "small": [
            "8 /work/global/ss2783/github/awsteal-new-apps/parsec-blackscholes/inputs/in_16.txt dummy.output "
        ],
        "tiny": [
            "8 /work/global/ss2783/github/awsteal-new-apps/parsec-blackscholes/inputs/in_4.txt dummy.output "
        ]
    },
    "parsec-blackscholes-parc": {
        "small": [
            "8 /work/global/ss2783/github/awsteal-new-apps/parsec-blackscholes/inputs/in_16.txt dummy.output "
        ],
        "tiny": [
            "8 /work/global/ss2783/github/awsteal-new-apps/parsec-blackscholes/inputs/in_4.txt dummy.output "
        ]
    },
    "parsec-blackscholes-parc-mtpull": {
        "small": [
            "8 /work/global/ss2783/github/awsteal-new-apps/parsec-blackscholes/inputs/in_16.txt dummy.output "
        ],
        "tiny": [
            "8 /work/global/ss2783/github/awsteal-new-apps/parsec-blackscholes/inputs/in_4.txt dummy.output "
        ]
    },
    "parsec-swaptions-serial-parc": {
        "small": [
            "-ns 8 -sm 1 -nt 8 "
        ]
    },
    "parsec-swaptions-parc": {
        "small": [
            "-ns 8 -sm 1 -nt 8 "
        ]
    },
    "parsec-swaptions-parc-mtpull": {
        "small": [
            "-ns 8 -sm 1 -nt 8 "
        ]
    },
}