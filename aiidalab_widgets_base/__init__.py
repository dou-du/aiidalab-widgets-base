"""Reusable widgets for AiiDA lab applications."""
# pylint: disable=unused-import,wrong-import-position
from aiida import load_profile
load_profile()

from .codes import CodeDropdown, AiiDACodeSetup, valid_aiidacode_args
from .computers import SshComputerSetup, valid_sshcomputer_args
from .computers import AiidaComputerSetup, valid_aiidacomputer_args
from .computers import ComputerDropdown
from .databases import CodQueryWidget
from .export import ExportButtonWidget
from .process import ProcessFollowerWidget, ProgressBarWidget, RunningCalcJobOutputWidget, SubmitButtonWidget
from .structures import StructureManagerWidget
from .structures import StructureBrowserWidget, StructureExamplesWidget, StructureUploadWidget, SmilesWidget
from .structures import BasicStructureEditor
from .structures_multi import MultiStructureUploadWidget
from .viewers import viewer

__version__ = "1.0.0b5"
