# rpi_battery_data_logger
This is a repository that holds two simple application, as follows:

- **Server API**
    - Have enpoints to receive POSTS with data
    - Have endpoits to respond to GET request
    - Stores data in SQLite3

- **Client Application**
    - Grabs information about the system (such as time, system stress, anything that seems useful)
    - Make POST requests to the Server Application

### About the tools used

- Flask
- SQLAlchemy
- SQLite3

### Why?

I've bought a battery pack for a RaspberryPi Zero W and want to know how much time it stays on on battery.
I know that I could stick a pendrive on that and make it update a simple sqlite database on it, but I wanted
to make it more interesting.

### Notes
- THIS APPLICATION IS NOT SECURE! I've created to use it in a controlled lab, I didn't added any layer of security,
  there is no JWT, Tokens and so.
- DO NOT USE IT FOR ANY PRODUCTION ENV! If it isn't obvious enough, it is just to play around with APIs on an Embedded system.