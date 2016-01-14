# Caption-Generator
To generate captions for any image, we need to run the eval.lua file. 

1. Make a folder called images and place the image you want to caption inside that folder. 

2. This code is written in Lua and requires Torch. If you're on Ubuntu, installing Torch in your home directory may look something like: 
```bash
$ curl -s https://raw.githubusercontent.com/torch/ezinstall/master/install-deps | bash
$ git clone https://github.com/torch/distro.git ~/torch --recursive
$ cd ~/torch; 
$ ./install.sh      # and enter "yes" at the end to modify your bashrc
$ source ~/.bashrc
```

See the Torch installation documentation for more details. After Torch is installed we need to get a few more packages using [LuaRocks](https://luarocks.org/) (which already came with the Torch install). In particular:

```bash
$ luarocks install nn
$ luarocks install nngraph 
$ luarocks install image 
$ luarocks install cutorch
$ luarocks install cunn
$ luarocks install loadcaffe
```
Download the model checkpoint from here: http://cs.stanford.edu/people/karpathy/neuraltalk2/checkpoint_v1_cpu.zip


To caption images run this line 

```bash
$ th eval.lua -model /path/to/model -image_folder /path/to/image/directory -num_images 1 -gpuid -1
```

Run the process.py to print captions to terminal.

```bash
python process.py vis/vis.json
```
getimages.py is a python script to fetch instagram images based on a hashtag.

Source and reference: https://github.com/karpathy/neuraltalk2
