import matplotlib.pyplot as plt
horizontal_axis_data = [1,4,12,14,15,17,19,19,21,23,24,25]
vertical_axis_data = [0,2,-1,7,9,-3,0,6,9,10,-2,3]
plt.plot(horizontal_axis_data,vertical_axis_data,"ro")#ro = red circle ploints
plt.show()
plt.clf() # for clear screen
plt.plot(horizontal_axis_data,vertical_axis_data)# without third argumant it
    #draw  linear chart
plt.show()
