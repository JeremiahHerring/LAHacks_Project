"""
Parsing information from the AI in order to
format it in an interpretable way for Reflex
"""

# container for each section of the ai's feedback (divided by the time)
class StudyPlan():
    """Contains the data containing the study plan"""
    def __init__(all_text: str):

        def sort_text(all_text: str) -> list['Section']:
            sorted_text = []
            # need info on the format of the string before continuing
            pass 
        
        # a list consisting of strings seperated by their week (time) association
        self._all_text = sort_text(all_text)

    def get_all_text() -> list['Section']:
        """Returns a list containing all the sorted tips from the
        study plan, a string containing all the data"""
        return self._all_text


# an object consisting of the aspects of a particular week of advice 
class Section():
    def __init__(week: int, focus: str, activities: list[str]):
        self._week = week
        self._focus = focus
        # the activities label can be hard coded intgitgto the ui since it won't be changed,
        # only these activities
        self._activities = activities

    def get_week() -> int:
        """Returns the week number"""
        return self._week

    def get_focus() -> str:
        """Returns the focus that the user needs to prioritize"""
        return self._focus

    def get_activities() -> list[str]:
        """returns a list of all the activities the user may partake in"""
        return self._activities


