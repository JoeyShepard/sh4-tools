#!/usr/bin/env python3

from tests.tests_util import *
from color import *

import tests.tests_sh4_disasm
do_tests("sh4_disasm",tests.tests_sh4_disasm.test_list)

import tests.tests_sh4_asm
do_tests("sh4_asm",tests.tests_sh4_asm.test_list)
