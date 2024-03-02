template = """ 
For the following text, extract the following information:

Warning: Don't greet or write any introduction. Just start with the answer to the prompts. Do as per the instructions given in the prompt. If you don't know the answer, leave that part (keep blank) and move to the next part.

1. Education: Extract the name of the all universities/colleges attended by the candidate with there CGPA.


2. Work: Extract all organization names where he/she has worked along with the position held, and the duration of employment.
            Predicted Skills : Also extract skills based on the work experience.
            Standardized Job Title: Identify the standardized job title for each work experience.
            Standardized Job Title: Identify the standardized job title for each work experience.Skills based on work experience
        
3. Projects: Extract the details of the projects the candidate has worked on.
                Predicted Skills : Also extract skills based on each project.
        
        
4.Skills: Identify the technical and non-technical skills associated with each work experience and project.


5.Career Trajectory: Identify the career progression of the candidate based on their work experience.

Output them in the following format: 
Warning: if there is no data for any of the fields, leave it blank.

        "Education: " and separate multiple entries with new line .
        
        "Work: " Organization Name, Location, Position, Start Date - End Date 'and separate multiple entries with a comma.
            "Job Title: " Identify the  job title for each work experience. Clean and strip them off suffixes, prefixes and seniority.
           
            " Predicted Skills : " and separate multiple entries with a comma for each work experience.
        Note: Separate each work experience with a new line.
        Warning: Don't print this text - "Organization Name, Location, Position, Start Date - End Date" as it is in the output  .
          
        
        "Project Name, Start Date - End Date, Project Description " and separate multiple entries with a comma and a new line for each project. ( 
            " Predicted Skills : " and separate multiple entries with a comma for each project.
            Note:  Project Description should be in 30 to 40 words
                
        Note: Separate each project with a new line. 
        Warning: Don't print "Project Name, Start Date - End Date, Project Description"  as it is (text)  in the output .       
        
        "Skills: " Skills under the skills section.
                    Classify them as technical and non-technical skills if possible.
        
        "Career Trajectory: " and separate multiple entries with a -> . Career Trajectory should be in acsending order with respect to date of joining.
                eg1 : "Data Analyst -> Data Scientist -> Senior Data Scientist"
                eg2 : "School Name -> College Name -> University Name -> Job Title -> Job Title"
                
Resume: {text}

"""

template_format_instructions = """ 
For the following text, extract the following information:

Warning: Don't greet or write any introduction. Just start with the answer to the prompts. Do as per the instructions given in the prompt. If you don't know the answer, leave that part (keep blank) and move to the next part.

1. Education: Extract the name of the all universities/colleges attended by the candidate with there CGPA.


2. Work: Extract all organization names where he/she has worked along with the position held, and the duration of employment.
            Predicted Skills : Also extract skills based on the work experience.
            Job Title: Identify the  job title for each work experience.
            Job Title: Identify the  job title for each work experience.Skills based on work experience
            Note: One work at a time with its Predicted Skills and Job Title

3. Projects: Extract the details of the projects the candidate has worked on.
                Predicted Skills : Also extract skills based on each project.


4.Skills: Identify the technical and non-technical skills associated with each work experience and project.


5.Career Trajectory: Identify the career progression of the candidate based on their work experience.

Output them in the following format: 
Warning: if there is no data for any of the fields, leave it blank.

        "Education: " and separate multiple entries with new line .

        "Work: " Organization Name, Location, Position, Start Date - End Date 'and separate multiple entries with a comma.
            "Job Title: " Identify the  job title for each work experience. Clean and strip them off suffixes, prefixes and seniority.

            " Predicted Skills : " and separate multiple entries with a comma for each work experience.
        Note: Separate each work experience with a new line.
        Warning: Don't print this text - "Organization Name, Location, Position, Start Date - End Date" as it is in the output  .
            Note: One work at a time with its Predicted Skills and Job Title


        "Project Name, Start Date - End Date, Project Description " and separate multiple entries with a comma and a new line for each project. ( 
            " Predicted Skills : " and separate multiple entries with a comma for each project.
            Note:  Project Description should be in 30 to 40 words

        Note: Separate each project with a new line. 
        Warning: Don't print "Project Name, Start Date - End Date, Project Description"  as it is (text)  in the output .       

        "Skills: " Skills under the skills section.
                    Classify them as technical and non-technical skills if possible.

        "Career Trajectory: " and separate multiple entries with a -> . Career Trajectory should be in ascending order with respect to date of joining.
                eg1 : "Data Analyst -> Data Scientist -> Senior Data Scientist"
                eg2 : "School Name -> College Name -> University Name -> Job Title -> Job Title"
                Note :  job titles  , school names or College/University are permissible in  Career Trajectory

Resume: {text}

\n{format_instructions}\n

"""
