"""Design class: read the toml config file, variables easy to access
    """
from pathlib import Path
import tomllib as toml


class Config:
    """Configuration for ngspice session:
    Reads config.toml (whatever is the name of your toml file)
    provides path to ngspice executable
    provides the design directories and names
    """

    def __init__(self, config_file: Path, design: str) -> None:

        self.fred = config_file.read_text()
        with open(config_file, "rb") as _:
            self.config = toml.load(_)
        self.design = design

        self.ngspice_bin: str = self.config["executable"]["ngspice_bin"]
        self.ngspice_exe_file: str = self.config["executable"]["ngspice_exe_file"]
        # ngspice executable with full path
        self.ngspice_exe: Path = Path(self.ngspice_bin) / self.ngspice_exe_file

        # project path absolute
        self.project_abs: Path = Path(self.config[self.design]["project_abs"])
        self.project_rel: Path = Path(self.config[self.design]["project_rel"])

        # # project path (full)
        # self.project: Path = Path(self.config[self.design]["project"])

        # # relative path (with regards to project path) to netlists
        # self.netlists: Path = Path(self.config[self.design]["netlists"])

        # # relative path (with regards to project path) to results
        # self.results: Path = Path(self.config[self.design]["results"])

        # # name of netlist file
        # self.netlist_file: str = self.config[self.design]["netlist_file"]
        # self.netlist_filename: Path = self.netlists / self.netlist_file

        # # name of control file
        # self.cntl_file: str = self.config[self.design]["cntl_file"]
        # self.cntl_filename: Path = self.netlists / self.cntl_file
