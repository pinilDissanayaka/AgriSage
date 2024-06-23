# SCREEN NAME: AgriSage Login Page

## PREPARED BY
Team Agri Sage

## DESIGNATION
Undergraduate

## DATE
23.06.2024

## SCENARIO ID: SC_01
**SCENARIO DESCRIPTION:** Login while Credential entering

---

## Requirement Description:
Users should be able to create an account and log in to the system.

**Priority:** High

**Acceptance Criteria:**
- User can access the login page from the homepage.
- User can enter their credentials and click the "login" button.
- User is redirected to their account dashboard upon successful login.

---

## User Stories:
1. As a new user, I want to be able to create a new account and login to the platform.
2. As an existing user, I want to be able to easily access my account by entering my login credentials.

---

## Test Cases:

| TEST CASE ID | TEST CASE DESCRIPTION                                      | PRECONDITION                                   | TEST DATA                                    | EXPECTED RESULT                                            | POSTCONDITION                                | ACTUAL RESULT                                | STATUS |
|--------------|-------------------------------------------------------------|------------------------------------------------|----------------------------------------------|------------------------------------------------------------|----------------------------------------------|----------------------------------------------|--------|
| TC_001       | Verify page title and logo                                  | Page is loaded                                | N/A                                          | Title is "AGRISAGE / Login" and logo is displayed            | N/A                                          | Title and logo displayed as expected         | Pass   |
| TC_002       | Verify presence of username and password fields             | Page is loaded                                | N/A                                          | Username and Password input fields are present and visible    | N/A                                          | Fields present and visible as expected       | Pass   |
| TC_003       | Attempt login with valid username and password              | User is on login page                         | Valid username and password                   | User is logged in successfully                              | User is redirected to the dashboard or main page | Successfully logged in                       | Pass   |
| TC_004       | Attempt login with invalid username and/or password         | User is on login page                         | Invalid username or password                 | Error message "Invalid username or password" displayed       | User remains on the login page with error message | Error message displayed as expected          | Pass   |
| TC_005       | Verify "Remember me" functionality                          | User is on login page                         | Checkbox checked                             | Session remembers user credentials upon next visit           | User's session persists with login credentials pre-filled | Session persisted with remembered credentials | Pass   |
| TC_006       | Verify "Forgot Password" link functionality                 | User is on login page                         | Click on "Forgot Password" link              | User is redirected to password reset page                    | User sees the password reset page             | Redirected to password reset page as expected | Pass   |
| TC_007       | Verify "Create an account" link functionality               | User is on login page                         | Click on "Create an account" link            | User is redirected to the registration page                  | User sees the registration page               | Redirected to registration page as expected  | Pass   |
| TC_008       | Attempt login without entering username and/or password     | User is on login page                         | Username and/or password fields are empty    | Error messages "Please enter your username" and "Please enter your password" displayed | User remains on login page with error messages | Error messages displayed as expected         | Pass   |
| TC_009       | Verify error message display for incorrect form submission | User has submitted incorrect login details  | Invalid username or password                 | Error message is displayed near the respective field         | User remains on login page with error message | Error message displayed as expected          | Pass   |
| TC_010       | Verify link to external resources (credits link)            | User is on login page                         | Click on "Designed by Team - AGRISAGE" link | User is redirected to the external resource page (e.g., team page) | User sees the external resource page         | Redirected to external resource page as expected | Pass   |

---

## Test Environment - AgriSage Project

**Test environment is the setup in which testing is performed. It includes hardware, software, and network configurations required for testing.**

### Hardware:
- Computers: Desktop computers with configurations suitable for running web applications, including adequate RAM and processing power.
- Mobile Devices: Various mobile devices (iOS and Android) for testing the responsiveness and compatibility of the AgriSage web application.
- IoT Sensors: Hardware devices equipped with IoT sensors (for soil moisture, temperature, etc.) used in conjunction with the AgriSage IoT integration.

### Software:
- Web Browsers: Latest versions of web browsers including Chrome, Firefox, and Safari to ensure cross-browser compatibility.
- Operating Systems: Windows, macOS, and Linux distributions to verify platform independence of AgriSage.
- Development Tools: Integrated Development Environments (IDEs) such as Visual Studio Code, software frameworks (Node.js, React), and version control systems (Git) used in AgriSage development.
- Testing Tools: Selenium for automated browser testing, JMeter for performance testing, Bugzilla for issue tracking and management.

### Network:
- Internet Connectivity: High-speed internet connection to simulate real-world usage scenarios and ensure responsiveness of AgriSage.
- Firewall Settings: Configured to simulate different network conditions and ensure that AgriSage operates securely.
- Security Settings: SSL certificates implemented to encrypt data transmission and secure transactions during testing.

### Data:
- User Data: Sample user profiles and data to simulate various user interactions and scenarios within AgriSage.
- Product Data: Comprehensive database of agricultural products, their specifications, and details required for AgriSage functionalities.
- Order Data: Test orders and transaction data to validate the ordering process, payment gateways, and order management features.
