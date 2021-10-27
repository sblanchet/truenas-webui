# coding=utf-8
"""SCALE High Availability (tn-bhyve01) feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
    parsers
)
from function import (
    wait_on_element,
    is_element_present,
    attribute_value_exist,
    wait_on_element_disappear,
    run_cmd,
    post
)


@scenario('features/NAS-T964.feature', 'Create an SMB share with the Active Directory dataset')
def test_create_an_smb_share_with_the_active_directory_dataset(driver):
    """Create an SMB share with the Active Directory dataset."""


@given(parsers.parse('the browser is open, navigate to "{host}"'))
def the_browser_is_open_navigate_to_host(driver, host):
    """the browser is open, navigate to "{host}"."""
    if host not in driver.current_url:
        driver.get(f"http://{host}/ui/sessions/signin")
        assert wait_on_element(driver, 10, '//input[@data-placeholder="Username"]')


@when(parsers.parse('the login page appears, enter "{user}" and "{password}"'))
def the_login_page_appears_enter_root_and_password(driver, user, password):
    """the login page appears, enter "root" and "password"."""
    global root_password
    root_password = password
    if not is_element_present(driver, '//mat-list-item[@ix-auto="option__Dashboard"]'):
        assert wait_on_element(driver, 10, '//input[@data-placeholder="Username"]')
        driver.find_element_by_xpath('//input[@data-placeholder="Username"]').clear()
        driver.find_element_by_xpath('//input[@data-placeholder="Username"]').send_keys(user)
        driver.find_element_by_xpath('//input[@data-placeholder="Password"]').clear()
        driver.find_element_by_xpath('//input[@data-placeholder="Password"]').send_keys(password)
        assert wait_on_element(driver, 5, '//button[@name="signin_button"]', 'clickable')
        driver.find_element_by_xpath('//button[@name="signin_button"]').click()
    else:
        assert wait_on_element(driver, 5, '//mat-list-item[@ix-auto="option__Dashboard"]', 'clickable')
        driver.find_element_by_xpath('//mat-list-item[@ix-auto="option__Dashboard"]').click()


@then('on the dashboard, click on Shares on the left sidebar')
def on_the_dashboard_click_on_shares_on_the_left_sidebar(driver):
    """on the dashboard, click on Shares on the left sidebar."""
    assert wait_on_element(driver, 7, '//h1[text()="Dashboard"]')
    assert wait_on_element(driver, 10, '//span[contains(text(),"System Information")]')
    assert wait_on_element(driver, 5, '//mat-list-item[@ix-auto="option__Shares"]', 'clickable')
    driver.find_element_by_xpath('//mat-list-item[@ix-auto="option__Shares"]').click()


@then('on the Sharing page, click Add on Windows Shares(SMB)')
def on_the_sharing_base_click_add_on_windows_sharessmb(driver):
    """on the Sharing base, click Add on Windows Shares(SMB)."""
    assert wait_on_element(driver, 7, '//h1[text()="Sharing"]')
    assert wait_on_element(driver, 5, '//a[contains(text(),"Windows (SMB) Shares")]')
    assert wait_on_element(driver, 5, '//span[contains(.,"Windows (SMB) Shares")]//button[contains(.,"Add")]', 'clickable')
    driver.find_element_by_xpath('//span[contains(.,"Windows (SMB) Shares")]//button[contains(.,"Add")]').click()


@then(parsers.parse('on the Add SMB side box, set the Path to "{path}"'))
def on_the_add_smb_side_box_set_the_path_to_mntdozermy_acl_dataset(driver, path):
    """on the Add SMB side box, set the Path to "/mnt/dozer/my_ad_dataset"."""
    global dataset
    dataset = path
    assert wait_on_element(driver, 7, '//h3[text()="Add SMB"]')
    assert wait_on_element(driver, 5, '//input[@ix-auto="input__Description"]')
    assert wait_on_element(driver, 5, '//input[@ix-auto="input__path"]', 'inputable')
    driver.find_element_by_xpath('//input[@ix-auto="input__path"]').send_keys(path)


@then(parsers.parse('input "{share_name}" as name, click to enable'))
def input_myadsmbshare_as_name_click_to_enable(driver, share_name):
    """input "myadsmbshare" as name, click to enable."""
    assert wait_on_element(driver, 5, '//input[@ix-auto="input__Name"]', 'clickable')
    driver.find_element_by_xpath('//input[@ix-auto="input__Name"]').clear()
    driver.find_element_by_xpath('//input[@ix-auto="input__Name"]').send_keys(share_name)
    assert wait_on_element(driver, 5, '//mat-checkbox[@ix-auto="checkbox__Enabled"]', 'clickable')
    if not attribute_value_exist(driver, '//mat-checkbox[@ix-auto="checkbox__Enabled"]', 'class', 'mat-checkbox-checked'):
        driver.find_element_by_xpath('//mat-checkbox[@ix-auto="checkbox__Enabled"]').click()


@then(parsers.parse('input "{description}" as the description, click Save'))
def input_my_active_directory_smb_share_as_the_description_click_save(driver, description):
    """input "My Active Directory SMB share" as the description, click Save."""
    driver.find_element_by_xpath('//input[@ix-auto="input__Description"]').send_keys(description)
    assert wait_on_element(driver, 5, '//button[@ix-auto="button__SAVE"]', 'clickable')
    driver.find_element_by_xpath('//button[@ix-auto="button__SAVE"]').click()
    assert wait_on_element(driver, 5, '//h6[contains(.,"Please wait")]')
    assert wait_on_element_disappear(driver, 30, '//h6[contains(.,"Please wait")]')


@then('when Enable service box appears, click ENABLE SERVICE')
def when_enable_service_box_appears_click_enable_service(driver):
    """when Enable service box appears, click ENABLE SERVICE."""
    assert wait_on_element(driver, 7, '//h1[text()="Enable service"]')
    assert wait_on_element(driver, 5, '//button[contains(.,"ENABLE SERVICE")]', 'clickable')
    driver.find_element_by_xpath('//button[contains(.,"ENABLE SERVICE")]').click()
    assert wait_on_element(driver, 7, '//h1[contains(text(),"SMB Service")]')
    assert wait_on_element(driver, 5, '//button[contains(.,"Close")]', 'clickable')
    driver.find_element_by_xpath('//button[contains(.,"Close")]').click()


@then(parsers.parse('the "{share_name}" should be added on the Sharing page'))
def the_myadsmbshare_should_be_added_on_the_sharing_page(driver, share_name):
    """the "myadsmbshare" should be added on the Sharing page."""
    assert wait_on_element(driver, 5, '//h1[text()="Sharing"]')
    assert wait_on_element(driver, 5, f'//div[text()="{share_name}"]')


@then('click on System Settings on the left sidebar, then click Services')
def click_on_system_settings_on_the_left_sidebar_then_click_services(driver):
    """click on System Settings on the left sidebar, then click Services."""
    assert wait_on_element(driver, 5, '//mat-list-item[@ix-auto="option__System Settings"]', 'clickable')
    driver.find_element_by_xpath('//mat-list-item[@ix-auto="option__System Settings"]').click()
    assert wait_on_element(driver, 5, '//div[contains(@class,"lidein-nav-md")]//mat-list-item[@ix-auto="option__Services"]', 'clickable')
    driver.find_element_by_xpath('//div[contains(@class,"lidein-nav-md")]//mat-list-item[@ix-auto="option__Services"]').click()


@then('on the Service page, verify SMB service is started')
def on_the_Service_page_verify_smb_service_is_started(driver):
    """on the Service page, verify SMB service is started."""
    assert wait_on_element(driver, 7, '//h1[text()="Services"]')
    assert wait_on_element(driver, 5, '//div[@ix-auto="overlay__stateSSH"]', 'clickable')
    assert attribute_value_exist(driver, '//mat-slide-toggle[@ix-auto="slider__state__SSH"]', 'class', 'mat-checked')


@then(parsers.parse('send a file to the share with "{host}"/"{share_name}" and "{ad_user}"%"{ad_password}"'))
def send_a_file_to_the_share(driver, host, share_name, ad_user, ad_password):
    """send a file to the share with "{host}"/"{share}" and "{ad_user}"%"{ad_password}"."""
    run_cmd('touch testfile.txt')
    results = run_cmd(f'smbclient //{host}/{share_name} -W AD01 -U {ad_user}%{ad_password} -c "put testfile.txt testfile.txt"')
    run_cmd('rm testfile.txt')
    assert results['result'], results['output']


@then(parsers.parse('verify that the file is on "{host}"'))
def verify_that_the_file_is_on_host(driver, host):
    """verify that the file is on "host"."""
    file = f'{dataset}/testfile.txt'
    results = post(host, '/filesystem/stat/', ('root', root_password), file)
    assert results.status_code == 200, results.text
