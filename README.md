This script is a General Relativity Simulator that calculates gravitational time dilation near a massive body, such as Sagittarius A*. 
It uses the Schwarzschild Metric to determine how much Proper Time passes for a stationary observer compared to Coordinate Time measured from deep space.

The script assumes a non-rotating, spherical mass. It models "shell observers" who remain at a fixed distance, calculating how gravity slows their local clocks. The math respects the Schwarzschild Radius, which marks the event horizon where time effectively stops relative to the outside world.

It builds a metric tensor to define the local "density" of time, calculates the spacetime interval between two points, and converts that 4D distance into seconds.

The included plotting logic generates a "Time Cliff" graph. By sampling distances from just above the event horizon of Sagittarius a* (~12.7M km) out to 100M km, the graph visualizes the dramatic drop in proper time as an observer approaches the black hole's edge.

To make the simulation modular, constants are stored in a config.json file. This allows the user to switch between celestial bodies easily without modifying the core logic in main.py.
Example: To simulate Sagittarius A (Default): 
python main.py --body sagittarius_a

Resources: 
https://en.wikipedia.org/wiki/Time_dilation
https://en.wikipedia.org/wiki/Gravitational_time_dilation
https://en.wikipedia.org/wiki/Schwarzschild_metric