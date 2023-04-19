# ryeeshu-saatvik-assignment5 

## Table 

| **Models**                             | **Training Time**  | **Training Loss**   | **Training Accuracy** | **Testing Accuracy** | **No. of model parameters** | **No. of epochs** |
|----------------------------------------|--------------------|---------------------|-----------------------|----------------------|-----------------------------|-------------------|
| VGG1                                   | 1749.3782160282135 | 0.5594148635864258  | 69.9999988079071      | > 55.000             | 40961153                    | 20                |
| VGG3                                   | 80.03491282463074  | 0.203384131193161   | 97.50000238418579     | > 92.500             | 10333505                    | 20                |
| VGG3 with data augmentation            | 105.11191153526306 | 0.5282458066940308  | 73.7500011920929      | > 70.000             | 10333505                    | 25                |
| Transfer learning using VGG16 or VGG19 | 151.68954753875732 | 0.02160074934363365 | 99.37499761581421     | > 97.500             | 17926209                    | 10                |
| MLP                                    | 68.79708528518677  | 0.2559237778186798  | 89.99999761581421     | > 92.500             | 15370497                    | 15                |

<br>
<hr>
<br>

## Question - 1
We observe that as we increase the complexity of the model, the **training accuracy** increase, indicating that the model is fitting the training data better. Similarly, the **testing accuracy** also improves as we increase the complexity of the model.

Also, the testing accuracy for VGG3 model with **data augmentation** is lesser than orginal model becuase of: 
- augmented images not captured the true variations in the data 
- VGG3 architecture may not be deep enough 
- introduced noise or irrelevant features 

Also, we observe that the **training time** increases as we increase the complexity of the model, which is expected as more complex models require more computation time. For example, VGG1 has highest training time becuase of high number of model parameters. 


## Question - 2
We can improve the performance of deep learning models based on VGG architecture using data augmentation. create variations of the images that can improve the ability of the fit models to generalize what they have learned to new images. This helps in better generalization and reduces overfitting. 

But, the effectiveness of data augmentation in improving the performance of a model is largely dependent on the model's capacity to learn complex features and patterns in the data. VGG1 is a relatively simple model with only a few layers and a small number of parameters, which limits its capacity to learn complex features and patterns in the data. Therefore, data augmentation may not be as effective in improving the performance of VGG1 as it would be for more complex models like VGG3 and higher.


## Question - 3
**Overfitting** can occur when the number of epochs is too **high**, resulting in a model that performs well on the training data but not on new data. On the other hand, **underfitting** can occur when the number of epochs is too **low**, leading to a model that has not learned enough from the training data and is not able to make accurate predictions. Therefore, it is crucial to find the **optimal number of epochs** that balances between the model's ability to learn from the training data and its generalization to new data.


## Question - 4
Yes, the model gets confused in a few instances. For example, in some instances, when the **tail of squirrel is hidden**, it sometimes classifies it as rat rather than a squirrel, which is likely due to the similar physical appearance of the squirrel and rat in that particular image. 


## Question - 5
Such a MLP with comparable parameters to VGG16 model **cannot learn complex features very well**, becuase MLPs do not consider the spatial behaviour of the data like CNNs. The model is more susceptible to **overfit** due to large number of layers and neurons. Also, the model requires **more computation time** and **resources**.
