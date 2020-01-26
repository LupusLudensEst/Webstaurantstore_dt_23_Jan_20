# Webstaurantstore_dt_23_Jan_20
Webstaurantstore_dt_23_Jan_20
WebstaurantStore Code Screen Task

Preconditions:
Runnable on: Windows 10
Browser: Chrome
Tools: Java, Selenium Webdriver

Testcase steps:
1.	Go to https://www.webstaurantstore.com/
2.	Search for 'stainless work table'.
3.	Check the search result ensuring every product item has the word 'Table' its title.
4.	Add the last of found items to Cart.
5.	Empty Cart.

Please put your code to GitHub.com and send the project link.

Thank you.
===========================================================================================
If you will install allure(java should be here)-you would be able to see the visual report. 
See steps:
$ pip install allure-behave
$ pip install allure-pytest
$ pip install pytest-allure-adaptor

to launch tests and generate reports folder: 
$ behave -f allure_behave.formatter:AllureFormatter -o test_results/ features/
to extract report into browser: 
$ allure serve test_results/
