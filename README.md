# capstone-project
Repo for capstone-project


### Pretrained Model 
Download the pre-trained model [here](http://cs.stanford.edu/people/karpathy/neuraltalk2/checkpoint_v1_cpu.zip)

### Setup Neuraltalk
1. You will need a unix machine
2. Setup Torch by following the [link](http://torch.ch/docs/getting-started.html#_)
3. After installing torch - we need few more packages 
	$ luarocks install nn
	$ luarocks install nngraph 
	$ luarocks install image 
4. To run using GPU 
	$ luarocks install cutorch
	$ luarocks install cunn
5. Since we are using VGGNet-16 and ResNet-18 caffee trained models we need to install loadcaffe
	$luarocks install loadcaffe
6. To view the results
	$ th eval.lua -model /path/to/model -image_folder /path/to/image/directory -num_images 10 


### Setup the server
1. Run the Server Class under ImageCaptioningServer

### Setup the android client
1. Import the project on Android Studio
2. Change the IP to your network ip
3. Run the project

