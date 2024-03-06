Enigma Scanner is a Web Vulnerability Scanner. 

It scans for 4 security checks:
1. Path Traversal.
2. Security Header.
3. SQL Injection.
4. Information Disclosure.

At the end of scanning it also generates a dynamic report.

This scanner was build with refrence to portswigger.

First of all we have to login only google authentication.

once logged in.
![image](https://github.com/Samellufy/Enigma-Scanner/assets/100872010/9f0b28d1-7daf-4d97-bfa0-96a1f189e201)
This is the user interface, the main functionality is in scan tab.
![image](https://github.com/Samellufy/Enigma-Scanner/assets/100872010/eaa557bd-0992-4060-b12b-29361305567f)
If user is not a asubscribed user then scanner will check only for two security flaw i.e information disclosure, security headers.
For showcase i will be using the blind time based sql injection lab from port swigger.
![image](https://github.com/Samellufy/Enigma-Scanner/assets/100872010/fe493854-5ac4-4da3-8ece-ef270e9a4f63)
![image](https://github.com/Samellufy/Enigma-Scanner/assets/100872010/e68772ec-2655-4c85-9385-12bc7e0d9cbd)
![image](https://github.com/Samellufy/Enigma-Scanner/assets/100872010/cfe8ed30-ce4c-4c9b-bb43-dc1609aa0f62)
![image](https://github.com/Samellufy/Enigma-Scanner/assets/100872010/5d3c9f92-0c8c-473a-9f38-4f527ee24b9f)
Now as a subscribed user.
![image](https://github.com/Samellufy/Enigma-Scanner/assets/100872010/53a46d25-cebb-4035-aa75-929a041bbeec)
![image](https://github.com/Samellufy/Enigma-Scanner/assets/100872010/56a15249-1848-48c1-ab0d-ba155ec6f8cc)
![image](https://github.com/Samellufy/Enigma-Scanner/assets/100872010/d3646185-4f2a-45ff-ab7f-a5ed3e8a25f6)
![image](https://github.com/Samellufy/Enigma-Scanner/assets/100872010/b789266a-e874-4f15-b62c-9e5873a66081)
![image](https://github.com/Samellufy/Enigma-Scanner/assets/100872010/a868e370-a413-45d3-a3f3-701227f03752)
![image](https://github.com/Samellufy/Enigma-Scanner/assets/100872010/3a3d1587-7167-4025-baf5-e532959ef134)
Download report is the main function that the subscribed user has.
![image](https://github.com/Samellufy/Enigma-Scanner/assets/100872010/b40ecbcc-9208-497b-8f81-25299515b908)


Report can be viewed in pdf format.
![image](https://github.com/Samellufy/Enigma-Scanner/assets/100872010/692e3673-cd57-4aa0-bb05-71fe470188ff)


In the report the pie is generated which is also dynamic based on the detected vulnerabilities.
![image](https://github.com/Samellufy/Enigma-Scanner/assets/100872010/67dec723-ff03-4a11-b029-3af7cf35e831)
![image](https://github.com/Samellufy/Enigma-Scanner/assets/100872010/29d70634-95d1-4a84-acb7-259fd343fa0a)


Below is the working in the backend how the scanner is checking for the security flaw (vulnerability) within the website.
![image](https://github.com/Samellufy/Enigma-Scanner/assets/100872010/38b81213-d1cb-4915-8fb1-6bfebfe62c0b)


Example report you can download it from the above which is named as report.pdf

