Problem Statement: Air Traffic Controller (ATC) is responsible for safe and orderly flow of air traffic and serves air traffic on First-In, First-Out (FIFO) unless there is emergency. <br>
In typical scenario, ATC is mainly responsible for following. <br>
• Orderly takeoff of aircrafts provided there are some aircrafts waiting in a queue. <br>
• Clearing Runways for aircrafts for landing which depends on aircraft going to takeoff. If Runway is not clear then it is possible to ask the pilot to go in a queue until cleared for landing. <br>
• Clear Runways for emergency landing before aircraft runs out of fuel. <br>
• If runway cannot be cleared for emergency landing then ATC can ask pilot to redirect flight to nearby airport separated by certain distance. <br>
 <br>
Assumptions: <br>
• Aircraft will be represented by flight number and remaining fuel. There will be fuel consumption/cost involved for landing.  <br>
• Aircrafts can go for emergency landing or normal landing. <br>
• ATC will allow landing on based landing priority (emergency/normal) and remaining fuel. <br>
• ATC will be represented by ATC_ID, no. of runways, takeoff queue, landing queue and distance of neighboring ATCs. <br>
• Once aircraft is in ATC vicinity then it is assumed that there is no further distance between ATC an aircraft. Except the fact that fuel consumption is required for landing. <br>
• If one aircraft lands, it means remaining aircrafts in queue will lose certain fuel specified by fuel consumption/cost for landing. <br>
• Once aircraft has landed, then it will go into takeoff queue and wait till interval has elapsed for takeoff. No parking of any sort. Aircrafts from takeoff queue will be emptied with each time unit interval. <br>

Requirements:  <br>
Design an application or distributed application to simulate behavior of ATC. <br>
Additionally, user should be able to see the current aircraft status on a screen of some sort for monitoring like on Browser, Command Line Tabular data, etc. <br>

When application starts it will be provided with following.
1. List of ATCs, their neighboring ATCs separated by distance d, available runways and max landing/takeoff queue limit.
2. Fuel consumption/cost for landing of an aircraft.
3. Interval (time units) of takeoff for each aircraft.
4. Fuel cost per Distance unit in case aircraft needs to travel to another ATC.
5. Initially, takeoff and landing queue will be empty for ATC. <br>
Input will be given in the form of JSON. <br>
Aircraft is represented as below <br>
{ <br>
 "flight_number": "a1", <br>
 "fuel": 100 <br>
} <br>
List of ATCs is represented as <br>
[ <br>
{ <br>
 "atc_id": "atc1", <br>
 "runways": 2, <br>
 "takeoff_limit": 4, <br>
 "landing_limit": 4, <br>
 "takeoff_queue": ["a1", "a2"] <br>
 "landing_queue": ["a3", "a4"] <br>
 "neighbor_atc": [{"atc_id": "atc2", "dist": 2}] <br>
}, <br>
{ <br>
 "atc_id": 2, <br>
 "runways": 1, <br>
 "takeoff_limit": 5, <br>
 "landing_limit": 4, <br>
 "takeoff_queue": ["a5", "a6"] <br>
 "landing_queue": ["a7", "a8"] <br>
 "neighbor_atc": [{"atc_id": "atc1", "dist": 2} <br>
]
