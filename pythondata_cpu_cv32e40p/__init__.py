import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/openhwgroup/cv32e40p"

# Module version
version_str = "1.0.1.post1909"
version_tuple = (1, 0, 1, 1909)
try:
    from packaging.version import Version as V
    pversion = V("1.0.1.post1909")
except ImportError:
    pass

# Data version info
data_version_str = "1.0.1.post1764"
data_version_tuple = (1, 0, 1, 1764)
try:
    from packaging.version import Version as V
    pdata_version = V("1.0.1.post1764")
except ImportError:
    pass
data_git_hash = "360d272898d81806be3377193870dbf83a3ea79f"
data_git_describe = "v1.0.1-1764-g360d272"
data_git_msg = """\
commit 360d272898d81806be3377193870dbf83a3ea79f
Merge: 782283a 1079a83
Author: Davide Schiavone <davide@openhwgroup.org>
Date:   Sat Jul 13 09:43:40 2024 +0200

    Merge pull request #1026 from openhwgroup/dev
    
    merge dev into master

"""

# Tool version info
tool_version_str = "0.0.post145"
tool_version_tuple = (0, 0, 145)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post145")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_cv32e40p."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_cv32e40p".format(f))
    return fn
