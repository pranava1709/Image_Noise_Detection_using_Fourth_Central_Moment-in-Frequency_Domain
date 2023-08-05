# Image_Noise_Detection_using_Fourth_Central_Moment-in-Frequency_Domain

Here I have divided the Noise is divided into three levels: HIGH, 
MEDIUM, LOW. Firstly we divided the Image into the blocks of 8*8 
size. Taking each Block, I converted the Pixel Values from Time 
Domain to Frequency Domain, using Discrete Cosine Transform. I 
then sorted the array into ascending order for each Image 
block. Here, Kurtosis analysis plays a very important role, which 
is the fourth Central Moment of an Image. The algorithm is capable of detecting Salt and Pepper Noise and Impulse 
Noise and the plot between Frequency domain and Kurtosis give 
the Noise Level. This algorithm is based on "Ganesan, G.Maragatham & Roomi, Mansoor & Perumal, Vasuki. 
(2015). Noise Detection in Images using Moments. Research Journal 
of Applied Sciences, Engineering, and Technology. 10. 307-314. 
10.19026/rjaset.10.2492"


![Capturehigh](https://github.com/pranava1709/Image_Noise_Detection_using_Fourth_Central_Moment-in-Frequency_Domain/assets/60814171/ae031e1f-41bd-419c-968a-7c6fa5e78184)

![Capturemed](https://github.com/pranava1709/Image_Noise_Detection_using_Fourth_Central_Moment-in-Frequency_Domain/assets/60814171/54bada41-1fd1-439b-b2b6-ab3803a6030a)

![Capturelow](https://github.com/pranava1709/Image_Noise_Detection_using_Fourth_Central_Moment-in-Frequency_Domain/assets/60814171/d62271b3-b6d5-4aab-aaa7-c07c6e6b14a5)
