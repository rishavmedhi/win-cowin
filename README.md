# win-cowin
As all Indians are frustrated with the vaccine situation in India and missing out booking of vaccine slots.  

This is a simple python script which uses the [Cowin website](https://www.cowin.gov.in/home) APIs and tells if there are any free slots available for booking at a particular district.

You can run the script on the terminal and it notifies you of a free slot with an audible speech saying "SLOTS AVAILABLE" and also a terminal log.

You can then open https://selfregistration.cowin.gov.in/ and book the open slots there at the particular location

**NOTE:** _This script doesn't book a slot for you. It's only for notifying you if there is a slot available at the moment_

## Usage

1. Clone the script in your local system using  
`git clone https://github.com/rishavmedhi/webrtc-basic.git`

2. In the script, change the code at the following places to customise the script as per your needs:

    **Change Place to be searched**

    ```python
    districtIds = [265, 294]
    ```

    Add the district ids of the districts you wish to search the slots.

    **Change Age**

    By default, you can search slots only for 18+  
    You can also edit this line to find slots for age 45+

    ```python
      if session['available_capacity']>0 and session['min_age_limit']==18:
    ```

    Change `session['min_age_limit']==45` to search slots for age 45+

3. Install the following packages using pip for running the script:  
    - [Requests](https://pypi.org/project/requests/)
    - [Pytz](https://pypi.org/project/pytz/)

4. Open the terminal in the project directory and run the script using the following command:  
`python3 win-cowin.py`

5. Script uses python scheduler library which calls the main function again after a minute.

## Known Issues

- The local system is to be active for the script to work. If the system goes to sleep, the script will not work
