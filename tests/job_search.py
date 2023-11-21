import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class JobSearch(unittest.TestCase):
    """
    A Selenium test suite to automate job search on the Veeam careers website.

    Attributes:
        driver (webdriver.Chrome): The Selenium WebDriver for Chrome.

    Methods:
        setUp(self): Set up the WebDriver before each test.
        test_search_job(self): Test method to perform job search on the Veeam careers website.
        tearDown(self): Clean up and close the WebDriver after each test.
    """

    def setUp(self):
        """
        Set up the WebDriver before each test.
        This method initializes the Selenium WebDriver with the Chrome browser.
        """
        self.driver = webdriver.Chrome()

    def test_search_job(self):
        """
        Test method to perform job search on the Veeam careers website.
        This method navigates to the Veeam careers page, accepts cookies, selects
        the 'Research & Development' department, filters jobs by language, and
        asserts that the number of jobs matches the expected number.
        """
        driver = self.driver

        # Navigate to the Veeam careers page
        driver.get("https://cz.careers.veeam.com/vacancies")
        self.assertIn("Veeam", driver.title)
        driver.maximize_window()

        # Accept cookies
        wait = WebDriverWait(driver, 20)
        cookies_locator = (By.XPATH, "//div[@id='cookiescript_accept']")
        cookies_btt = wait.until(ec.element_to_be_clickable(cookies_locator))
        driver.get_screenshot_as_file("cookies1.png")
        cookies_btt.click()
        driver.get_screenshot_as_file("cookies2.png")

        # Get the expected number of jobs
        expected_job_number = driver.find_element(By.CSS_SELECTOR, ".text-secondary.pl-2").text
        print("Expected Job Number: ", expected_job_number)

        # Select 'Research & Development' department
        department = driver.find_element(By.XPATH, "(//button[normalize-space()='All departments'])[1]")
        department.click()
        department_re = driver.find_element(By.XPATH, "//a[normalize-space()='Research & Development']")
        department_re.click()
        driver.get_screenshot_as_file("file.png")

        # Filter jobs by language
        language = driver.find_element(By.XPATH, "(//button[normalize-space()='All languages'])[1]")
        language.click()
        driver.get_screenshot_as_file("file2.png")
        wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, "label[for='lang-option-0']"))).click()
        driver.get_screenshot_as_file("file3.png")

        # Get the actual number of jobs after filtering
        job_number = driver.find_element(By.CSS_SELECTOR, ".text-secondary.pl-2").text

        # Assert that the actual number of jobs matches the expected number
        self.assertEqual(expected_job_number, job_number, "The number of jobs available is:" + job_number)

    def tearDown(self):
        """
        Clean up and close the WebDriver after each test.
        This method is called after each test to close the WebDriver and perform cleanup.
        """
        self.driver.close()


if __name__ == "__main__":
    # Run the test suite
    unittest.main()
