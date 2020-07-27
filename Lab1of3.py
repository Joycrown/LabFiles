#Note that this code uses scientific notation to define large numbers. 4.445e8 is equal to 4.445 * 10 ** 8 which is equal to 444500000.0.

# The current volume of a water reservoir (in cubic metres)
reservoir_volume = 4.445e8
# The amount of rainfall from a storm (in cubic metres)
rainfall = 5e6

# decrease the rainfall variable by 10% to account for runoff
decrease= int(rainfall) - (int(rainfall) * 0.1)
print(decrease)



# add the rainfall variable to the reservoir_volume variable
print(int(reservoir_volume) + int(rainfall))



# increase reservoir_volume by 5% to account for stormwater that flows into the reservoir in the days following the storm
increase_in_reservoir_volme= (int(reservoir_volume) + int(reservoir_volume) * 0.5)




# decrease reservoir_volume by 5% to account for evaporation
decrease_in_new_reservoir_volume= (int(increase_in_reservoir_volme) - int(increase_in_reservoir_volme) * 0.5)



# subtract 2.5e5 cubic metres from reservoir_volume to account for water that's piped to arid regions.
for_arid_region= (int(decrease_in_new_reservoir_volume) - int(2.5e5))





# print the new value of the reservoir_volume variable
new_volume= (int(increase_in_reservoir_volme)- int(for_arid_region) - int(decrease_in_new_reservoir_volume))
print(new_volume)
