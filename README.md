# Capture the Compute Capability of the NVIDIA GPU
A web crawler to capture the compute capability of the NVIDIA GPU.

|       script          |       describe        |
|       ------          |       --------        |
|   [gen_gpu_table.py](gen_gpu_table.py)  |     generate a JSON file which include all information from the [NVIDIA website](https://developer.nvidia.com/cuda-gpus)
|   [get_info.py](get_info.py)            |     capture the target information like "capability", "full name"

# Requirement
```bash
pip3 install -r requirements.txt
```

# How to use
* Get the capability
    ```bash
    # help
    $ python3 get_gpu_info.py -h

    # get the information of Jetson AGX
    $ python3 get_gpu_info.py -n AGX
    NAME:  Jetson AGX Xavier
    TITLE: CUDA-Enabled Jetson Products
    SUB_TITLE: Jetson Products
    CAPABILITY: 7.2

    # get the capability of Jetson A6000
    $ python3 get_gpu_info.py -n A6000 --capability
    8.6

    # get all the information of the gpu which name include 3060
    $ python3 get_gpu_info.py -n 3060
    NAME:  Geforce RTX 3060 Ti
    TITLE: CUDA-Enabled GeForce and TITAN Products
    SUB_TITLE: GeForce and TITAN Products
    CAPABILITY: 8.6
    NAME:  Geforce RTX 3060
    TITLE: CUDA-Enabled GeForce and TITAN Products
    SUB_TITLE: GeForce and TITAN Products
    CAPABILITY: 8.6
    NAME:  GeForce RTX 3060
    TITLE: CUDA-Enabled GeForce and TITAN Products
    SUB_TITLE: GeForce Notebook Products
    CAPABILITY: 8.6
    ```
* Get the full name
    ```bash
    $ python3 get_gpu_info.py -n nano --fullname
    Jetson Nano
    ```
* Print and Generate the table of GPU Information
    ```bash
    $ python3 gen_gpu_table.py 
    {'GeForce 410M': {'capability': '2.1',
                    'sub_title': 'GeForce Notebook Products',
                    'title': 'CUDA-Enabled GeForce and TITAN Products'},
    'GeForce 610M': {'capability': '2.1',
                    'sub_title': 'GeForce Notebook Products',
                    'title': 'CUDA-Enabled GeForce and TITAN Products'},
    'GeForce 705M': {'capability': '2.1',
                    'sub_title': 'GeForce Notebook Products',
                    'title': 'CUDA-Enabled GeForce and TITAN Products'},
    # ...
    'Tesla P100': {'capability': '6.0',
                'sub_title': 'NVIDIA Data Center Products',
                'title': 'CUDA-Enabled Datacenter Products'},
    'Tesla P4': {'capability': '6.1',
                'sub_title': 'NVIDIA Data Center Products',
                'title': 'CUDA-Enabled Datacenter Products'},
    'Tesla P40': {'capability': '6.1',
                'sub_title': 'NVIDIA Data Center Products',
                'title': 'CUDA-Enabled Datacenter Products'}}

    # the gpu_info.json sould be generated
    $ ls
    gen_gpu_table.py  get_gpu_info.py  gpu_info.json  LICENSE  README.md
    ```
# Reference
[CUDA GPUs](https://developer.nvidia.com/cuda-gpus)