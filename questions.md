# 🏁 Capstone Assignment / Final Project

In this assignment, you’ll submit the work you completed as part of the Full-stack development Capstone project, where you took on the role of a full-stack developer for **Cars Dealership**, a national car retailer in the U.S. 

In that project, you built a responsive web application that displayed dealership branches and allowed users to view and submit reviews. You developed both the frontend and backend using technologies like **React, Django, Flask, Node.js, MongoDB, and SQLite**, and deployed the application with **Docker, Kubernetes, and IBM Cloud Code Engine**.

Through this project, you applied your skills in version control, CI/CD with GitHub Actions, responsive UI design, microservices architecture, and sentiment analysis.

---

## 📋 Instructions

### Steps to complete this assignment successfully:
1. **Complete the capstone project**, ensuring all tasks are completed and your work is saved in the correct files.
2. Click **Begin the Assignment** to start.
3. **Read each question carefully**, then submit your answers with the required GitHub URLs and cURL command outputs.
4. After responding to all questions, select **Submit Assignment**.
5. **Review the feedback** once it’s available to see how you performed and where you can improve.

---

## 🏆 Grading Criteria

> 💡 **Overview:** The capstone project consists of **28 tasks**, carrying a total of **50 points**. You will be graded as per the following grading criteria:

### 🟢 Phase 1: Core Configuration & Static Frontends
*   **Task 1:** Submit the public GitHub URL of the `README.md` file that contains the Project name details. `(1 point)`
*   **Task 2:** Copy and paste the terminal output saved in the file named `django_server`, showing the Django server running. `(1 point)`
*   **Task 3:** Submit the public GitHub URL of the `server/frontend/static/About.html` file showing the updated “About Us” page with correct CSS links, realistic images, names, roles, brief details, and email IDs. `(3 points)`
*   **Task 4:** Submit the public GitHub URL of the `server/frontend/static/Contact.html` file showing the “Contact Us” page of your Django app which you created with updated CSS links, navigation bar (active on Contact Us), images, and all required contact details. `(2 points)`

---

### 🟡 Phase 2: User Authentication & Direct API Testing
*   **Task 5:** Copy and paste the cURL command and its output, saved in a file named `loginuser`, which performs a login operation using any valid username and password. `(2 points)`
*   **Task 6:** Copy and paste the cURL command and its output, saved in a file named `logoutuser`, which performs the logout operation for the logged-in user. `(2 points)`
*   **Task 7:** Submit the public GitHub URL of the `server/frontend/src/components/Register/Register.jsx` file showing the “Sign-up” page of your Django/React application with all five input fields *(Username, First Name, Last Name, Email, Password)* and the Register button. `(1 point)`

---

### 🔵 Phase 3: NoSQL Services & Regional Dealership Data
*   **Task 8:** Copy and paste the cURL command and its output, saved in a file named `getdealerreviews`, which displays the review(s) for any dealer ID. `(2 points)`
*   **Task 9:** Copy and paste the cURL command and its output, saved in the file named `getalldealers`, which displays all dealer(s) retrieved. `(2 points)`
*   **Task 10:** Copy and paste the cURL command and its output, saved in a file named `getdealerbyid`, which displays the details of any dealer ID. `(2 points)`
*   **Task 11:** Copy and paste the cURL command and its output, saved in the file named `getdealersbyState`, which displays the dealer(s) located in the state of Kansas. `(2 points)`

---

### 🟣 Phase 4: Administrative Security & Inventory Models
*   **Task 12:** Submit the screenshot (`admin_login.png` or `admin_login.jpeg`) showing the root user login on the admin page. `(2 points)`
*   **Task 13:** Submit the screenshot (`admin_logout.png` or `admin_logout.jpeg`) showing the root user logged out from the admin page. `(1 point)`
*   **Task 14 and 15:** Copy and paste the cURL command and its output, saved in the file named `getallcarmakes`, which displays all car makes and models retrieved. `(4 points)`

---

### 🟤 Phase 5: Machine Learning Microservices & Local UI Validation
*   **Task 16:** Copy and paste the cURL command and its output, saved in the file named `analyzereview`, which displays the sentiment analysis result for the review text *"Fantastic services"*. `(2 points)`
*   **Task 17:** Submit the screenshot (`get_dealers.png` or `get_dealers.jpeg`) showing the dealers on the home page of the Django application before logging in. `(1 point)`
*   **Task 18:** Submit a screenshot showing the dealers displayed on the home page of the Django application after logging in, with the image name `get_dealers_loggedin`. *The screenshot must clearly show the Review Dealer option, the logged-in username, and the endpoint visible in the browser address bar.* `(2 points)`
*   **Task 19:** Submit the screenshot (`dealersbystate.png` or `dealersbystate.jpeg`) showing the dealers filtered by the State on the home page of the Django application. *Please ensure that the endpoint is visible in the browser address bar.* `(2 points)`

---

### 🟠 Phase 6: Client Engagement & Submission Verification
*   **Task 20:** Submit a screenshot showing the selected dealer details on the dealer page, along with the reviews, with the image name `dealer_id_reviews` *(saved as .png or .jpeg)*. *The screenshot must clearly display the endpoint visible in the browser address bar.* `(1 point)`
*   **Task 21:** Submit a screenshot showing the Post Review page after entering the review details, before submission, with the image name `dealership_review_submission`. `(1 point)`
*   **Task 22:** Submit a screenshot showing the posted review, with the image name `added_review`. `(2 points)`

---

### 🔴 Phase 7: Automation Pipelines & Cloud Native Deployment
*   **Task 23:** Copy and paste the terminal output saved in the file named `CICD` that shows your GitHub Actions workflow running successfully. *The output should clearly display the steps executed in the workflow.* `(3 points)`
*   **Task 24:** Submit the deployment URL for your Django application saved in the file named `deploymentURL`. `(1 point)`
*   **Task 25:** Submit a screenshot showing the deployed landing page, with the image name `deployed_landingpage`. `(2 points)`
*   **Task 26:** Submit a screenshot showing the deployed logged-in page, with the image name `deployed_loggedin`. *The screenshot must clearly display the username of the logged-in user.* `(2 points)`
*   **Task 27:** Submit a screenshot showing the dealer details page opened through your deployment, with the image name `deployed_dealer_detail`. `(2 points)`
*   **Task 28:** Submit a screenshot showing the review displayed in your deployed application, with the image name `deployed_add_review`. `(2 points)`
