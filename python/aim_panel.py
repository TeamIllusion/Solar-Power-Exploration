# General functionality
#
# Sun position will be estimated using pysolar.  We will also
# be able to get a prediction of the solar radiation for our
# project from the package.
#
# Check visibility of sun for time of day
#
# If sun is not visible, point to next expected sunrise position
#
# If sun is visible, check azimuth on compass, correcting error
# If sun is visible, check elevation on IMU, correcting error
# If sun is visible, compute expected radiation
#
# Motion control will be handled by a Sparkfun Auto pHat.  I know this
# seems a bit odd, but the Spark Motor Controller operates on a "Servo
# Style" PWM and the Auto pHat has four of those.  In addition, the Auto 
# pHat has two Encoder inputs and a built in 9-DOF IMU.  The 9-DOF IMU
# adds a magnetometer to the mix.  If the solar panel electronics does 
# not interfere too much, we should be able to get fairly accurate info
# on the panel's orientation.
#
# If we fail to drive the Spark Controllers, we will fall back to some
# smaller motors.


from pysolar.solar import *
import datetime
import pytz
est = pytz.timezone('US/Eastern')

latitude = 39.095833
longitude = -76.859722

date = datetime.datetime(2022, 2, 8, 12, 0, 0, 0, tzinfo=est)

altitude_deg = get_altitude(latitude_deg, longitude_deg, date)

# Sun is visible if altitude_deg is greater than zero 

azimuth_deg = get_azimuth(latitude, longitude, date))
radiation.get_radiation_direct(date, altitude_deg)
