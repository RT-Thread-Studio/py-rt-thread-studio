# py-rt-thread-studio

py-rt-thread-studio supply some tools used for  RT-Thread Studio IDE project.



## install

```python
pip install rt-thread-studio
```

## requirements

+ python 3.x
+ pyyaml

## features list

1. board support package check

   example

   ```python
   from rt_thread_studio import bsp_checker
   
   bsp_path = '.'
   checker = bsp_checker.BspChecker(bsp_path)
   checker.check();
   ```

   

