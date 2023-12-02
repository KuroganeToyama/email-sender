# Email Sender
So a while ago, I worked on this small project (https://github.com/KuroganeToyama/email-sender-test), which turned out somewhat okay.
<br><br>
Until my senpai Mark Gasior showed me the power of Linux with `mutt`.
<br><br>
This script was originally developed by him, so 95% of the credit goes to him.
<br><br>
But Mark didn't have much care for email styling and I did.
<br><br>
So I upgraded his script with custom HTML (apparently I can't do that with the subject line cause `mutt` isn't so good with RTF).
<br><br>
And we both agreed that my HTML looked fantastic (not really but it looks nice for sending remark requests responses).
<br><br>
So once again, praise my senpai Mark Gasior and his expertise with Linux.

# Usage
`python html_send_remark_requests.py`

# Notes
Note 1: The script was done a long time ago, I just kinda forgot to show it on my GitHub. Being an ISA is a lot more busy than you might think.
<br><br>
Note 2: Yeah, I'm aware I could have set the script to accept the CSV as an argument, instead of modifying the script, but it's such a minor change that I didn't really bother to do so.
<br><br>
Note 3: `pandas` was used because it was more convenient for extracting all data on each row.
<br><br>
Note 4: How come Fall 2023 is the first time an auto-email script was used to send remark requests responses, which had like 50 of them on every single assignment?