import matplotlib.pyplot as plt

perfs_5_5 = [(-33.75195339596918, 12.7171613142), (-33.751459504743515, 12.7310337044), (-33.75127923794514, 12.6927154059), (-33.75029821148631, 12.6538821085), (-33.73021654769751, 13.1594502929), (-33.672048612269705, 11.820640766), (-33.55730210836235, 11.0521360186), (-33.313753434279384, 9.33135356512), (-33.2598846545417, 8.90662065381), (-33.14452264911503, 14.4714959918), (-32.58687971682872, 3.00834479471), (-32.58566898133363, 3.0), (-32.10434601320493, 0.0), (-14.628542882216717, 25.0), (-12.00185272068717, 50.0), (-11.839974547824376, 48.0958962191)]

perfs_5_15 = [(-33.34420799742127, 11.0521360186), (-33.210631028344885, 9.33135356512), (-33.17996237036455, 8.90662065381), (-32.58663280746835, 3.00834479471), (-32.5854903543183, 3.0), (-32.10434601320493, 0.0), (-31.03607921990066, 11.820640766), (-21.642274082465605, 12.6538821085), (-21.275680068818797, 12.6927154059), (-21.05148261159282, 12.7171613142), (-20.925538224452083, 12.7310337044), (-17.716310162861788, 13.1594502929), (-13.432946915275785, 14.4714959918), (-12.365398508609744, 25.0), (-12.132164302150866, 50.0), (-11.974742807483327, 48.0958962191)]

perfs_5_25 = [(-33.20852187702491, 9.33135356512), (-33.17874813138406, 8.90662065381), (-32.58663280746835, 3.00834479471), (-32.5854903543183, 3.0), (-32.10434601320493, 0.0), (-26.211635732840975, 11.0521360186), (-16.89683951541342, 11.820640766), (-13.845649207964934, 12.6538821085), (-13.790408197401756, 12.6927154059), (-13.757507619723444, 12.7171613142), (-13.739193664272292, 12.7310337044), (-13.3684903404706, 13.1594502929), (-13.022520290760935, 14.4714959918), (-12.345327737086109, 25.0), (-12.167224216891908, 50.0), (-12.007985067344372, 48.0958962191)]


perfs_525_5 = [(-33.75195339596918, 12.7171613142), (-33.751459504743515, 12.7310337044), (-33.75127923794514, 12.6927154059), (-33.75029821148631, 12.6538821085), (-33.73021654769751, 13.1594502929), (-33.672048612269705, 11.820640766), (-33.55730210836235, 11.0521360186), (-33.313753434279384, 9.33135356512), (-33.2598846545417, 8.90662065381), (-33.14452264911503, 14.4714959918), (-33.125224799642204, 7.74339026692), (-33.094447026277166, 14.5186636924), (-33.08167576019211, 7.33039954976), (-33.01040672742421, 6.65689729457), (-32.9835400294306, 6.39804098317), (-32.98182824325757, 6.37932586064), (-32.98157770045403, 6.37786059331), (-32.920989987462484, 5.80684309037), (-32.79694249818647, 4.68589989593), (-32.781164993168034, 4.54985044422), (-32.607552572836354, 3.17023101017), (-32.58687971682872, 3.00834479471), (-32.58566898133363, 3.0), (-32.33580717895648, 1.33288247399), (-32.11008216893854, 0.000147472750265), (-32.10434601320493, 0.0), (-14.628542882216717, 25.0), (-12.00185272068717, 50.0), (-11.839974547824376, 48.0958962191)]

perfs_525_15 = [(-33.34420799742127, 11.0521360186), (-33.210631028344885, 9.33135356512), (-33.17996237036455, 8.90662065381), (-33.08833276059569, 7.74339026692), (-33.052804386351355, 7.33039954976), (-32.99463224117171, 6.65689729457), (-32.9708438587864, 6.39804098317), (-32.969424079898594, 6.37932586064), (-32.96927812115623, 6.37786059331), (-32.91336419240331, 5.80684309037), (-32.79486680446065, 4.68589989593), (-32.778972879043316, 4.54985044422), (-32.60717832406698, 3.17023101017), (-32.58663280746835, 3.00834479471), (-32.5854903543183, 3.0), (-32.335807289932916, 1.33288247399), (-32.11008216893854, 0.000147472750265), (-32.10434601320493, 0.0), (-31.03607921990066, 11.820640766), (-21.642274082465605, 12.6538821085), (-21.275680068818797, 12.6927154059), (-21.05148261159282, 12.7171613142), (-20.925538224452083, 12.7310337044), (-17.716310162861788, 13.1594502929), (-13.432946915275785, 14.4714959918), (-13.382271882600849, 14.5186636924), (-12.365398508609744, 25.0), (-12.132164302150866, 50.0), (-11.974742807483327, 48.0958962191)]

perfs_525_25 = [(-33.20852187702491, 9.33135356512), (-33.17874813138406, 8.90662065381), (-33.08803406356679, 7.74339026692), (-33.05274303125204, 7.33039954976), (-32.99462550235506, 6.65689729457), (-32.97085249025889, 6.39804098317), (-32.96941709611677, 6.37932586064), (-32.96927805417134, 6.37786059331), (-32.91335831982086, 5.80684309037), (-32.79486680446065, 4.68589989593), (-32.778972879043316, 4.54985044422), (-32.60717832406698, 3.17023101017), (-32.58663280746835, 3.00834479471), (-32.5854903543183, 3.0), (-32.335807289932916, 1.33288247399), (-32.11008216893854, 0.000147472750265), (-32.10434601320493, 0.0), (-26.211635732840975, 11.0521360186), (-16.89683951541342, 11.820640766), (-13.845649207964934, 12.6538821085), (-13.790408197401756, 12.6927154059), (-13.757507619723444, 12.7171613142), (-13.739193664272292, 12.7310337044), (-13.3684903404706, 13.1594502929), (-13.022520290760935, 14.4714959918), (-13.017614782770513, 14.5186636924), (-12.345327737086109, 25.0), (-12.167224216891908, 50.0), (-12.007985067344372, 48.0958962191)]

scores5 = []
params5 = []

scores15 = []
params15 = []

scores25 = []
params25 = []

for score, param in perfs_525_5:
    scores5.append(-score)
    params5.append(param)

for score, param in perfs_525_15:
    scores15.append(-score)
    params15.append(param)

for score, param in perfs_525_25:
    scores25.append(-score)
    params25.append(param)


plt.plot(params5, scores5, 'ro', label= "5 iterations")
plt.plot(params15, scores15, 'bo', label = "15 iterations")
plt.plot(params25, scores25, 'go', label = "25 iterations")
plt.legend()
plt.show()