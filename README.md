# AutoImSight

## Automating scientific imaging as decoding method for DNA nanostructures data storage 

 

### Motivation 

The principle of decoding information from DNA nanostructures back to binary data relies on Atomic Force Microscopy (AFM) imaging. This process involves encoding binary data into patterns of protein on single-layer DNA origami, then reading and matching these patterns to retrieve the encoded information. To address the limitations of speed and cost associated with traditional methods, an alternative approach involves encoding information into DNA origami and decoding it through imaging. 

The active machine learning community has led to the emergence of advanced computer vision models with improved capabilities and user-friendly inference approaches. One such method, transfer learning, allows for the use of a small amount of data to modify the weights of a pre-trained machine learning model. These pre-trained models, trained on millions of images, perform well in recognizing common objects in previously unseen pictures. However, scientific images often lack the common objects that pre-trained models can recognize without additional training. 

To harness the object recognition capabilities of pre-trained models for specific features in scientific images, fine-tuning the model with target images containing the relevant features is necessary—a process known as transfer learning. The significant advantage of transfer learning is that it requires substantially less training data to fine-tune the pre-trained model compared to training a model from scratch. This is particularly beneficial for scientific imaging, where the number of available images is typically limited due to the complexity of specimen preparation, low throughput of imaging techniques, or restricted equipment access. 

To streamline the decoding process, we developed software that automates two critical components: i) automated image acquisition and ii) automated feature detection and data saving. This software leverages the advancements in machine learning, particularly transfer learning, to enhance the efficiency and accuracy of decoding information from DNA nanostructures, making the process faster and more cost-effective. 

 
