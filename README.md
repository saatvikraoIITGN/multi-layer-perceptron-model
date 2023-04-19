# yeeshu-saatvik-assignment5 

## Question - 1
We observe that as we increase the complexity of the model, both the **training loss** and **training accuracy** increase, indicating that the model is fitting the training data better. Similarly, the **testing accuracy** also improves as we increase the complexity of the model.

However, we notice an unexpected trend where the **testing accuracy was consistently higher than the training accuracy**. This is due to the limited amoung of training data we used.

Also, we observe that the **training time** increases as we increase the complexity of the model, which is expected as more complex models require more computation time.


## Question - 2
We can improve the performance of deep learning models based on VGG architecture using data augmentation. The amount of training data can be increaed by applying transformations such as *rotaion*, *flipping* and *cropping*. This helps in better generalization and reduces overfitting.

But, data augmentation is limited in VGG3 models because of the model's incapability to capture the complexity and variation of data, resulting in low performance. So, for VGG3 model, data augmentation can be helpful but not as significant as it would be for larger models (like the original VGG architecture with 16 layes which can capture more complex features in data).


## Question - 3
**Overfitting** can occur when the number of epochs is too **high**, resulting in a model that performs well on the training data but not on new data. On the other hand, **underfitting** can occur when the number of epochs is too **low**, leading to a model that has not learned enough from the training data and is not able to make accurate predictions. Therefore, it is crucial to find the optimal number of epochs that balances between the model's ability to learn from the training data and its generalization to new data.


## Question - 4
Yes, the model gets confused in a few instances. For example, in some instances, when the **tail of squirrel is hidden**, it sometimes classifies it as rat rather than a squirrel, which is likely due to the similar physical appearance of the squirrel and rat in that particular image.


## Question - 5
Such a MLP with comparable parameters to VGG16 model **cannot learn complex features very well**, becuase MLPs do not consider the spatial behaviour of the data like CNNs. The model is more susceptible to **overfit** due to large number of layers and neurons. Also, the model requires **more computation time**.