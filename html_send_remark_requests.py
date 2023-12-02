import pandas as pd
import os
import time

subject = "Remark Request Response"

file = "Path to CSV file for remark request responses"

df = pd.read_csv(file)

for (numid, line) in df.iterrows():
    (student_id, name, qns, request, response) = line

    print(f"Sending email to {student_id}")

    html_email = f"""
    <body style = "font-family: Arial, sans-serif;">
        Here is the response to your remark request.
        <div style = "border: 1px outset black; padding: 15px 15px 10px 15px; margin: 15px 15px 15px 0px;">
            <h3> Original Request </h3>
            <p>{request}</p>
        </div>

        <div style = "border: 1px outset black; padding: 15px 15px 10px 15px; margin: 15px 15px 15px 0px;">
            <h3> Our Response </h3>
            <p>{response}</p>
        </div>

        <b> Kind regards, </b> <br>
        <b> CS 135 ISA Team </b> <br>
    </body>
    """

    os.system(f'mutt -e "set content_type=text/html" -s "{subject}" {student_id}@uwaterloo.ca << EOF \n {html_email}')

    # Linux server might get wacky when mutt executes multiple email sendings at once, 
    # so time interval is included for safety purposes.
    time.sleep(2)

