# FrisquetConnectDomoticz
Domoticz Plugin For Frisquet Connect Boiler control

# Prerequisites
- You must first have a working Frisquet Connect Site with a boiler identified and installed.
- Only one boiler must be referenced on the site. In case of multiple boilers, it may work but it has never be tested
- You will need your username and password to access the frisquetConnect site
- Domoticz 2023.2 or higher


#Features
- Control Confort, reduce and Frost Protection for one or multiple zone(s)
- Access the temperature from one or multiple zone(s)

#Work in Progress
- Hot Water control
- Multiple boiler control
- Boost control
- On/Off control
- Automatic/Manual trigger
- External temperature sensor
- Holydays
- Program
- Alarms
- Update for new version warning
- translation

#Installation
Path and command may vary depending on your installation.
- Go to your domoticz plugin folder (for example : `/var/www/domoticz/plugins/`)
- `git clone https://github.com/Krakinou/FrisquetConnectDomoticz`
- Restart your domoticz instance `sudo service domoticz restart`

Also check that the folder `FrisquetConnectDomoticz` and files are owned by the domoticz user running the instance.

#Updating
- Go to your domoticz plugin folder (for example : `/var/www/domoticz/plugins/`)
- `git pull`
- Restart your domoticz instance `sudo service domoticz restart`

#Configuration
- Add a new Hardware
- Just enter your user and password
- Devices should be created in the next minute

Following devices are created:
Device Name | Type | Fonction |
|------------|------|---------------------------------------|
|Température Zone X |Temperature| Temperature sensor from the Frisquet Visio Module for Zone X. If mutiple zones are available mutiple devices will be created |
|Consigne Hors-Gel Zone X | Setpoint | Defaut Frost Protection Thermostat setpoint |
|Consigne Réduit Zone X | Setpoint | Defaut Reduce Thermostat setpoint |
|Consigne Confort Zone X | Setpoint | Defaut Confort Thermostat setpoint |

#Contribute
Submit your PR on the dev branch.