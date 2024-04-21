"""
Parsing information from the AI in order to
format it in an interpretable way for Reflex
"""

def check_if_week(s: str) -> bool:
    """Checks if the current string contains the phrase 'Week'"""
    if len(s) >= 4:
        if s[0:4] == 'Week':
            return True
    
    return False


# container for each section of the ai's feedback (divided by the time)
class StudyPlan():
    """Contains the data containing the study plan"""
    def __init__(all_text: str):

        def sort_text(all_text: str) -> list['Section']:
            sorted_text = []
            curr_week = []
            # need info on the format of the string before continuing
            sentences = all_text.split('\n')

            # split all by weeks first
            for s_ind in range(len(sentences)):
                if len(sentences[s_ind]) >= 4 and sentences[s_ind][0:4] == 'Week':
                    curr_week.append(sentences[s_ind])
                    remaining = sentences[s_ind+1:]
                    check_ind = s_ind+1
                    # could be out of scope index
                    s2 = remaining[check_ind] # specific value that's next

                    while check_if_week(s2) is False:
                        curr_week.append(sentences[s2])
                        check_ind += 1
                    
                    if check_if_week(s2) is True:
                        pass
                        # create_selection(curr_week)
                        # curr_week = [] if not reset already
                    
                    # week = s.strip()[4:-1]

                    # Section(week, focus, activities)

        
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

    def get_all_values() -> list[int, str, list]:
        """returns all the attributes of a Section object as
        a list"""
        return [self._week, self._focus, self._activities]


