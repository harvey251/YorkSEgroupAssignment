class AllocationSystem:
    """
    Liases with the db
    """

    def get_staff_availability_week(self, start):
        """
        start
        Question: Why do you always add in Mondays date? What's the expected behaviour if you enter Tuesdays date, is it just next 7 days?
        Question: should this have a default end date  7 days later, is there any reason to want to look ahead further

        returns list availability of staff who are AVAILABLE for the WHOLE week
        """
        pass

    def get_staff_unavailability_week(self, start):
        """
        returns list availability of staff who are UNAVAILABLE for the WHOLE week
        """
        pass

    def get_staff_partial_availability_week(self, start):
        """
        Question: Are there part time staff? if so should they always show in this list?
            If a part time staff doesn't have holiday how do we know they are available/unavailable within the system?

        returns list availability of staff who are AVAILABLE for the WHOLE week
        """
        pass

    def authorise_holiday(self):
        """
        check permission to authorise
        authorisation outcome

        Question: add to the system on authorisation OR added to the system unauthorised
        Question: does this system cater for half days

        Question: on authorisation, should automatically inform staff via email
        """

    def request_holiday(self):
        """
        Question: On request should the manager be automatically informed.
          Or schedule a daily email.  Depends on number of people they oversee

        """

    def sumbit_illness(self, staff, reason, start, number_of_days):
        """
        Question: Who do they call, I guess reception who then informs the manager, who then adds it to the system
        Question: if the managers ill who authorises?  I assumed there is always 1 manager available per shift.
        Question: Do we care about sickness duration, and report, self signed.

        staff: staff who is ill
        number_of_days: just an estimate
        """


class HolidayForm:
    """
    Question: paper or electronic???
    Question: can you take a half day???
    """

    def enter_details(self, start, return_date):
        """
        entered by staff
        """


class Staff:
    # Question, what are skills? are these discrete exams?, a ranking
    skills = []

    # Question: what is experience, years in this role, years in this role anyway, years in this role at this company
    experience = []

    # Which line they are working on, at the moement.
    # Question I feel like this should be in a table with historical data,
    #  because if they change line for a short period, all their previous experience is discounted
    line = None
    duration_on_line = None

    holiday_submission = True
    holiday_authorisation = False


class FactoryManager:
    """
    Question: does the manager need to submit their holiday. One would assume so
    """
    holiday_submission = True
    holiday_authorisation = True

    def allocate_staff_to_line(self):
        pass


class Factory:
    """
    Each Factory has several lines
    """
    name: str = None
    lines = None


class Line:
    """
    Each line has several session

    # Question: what is a line?
    """
    name: str = None
    sessions = None


class Session:
    """
    Question is this a time intercal
    """
    name: str
    start_time: datetime
    end_time: datetime