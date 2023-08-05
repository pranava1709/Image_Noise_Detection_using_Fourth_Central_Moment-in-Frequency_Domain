# Image_Noise_Detection_using_Fourth_Central_Moment-in-Frequency_Domain

Here I have divided the Noise is divided in three levels: HIGH, 
MEDIUM, LOW. Firstly we divided the Image into the blocks of 8*8 
size. Taking each Block, I converted the Pixel Values from Time 
Domain to Frequency Domain, using Discrete Cosine Transform. I, 
then sorted the array into the ascending order for each Image 
block. Here, Kurtosis analysis plays a very important role, which 
is the fourth Central Moment of an Image. The algorithm is capable of detecting Salt and Pepper Noise and Impulse 
Noise and the plot between Frequency domain and Kurtosis gives 
the Noise Level. This algorithm is based on "Ganesan, G.Maragatham & Roomi, Mansoor & Perumal, Vasuki. 
(2015). Noise Detection in Images using Moments. Research Journal 
of Applied Sciences, Engineering and Technology. 10. 307-314. 
10.19026/rjaset.10.2492"


![Capturehigh](https://github.com/pranava1709/Image_Noise_Detection_using_Fourth_Central_Moment-in-Frequency_Domain/assets/60814171/b2eb01b3-fdd1-4909-a88b-47d8c707597b)

![Capturemed](https://github.com/pranava1709/Image_Noise_Detection_using_Fourth_Central_Moment-in-Frequency_Domain/assets/60814171/8f9f18df-eb02-4a9c-bebd-8171d57fcc5c)

![Capturelow](https://github.com/pranava1709/Image_Noise_Detection_using_Fourth_Central_Moment-in-Frequency_Domain/assets/60814171/9371e303-06d4-4ce2-975a-e6127231f97b)
