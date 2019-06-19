# パッケージとモジュールの読み込み

# import from a module
import my_module
my_module.get_genius()
my_module.get_popular()

import my_module as mm
mm.get_genius()
mm.get_popular()

from my_module import get_genius
get_genius()

#*************************************************************************

# import from a package
import gscommon.my_module
gscommon.my_module.get_genius()

from gscommon import my_module
my_module.get_genius()

import gscommon
gscommon.my_module.get_genius()








