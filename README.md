# Repository_11
Automation pom 
1. Project Objective:
The goal of this project is to automate the login and logout functionality of the Classify Zenclass application using Selenium WebDriver and PyTest framework.
The project includes both positive and negative test scenarios as well as UI validations according to the requirements.


2.Feature and Description:

1.Successful Login- Valid credentials should log into the application.

2.Unsuccessful Login- Invalid credentials should display an error message.

3.Username Field Validation- Field must be present and visible.

4.Password Field Validation- Field must be present and visible.

5.Login Button UI Validation- Login button must be clickable/enabled.

6.Logout Functionality- User must be able to logout successfully.



3.Tools & Technologies:

Tool and Purpose
1.Python- Programming Language

2.Selenium WebDriver - Browser Automation

3.PyTest - Test Execution Framework

4.Page Object Model - Framework Design Pattern

5.HTML Report Plugin - Reporting & Results



4.Test Cases Included:
✅ Successful Login
Enter valid username & password
Assert the landing page URL contains “classify”

❌ Unsuccessful Login
Enter invalid username/password
Verify error message contains “incorrect”


5.✳️ UI Validation Tests:
Test and Validation Logic
Username input field visible- Assert element is visible
Password input field - Assert element is visible
Login button clickable- Assert clickable/enabled



6.🔁 Logout Functionality:
Do login and then perform logout
Click logout button
Assert page redirects back to login page


7.Conclusion:
The login system for the Classify application works as expected.
All functional and UI validations passed successfully.
Logout feature redirects user safely back to login page.
The automation framework is reusable, scalable, and ready for future test case additions.



