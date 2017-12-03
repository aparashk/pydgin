#! /usr/bin/env python
#============================================================================
# dodo
#============================================================================
# Template dodo file with reporter that outputs task actions as strings.
#
# Author : Shreesha Srinath
# Date   : September 16th, 2017

from doit.task  import clean_targets
from doit.tools import check_timestamp_unchanged
from doit.tools import create_folder

from apps import *
from doit_utils import *
from doit_pydgin_utils import *

#----------------------------------------------------------------------------
# Config
#----------------------------------------------------------------------------

DOIT_CONFIG = {
  'reporter' : MyReporter,
}

#----------------------------------------------------------------------------
# Tasks
#----------------------------------------------------------------------------

def task_pydgin_sims_wsrt():

  evaldict = get_base_evaldict()

  evaldict['basename']    = "sim-pydgin-wsrt"
  evaldict['resultsdir']  = "results-tiny-wsrt"
  evaldict['doc']         = os.path.basename(__file__).rstrip('c')

  evaldict['app_group']   = ["tiny","mtpull"]
  evaldict['app_list']    = app_list
  evaldict['app_dict']    = app_dict

  yield gen_trace_per_app( evaldict )

def task_pydgin_sims_spmd():

  evaldict = get_base_evaldict()

  evaldict['basename']    = "sim-pydgin-spmd"
  evaldict['resultsdir']  = "results-small-spmd"
  evaldict['doc']         = os.path.basename(__file__).rstrip('c')

  evaldict['app_group']   = ["small","mt"]
  evaldict['app_list']    = app_list_spmd
  evaldict['app_dict']    = app_dict

  yield gen_trace_per_app( evaldict )
