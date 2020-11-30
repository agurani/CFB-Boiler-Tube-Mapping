# CFB-Furnace-Tube-Visualization
### Circulating Fluidized Bed Boiler (CFB) Furnace Tubes Ultrasonic Thickness Mapping Measurements and Visualization

**This code is for CFB Boiler maintenance team.**

CFB Boiler furnace chamber tubes thickness has been checked at different levels on the front wall, rear, right and left walls. Thicknesses have been measured with ultrasonic testing device which has B scanning feature. Measurements are continuously recorded every 1 mm of 1m wall tube length. With Tube thickness less than a specific value is needed to be marked for replacing with proper thickness of tubes.

Examined components are recorded in excel format for each wall. This means 160 tubes for front wall, recorded into 160 excel formatted files. And each file has 1000 data of tube thickness. These measurements are taken also for left wall (which has 80 tubes), rear wall (160 tubes) and right wall (80 tubes).

This application implemented to furnace chamber walls of CFB boiler at different levels. For each level there are 480 excel files which include 1000 thickness or more data in each file.

For evaluating of this bulky data, a python code is written to collect all data in suitable format from each tube excel file.

The mapping determines how the attributes of these tube thicknesses vary according to the data. Color scales are used to show the thinnest to the thickest tubes. The thinnest one is assigned as red color, and the thickest are assigned as green color.

This effective visualization helps CFB Boiler Operators analyze and reason about data and evidence. It makes complex data more accessible, understandable and usable. CFB Boiler Operators may have particular analytical tasks, such as making comparison of internal circulation inside the combustion chamber.


<a href="url"><img src="https://github.com/agurani/CFB-Boiler-Tube-Mapping/blob/main/13500%20RearWall%20Tube%20Thicknesses%20Visualization.JPG" align="left" height="350" width="350" ></a> 
<a href="url"><img src="https://github.com/agurani/CFB-Boiler-Tube-Mapping/blob/main/13500%20FrontWall%20Tube%20Thicknesses%20Visualization.JPG" align="left" height="350" width="350" ></a> <br/>
