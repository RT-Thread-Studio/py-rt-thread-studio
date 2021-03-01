TEMP_TAML_STR = """---
yaml_version: 3
pkg_version: 1.0.0
pkg_vendor: RealThread
pkg_type: Board_Support_Packages
board:
  name: STM32L475-ATK-PANDORA
  version: Rev.A
  vendor: ATK
  description_zh: 潘多拉 IoT Board 是正点原子和 RT-Thread 联合出品，定位为 IoT 物联网开发板。板载资源非常丰富，集成度非常高。同时潘多拉开发板也是正点原子和
    RT-Thread 指定的 IoT 开发板。
  description_en: Pandora IoT Board is a joint product of ATK and RT-Thread, and is
    positioned as an IoT development board. The onboard resources are very rich and
    the integration is very high. At the same time, the Pandora development board
    is also an IoT development board designated by ATK and RT-Thread.
  small_image: documents/images/board_small.png
  large_image: documents/images/board_large.png
  sale_contact_cn: http://www.alientek.com/
  sale_contact_global: http://www.alientek.com/
  buy_url_cn: https://detail.tmall.com/item.htm?id=609759187128
  buy_url_global: https://detail.tmall.com/item.htm?id=609759187128
  price_cn: 238.00 CNY
  price_global: 35.00 USD
  debugger: ST-LINK
  debug_interface: SWD
  emulator_machine: ''
chip:
  device_vendor: STMicroelectronics
  family_name: STM32
  series_name: STM32L4
  sub_series_name: STM32L475
  chip_name: STM32L475VETx
  rx_name: PA10
  tx_name: PA9
  clock_source: HSE
  source_freq: '8000000'
  target_freq: '240000000'
  uart_name: UART1
docs:
- file: documents/manuals/UM3004-RT-Thread-IoT Board.pdf
  title: Rt-Thread IoT Board
  category: manual
- file: documents/sheet/STM32L475xx Datasheet.pdf
  title: STM32L475xx Datasheet
  category: sheet
features:
- On-board ST-LINK/V2.1
- SRAM:128K
- SDIO WIFI:AP6181
- 1.3 inch TFT:240*240
- Audio:ES8388
- Sensor:ICM-20608
- Sensor:AHT10
- Motor:TC214B
- Interface:ATK module
- Examples:36 bare-metal demos and 30 RT-Thread demos
features_zh:
- 板载仿真器 ST-LINK/V2.1
- SRAM:128K
- SDIO WIFI:AP6181
- 1.3 inch TFT:240*240
- 音频:ES8388
- 传感器:ICM-20608
- 传感器:AHT10
- 马达:TC214B
- 接口:ATK module
- 例程:36 bare-metal demos and 30 RT-Thread demos
template_projects:
- project_name: empty
  project_description: creat this peoject if user choose rt-thread project
  project_type: rt-thread|@full|@4.0.2
  builtin_files:
  - source_path_offset: default_project_0
    target_path_offset: ''
    files_and_folders:
    - ".settings"
    - applications
    - board
    - figures
    - libraries
    - ".config"
    - ".cproject"
    - ".gitignore"
    - ".project"
    - cconfig.h
    - Kconfig
    - makefile.targets
    - project.ewd
    - project.ewp
    - project.eww
    - project.uvoptx
    - project.uvprojx
    - README.md
    - rtconfig.h
    - rtconfig.py
    - rtconfig_preinc.h
    - SConscript
    - SConstruct
    - template.ewp
    - template.eww
    - template.uvoptx
    - template.uvprojx
  external_files:
  - package_type: Chip_Support_Packages
    package_vendor: RealThread
    package_name: STM32L4
    package_version: 0.1.9
    source_path_offset: ''
    target_path_offset: ''
    files_and_folders: []
  - package_type: RT-Thread_Source_Code
    package_vendor: ''
    package_name: RT-Thread
    package_version: 4.0.2
    source_path_offset: ''
    target_path_offset: rt-thread
    files_and_folders:
    - components
    - include
    - libcpu/arm
    - libcpu/Kconfig
    - libcpu/SConscript
    - src
    - tools
    - Kconfig
    - LICENSE
- project_name: empty3
  project_description: creat this peoject if user choose rt-thread project
  project_type: rt-thread|@full|@latest
  builtin_files:
  - source_path_offset: default_project_0
    target_path_offset: ''
    files_and_folders:
    - ".settings"
    - applications
    - board
    - figures
    - libraries
    - ".config"
    - ".cproject"
    - ".gitignore"
    - ".project"
    - cconfig.h
    - Kconfig
    - makefile.targets
    - project.ewd
    - project.ewp
    - project.eww
    - project.uvoptx
    - project.uvprojx
    - README.md
    - rtconfig.h
    - rtconfig.py
    - rtconfig_preinc.h
    - SConscript
    - SConstruct
    - template.ewp
    - template.eww
    - template.uvoptx
    - template.uvprojx
  external_files:
  - package_type: Chip_Support_Packages
    package_vendor: RealThread
    package_name: STM32L4
    package_version: 0.1.9
    source_path_offset: ''
    target_path_offset: ''
    files_and_folders: []
  - package_type: RT-Thread_Source_Code
    package_vendor: ''
    package_name: RT-Thread
    package_version: latest
    source_path_offset: rt-thread
    target_path_offset: rt-thread
    files_and_folders:
    - components
    - include
    - libcpu/arm
    - libcpu/Kconfig
    - libcpu/SConscript
    - src
    - tools
    - Kconfig
    - LICENSE
- project_name: empty2
  project_description: creat this peoject if user choose rt-thread project
  project_type: rt-thread|@full|@lts-v3.1.4
  builtin_files:
  - source_path_offset: default_project_0
    target_path_offset: ''
    files_and_folders:
    - ".settings"
    - applications
    - board
    - figures
    - libraries
    - ".config"
    - ".cproject"
    - ".gitignore"
    - ".project"
    - cconfig.h
    - Kconfig
    - makefile.targets
    - project.ewd
    - project.ewp
    - project.eww
    - project.uvoptx
    - project.uvprojx
    - README.md
    - rtconfig.h
    - rtconfig.py
    - rtconfig_preinc.h
    - SConscript
    - SConstruct
    - template.ewp
    - template.eww
    - template.uvoptx
    - template.uvprojx
  external_files:
  - package_type: Chip_Support_Packages
    package_vendor: RealThread
    package_name: STM32L4
    package_version: 0.1.9
    source_path_offset: ''
    target_path_offset: ''
    files_and_folders: []
  - package_type: RT-Thread_Source_Code
    package_vendor: ''
    package_name: RT-Thread
    package_version: lts-v3.1.4
    source_path_offset: ''
    target_path_offset: rt-thread
    files_and_folders:
    - components
    - include
    - libcpu/arm
    - libcpu/Kconfig
    - libcpu/SConscript
    - src
    - tools
    - Kconfig
    - LICENSE
example_projects: []
"""