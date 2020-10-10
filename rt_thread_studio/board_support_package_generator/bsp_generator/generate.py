import os
import shutil
import tkinter as tk
from pathlib import Path
from tkinter import filedialog
import pathlib
from . import bsp_descriptor
from . import builtin_files
from . import external_files
from . import project


class Generator(object):
    """
    This is the project generator class, it contains the basic parameters and methods in all type of projects
    """

    def __init__(self):
        self.project_type = "rt-thread"
        self.project_sub_type = "full"
        self.rtt_version = None

    def generate_bsp(self):
        bsp_name = input("Step 0: 请输入开发板支持包名称:\n>")

        bsp_location = input("Step 1: 请输入开发板支持包的存储位置（如果希望使用图形界面选择，请直接点击 Enter 键）\n>")
        if bsp_location.strip() == '':
            root = tk.Tk()
            root.withdraw()
            bsp_location = filedialog.askdirectory()
            print(bsp_location)
        bsp_root_path = Path(bsp_location).joinpath(bsp_name)
        os.mkdir(bsp_root_path)
        new_bsp_descriptor = bsp_descriptor.BspDescriptor()

        project_root_path = input(
            "Step 2: 请选择一个 RT-Studio 工程（如果希望使用图形界面选择，请直接点击 Enter 键）\n>")
        if project_root_path.strip() == '':
            root = tk.Tk()
            root.withdraw()
            project_root_path = filedialog.askdirectory()

        if "rt-thread" in os.listdir(project_root_path):
            use_external_rtt_code = input("Step 3: 探测到这是一个 rt-thread 工程，是否移除工程内 rt-thread 源代码并添加对 rt-thread 源代码依赖信息 ? [Y/n]\n>")
            if "n" in use_external_rtt_code.lower():
                is_use_external_rtt_code = False
            else:
                is_use_external_rtt_code = True
        else:
            is_use_external_rtt_code = False
            self.project_type = "bare-metal"
            self.project_sub_type = "notUsed"
            self.rtt_version = "notUsed"
        if is_use_external_rtt_code:
            rtt_package = input("""Step 4: 请选择该工程使用的 rt-thread 版本 [0/1/2]:
        rt-thread 4.0.2  ------------------- 0
        rt-thread latest ------------------- 1
        rt-thread nano   ------------------- 2
>""")
            if rtt_package == "0":
                self.project_type = "rt-thread"
                self.project_sub_type = "full"
                self.rtt_version = "4.0.2"
            elif rtt_package == "1":
                self.project_type = "rt-thread"
                self.project_sub_type = "full"
                self.rtt_version = "latest"
            elif rtt_package == "0":
                self.project_type = "rt-thread"
                self.rtt_version = "nano-v3.1.3"
                self.project_sub_type = "nano"
        else:
            print("Step 4: 跳过.\n")
        temp_yaml = pathlib.Path(__file__).parent.parent/'template/temp.yaml'
        Generator.cp_fr_list(["debug","documents"], pathlib.Path(__file__).parent.parent/'template',
                             bsp_root_path)
        new_bsp_descriptor.load(temp_yaml)
        new_bsp_descriptor.template_projects.clear()
        new_bsp_descriptor.example_projects.clear()

        project1 = project.Project()
        builtin_files1 = builtin_files.BuiltinFiles()


        builtin_files1.source_path_offset = "rtt_default_project_0"
        builtin_files1.target_path_offset = ""
        builtin_files1.files_and_folders.extend(os.listdir(project_root_path))
        project1.builtin_files.append(builtin_files1.dump())
        project1.project_type= self.project_type+"|@"+self.project_sub_type+"|@"+self.rtt_version
        if is_use_external_rtt_code:
            print(project_root_path)
            builtin_files1.files_and_folders.remove("rt-thread")
            print(builtin_files1.files_and_folders)
        else:
            pass

        if ".git" in builtin_files1.files_and_folders:
            builtin_files1.files_and_folders.remove(".git")
        Generator.cp_fr_list(builtin_files1.files_and_folders, Path(project_root_path),
                             bsp_root_path.joinpath(builtin_files1.source_path_offset))
        if is_use_external_rtt_code:
            external_files2 = external_files.ExternalFiles()
            external_files2.package_type = "RT-Thread_Source_Code"
            external_files2.package_name = "RT-Thread"
            external_files2.package_vendor = ""
            external_files2.package_version = self.rtt_version
            if self.rtt_version == "latest":
                external_files2.source_path_offset = "rt-thread"
            else:
                external_files2.source_path_offset = ""
            external_files2.target_path_offset = "rt-thread"
            external_files2.files_and_folders = ["components",
                                                 "include",
                                                 "libcpu/arm",
                                                 "libcpu/Kconfig",
                                                 "libcpu/SConscript",
                                                 "src",
                                                 "tools",
                                                 "Kconfig",
                                                 "LICENSE"]

            project1.external_files.append(external_files2.dump())
        new_bsp_descriptor.template_projects.append(project1.dump())

        pkg_vendor = input("Step 5: 请输入您的公司名称，如果希望使用默认值（RealThread），请直接点击 Enter 键。\n>")
        if pkg_vendor.strip() == '':
            pkg_vendor = "RealThead"
        else:
            pkg_vendor = pkg_vendor.strip()
        new_bsp_descriptor.pkg_vendor = pkg_vendor

        board_name = input("Step 6: 请输入开发板的名称，如果希望使用默认值（STM32L475-ATK-PANDORA），请直接点击 Enter 键。\n>")
        if board_name.strip() == '':
            board_name = "STM32L475-ATK-PANDORA"
        else:
            board_name = board_name.strip()
        new_bsp_descriptor.board.name = board_name

        dvendor = input("Step 7: 请输入板载 MCU 的厂商名称，如果希望使用默认值（STMicroelectronics），请直接点击 Enter 键。\n>")
        if dvendor.strip() == '':
            dvendor = "STMicroelectronics"
        else:
            dvendor = dvendor.strip()
        new_bsp_descriptor.board.vendor = dvendor

        new_bsp_descriptor.price_cn = "238.00 CNY"
        new_bsp_descriptor.price_global = "35.00 USD"
        new_bsp_descriptor.debugger = "QEMU"
        new_bsp_descriptor.debug_interface = "SWD"

        new_bsp_descriptor.dump(Path(bsp_root_path).joinpath(bsp_name + ".yaml"))
        print("Step 8: 完成.\n开发板支持包位于 : ", str(Path(bsp_root_path)))
        print("""\n以下信息需要手动完善
* 修改yaml文件内的详细信息，包含价格，销售链接，图片位置等
* 开发板的图片信息，默认位置在documents/images/ 文件夹下
* 开发板和 mcu 的文档信息，默认位置在documents下
        """)

    @staticmethod
    def rm_fr_list(item_list, dst_path):
        for item_path in item_list:
            dst_item_path = str(dst_path.joinpath(item_path))
            dst_item_path = dst_item_path.replace('\\', '/')
            dst_item_path = Path(dst_item_path)
            if dst_item_path.exists():
                if Path.is_dir(dst_item_path):
                    shutil.rmtree(dst_item_path)
                else:
                    os.remove(dst_item_path)

    @staticmethod
    def mv_fr_list(item_list, src_path, dst_path):
        for item_path in item_list:
            src_item_path = str(src_path.joinpath(item_path))
            dst_item_path = str(dst_path.joinpath(item_path))
            src_item_path = src_item_path.replace('\\', '/')
            dst_item_path = dst_item_path.replace('\\', '/')
            src_item_path = Path(src_item_path)
            dst_item_path = Path(dst_item_path)
            if dst_item_path.exists():
                if Path.is_dir(dst_item_path):
                    shutil.rmtree(dst_item_path)
                else:
                    os.remove(dst_item_path)
            if not dst_item_path.parent.exists():
                os.makedirs(dst_item_path.parent)
            if src_item_path.is_dir():
                shutil.move(src_item_path, dst_item_path)
            else:
                shutil.move(src_item_path, dst_item_path)

    @staticmethod
    def remove_empty_folders(path, remove_root=True):
        """Function to remove empty folders"""
        if not os.path.isdir(path):
            return

        # remove empty sub folders
        files = os.listdir(path)
        if len(files):
            for f in files:
                full_path = os.path.join(path, f)
                if os.path.isdir(full_path):
                    Generator.remove_empty_folders(full_path)

        # if folder empty, delete it
        files = os.listdir(path)
        if len(files) == 0 and remove_root:
            os.rmdir(path)

    @staticmethod
    def cp_fr_list(item_list, src_path, dst_path):
        for item_path in item_list:
            src_item_path = str(src_path.joinpath(item_path))
            dst_item_path = str(dst_path.joinpath(item_path))
            src_item_path = src_item_path.replace('\\', '/')
            dst_item_path = dst_item_path.replace('\\', '/')
            src_item_path = Path(src_item_path)
            dst_item_path = Path(dst_item_path)
            if dst_item_path.exists():
                if Path.is_dir(dst_item_path):
                    shutil.rmtree(dst_item_path)
                else:
                    os.remove(dst_item_path)
            if not dst_item_path.parent.exists():
                os.makedirs(dst_item_path.parent)
            if src_item_path.is_dir():
                shutil.copytree(src_item_path, dst_item_path)
            else:
                shutil.copy(src_item_path, dst_item_path)


if __name__ == '__main__':
    generator1 = Generator()
    generator1.generate_bsp()

