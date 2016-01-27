#Exercise 2
The client is very excited about these new features you are delivering. Unfortunately they have a dodgy set-up which means their servers occasionally crash.

They need you to modify your program so when they input a timestamp and schedule file it returns the TV show currently playing, and how far (in seconds) we are into the show. This is known as the _seek time_, as it can then be used to seek to the correct location in the show.

##Example
For example, given the inputs:

 - tv_schedule_1.csv
 - 1453805100

The output should be "Homes Under the Hammer" and 2700.
The show started at 1453802400, or 26th January 2016 at 10:00.
The input timestamp 1453805100 converts to 10:45 on 26th January 2016.
2700 / 60 = 45.

# Exercise 2.1
For the input timestamp 1453822200 what TV show is playing, and what's the seek time?

## Exercise 2.2
For the input timestamp 1453828500 what TV show is playing, and what's the seek time?
