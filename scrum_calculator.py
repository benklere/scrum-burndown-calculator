class scrum_calculator:
    def scrum_calculator(self, total_story_points, sprints, remaining_story_points, weeks_per_sprint):
        average_velocity = total_story_points / sprints
        expected_sprints = remaining_story_points / average_velocity
        expected_weeks = expected_sprints * weeks_per_sprint

        return expected_sprints, expected_weeks


 
    


    