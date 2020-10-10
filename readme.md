# py-rt-thread-studio

py-rt-thread-studio supply some tools used for  RT-Thread Studio IDE project.



## install

```python
pip install rt-thread-studio
```

## requirements

+ python 3.x
+ pyyaml
+ click

## features list

1. board support package check

   example

   ```python
   from rt_thread_studio import bsp_checker
   
   bsp_path = '.'
   checker = bsp_checker.BspChecker(bsp_path)
   checker.check();
   ```
2. create board support package

    open powershell or cmd, run `rt_tools create`
    ```powershell
    PS C:\Users\yaxing.chen\Pictures> rt_tools create
    Step 0: 请输入开发板支持包名称:
    >13888
    Step 1: 请输入开发板支持包的存储位置（如果希望使用图形界面选择，请直接点击 Enter 键）
    >.
    Step 2: 请选择一个 RT-Studio 工程（如果希望使用图形界面选择，请直接点击 Enter 键）
    >
    Step 3: 探测到这是一个 rt-thread 工程，是否移除工程内 rt-thread 源代码并添加对 rt-thread 源代码依赖信息 ? [Y/n]
    >
    Step 4: 请选择该工程使用的 rt-thread 版本 [0/1/2]:
            rt-thread 4.0.2  ------------------- 0
            rt-thread latest ------------------- 1
            rt-thread nano   ------------------- 2
    >1
    C:/RT-ThreadStudio111full/workspace/F051
    ['.config', '.config.old', '.cproject', '.gitattributes', '.gitignore', '.project', '.sconsign.dblite', '.settings', 'applications', 'build', 'cconfig.h', 'Debug', 'debug.log', 'drivers', 'Kconfig', 'libraries', 'linkscripts', 'makefile.targets', 'rtconfig.h', 'rtconfig.py', 'rtconfig.pyc', 'rtconfig_preinc.h', 'SConscript', 'SConstruct']
    Step 5: 请输入您的公司名称，如果希望使用默认值（RealThread），请直接点击 Enter 键。
    >
    Step 6: 请输入开发板的名称，如果希望使用默认值（STM32L475-ATK-PANDORA），请直接点击 Enter 键。
    >
    Step 7: 请输入板载 MCU 的厂商名称，如果希望使用默认值（STMicroelectronics），请直接点击 Enter 键。
    >
    Step 8: 完成.
    开发板支持包位于 :  13888
    
    以下信息需要手动完善
    * 修改yaml文件内的详细信息，包含价格，销售链接，图片位置等
    * 开发板的图片信息，默认位置在documents/images/ 文件夹下
    * 开发板和 mcu 的文档信息，默认位置在documents下
    
    PS C:\Users\yaxing.chen\Pictures>
```

   

