# app.py - The main executable file
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from time import sleep
from Test_locators import locators
from Test_data import data
import pytest


class Test_Logimax:
    @pytest.fixture
    

    def booting_function(self):
       self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
       self.driver.get(data.Logi_Data().url)
       self.driver.maximize_window()
       self.driver.implicitly_wait(5)
  
    
   
    def test_Billing(self,booting_function):   
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().username_inputBox).send_keys(data.Logi_Data().username)
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().password_inputBox).send_keys(data.Logi_Data().password)
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().signButton).click()
        sleep(20)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().side_bar).click()
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().customer_order).click()
        Clickable_Name = self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().customer_order).text
        assert self.driver.title == 'Logimax Technology | Admin'
        print('Clickable name :',Clickable_Name)
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().creat_order).click()
        sleep(5)
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().Add_order).click()
        sleep(5)
        customer = self.driver.find_element(by=By.ID,value=locators.Logi_Locators().Customer)
        sleep(10)
        customer.send_keys(data.Logi_Data().name)
        sleep(5)
        customer.send_keys(Keys.BACK_SPACE)
        sleep(10)
        se_ver = self.driver.find_elements(By.XPATH, "//ul[@id='ui-id-1']//li")
        #print('Total',len(se_ver))
        customer_name = data.Logi_Data().customer_name
        for element in se_ver:
            if element.text == customer_name:
                element.click()
                break
        assert self.driver.title == 'Logimax Technology | Admin'
        print('Customer name : {a}'.format(a = customer_name)) 
        sleep(5)
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().Order_Branch).click()
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().text_box).send_keys ('HEAD OFFICE')
        assert self.driver.title == 'Logimax Technology | Admin'
        print('Select Branch name : {a}'.format(a = 'HEAD OFFICE'))
        sleep(5)
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().Sales_Employee).click()
        sleep(5)
        employee = self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().text_box)
        employee.send_keys('111-Logimax Developer')
        employee.send_keys(Keys.RETURN) 
        assert self.driver.title == 'Logimax Technology | Admin'
        print('Sales Employee name  : {a}'.format( a='111-Logimax Developer'))
        sleep(5)
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().balance_type).click()
        type = self.driver.find_element(By.XPATH, '(//*[@for="metal_bal_type"])').text
        assert self.driver.title == 'Logimax Technology | Admin'
        print('Balance Type : {a}'.format( a=type ))
        sleep(5)
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().tag_order).click()
        tag_order = self.driver.find_element(By.XPATH, '(//*[@for="tag_order"])').text
        assert self.driver.title == 'Logimax Technology | Admin'
        print('Order Type : {a}'.format( a = tag_order ))
        sleep(5)
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().order_rate).click()
        order_rate = self.driver.find_element(By.XPATH, '(//*[@for="customer_order"])[2]').text
        assert self.driver.title == 'Logimax Technology | Admin'
        print('Rate Type : {a}'.format( a = order_rate ))
        sleep(5)
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().New_tag_scan).send_keys(data.Logi_Data().Tag_code)
        assert self.driver.title == 'Logimax Technology | Admin'
        print('New Tag Scan  : {a}'.format( a = data.Logi_Data().Tag_code))
        sleep(8)
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().Tag_search).click()
        #sleep(8)
        ''' self.driver.find_element(by=By.ID,value=locators.Logi_Locators().Gross_weight).send_keys(data.Logi_Data().G_weight)
        assert self.driver.title == 'Logimax Technology | Admin'
        print('Gross Weight: {a}'.format(a = data.Logi_Data().G_weight))    
        
        sleep(5)
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().Peace).send_keys(data.Logi_Data().Pcs)
        assert self.driver.title == 'Logimax Technology | Admin'
        print('No Of PCs: {a}'.format(a = data.Logi_Data().Pcs))
        sleep(5)
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().Wast).send_keys(data.Logi_Data().wast_percentage)
        assert self.driver.title == 'Logimax Technology | Admin'
        print('Wast percentage: {a}'.format(a = data.Logi_Data().wast_percentage))
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().Mc_type).click()
        sleep(5)
        Mc_type = self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().text_box)
        Mc_type.send_keys('piece')
        Mc_type.send_keys(Keys.RETURN) 
        assert self.driver.title == 'Logimax Technology | Admin'
        print('MC Type : {a}'.format( a = 'piece'))
        sleep(5)
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().Mc_value).clear()
        sleep(5)
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().Mc_value).send_keys(data.Logi_Data().value)
        assert self.driver.title == 'Logimax Technology | Admin'
        print('MC Value: {a}'.format(a = data.Logi_Data().value))
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().other_charge).click()
        sleep(5)
        Other_charge = Select(self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().Charge_name))
        Other_charge .select_by_value('2')
        selected_option = Other_charge.first_selected_option
        selected_text = selected_option.text
        assert self.driver.title == 'Logimax Technology | Admin'
        print('Charge Name : {a}'.format(a = selected_text))   
        sleep(5) 
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().value).clear()
        sleep(5) 
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().value).send_keys(data.Logi_Data().other_charge_value)
        assert self.driver.title == 'Logimax Technology | Admin'
        print('Other Charge Value : {a}'.format(a = data.Logi_Data().other_charge_value))
        sleep(5) 
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().Save_charge).click()'''
        sleep(20) 
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().description).click()
        sleep(5) 
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().item_description).send_keys(data.Logi_Data().items_describe)
        assert self.driver.title == 'Logimax Technology | Admin'
        print('Item Description: {a}'.format(a = data.Logi_Data().items_describe))
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().Add_description).click() 
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().Due_days).send_keys(data.Logi_Data().no_of_days)
        assert self.driver.title == 'Logimax Technology | Admin'
        print('No Of Due Days : {a}'.format(a = data.Logi_Data().no_of_days))
        sleep(5)
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().save_page).click() 
        assert self.driver.title == 'Logimax Technology | Admin'
        print('customer Order Create Successfully')
        sleep(10)
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().Order_Branch).click()
        sleep(5)
        branch = self.driver.find_element(by=By.XPATH,value=locators.Estimation_Locators().text_box)
        branch.send_keys(data.Estimation_Data().Branch)
        branch.send_keys(Keys.RETURN) 
        sleep(5)
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().Search).click()
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().order_search).send_keys(data.Logi_Data().Tag_code)
        sleep(5)
        order_no = (self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().Order_number).text)
        sleep(8)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().side_bar).click()
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Estimation_Locators().estimation).click()
        Select_option = self.driver.find_element(by=By.XPATH,value=locators.Estimation_Locators().estimation).text
        assert self.driver.title == 'Logimax Technology | Admin'
        print(f'Clickable Name : {Select_option}')
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Estimation_Locators().Add_Estimation).click()
        sleep(8)
        self.driver.find_element(by=By.ID,value=locators.Estimation_Locators().Order_Branch).click()
        sleep(5)
        branch = self.driver.find_element(by=By.XPATH,value=locators.Estimation_Locators().text_box)
        branch.send_keys(data.Estimation_Data().Branch)
        branch.send_keys(Keys.RETURN) 
        assert self.driver.title == 'Logimax Technology | Admin'
        print(f'Branch Name : {data.Estimation_Data().Branch}')
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Estimation_Locators().Sales_Employee).click()
        sleep(5)
        employee = self.driver.find_element(by=By.XPATH,value=locators.Estimation_Locators().text_box)
        employee.send_keys(data.Estimation_Data().Employee_name)
        employee.send_keys(Keys.RETURN) 
        assert self.driver.title == 'Logimax Technology | Admin'
        print(f'Employee Name : {data.Estimation_Data().Employee_name}')
        sleep(5)
        customer = self.driver.find_element(by=By.ID,value=locators.Estimation_Locators().Customer)
        sleep(10)
        customer.send_keys(data.Estimation_Data().name)
        sleep(5)
        customer.send_keys(Keys.BACK_SPACE)
        sleep(10)
        se_ver = self.driver.find_elements(By.XPATH, "//ul[@id='ui-id-1']//li")
        #print('Total',len(se_ver))
        customer_name = (data.Estimation_Data().customer_name)
        for element in se_ver:
            if element.text == customer_name:
                element.click()
                break
        assert self.driver.title == 'Logimax Technology | Admin'
        print(f'Customer Name : {customer_name}')     
             
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Estimation_Locators().Close).click()    
        sleep(5)
        self.driver.find_element(by=By.ID,value=locators.Estimation_Locators().old_metal).click()
        Estimation_item = self.driver.find_element(By.XPATH,'//label[text()="Old Metal "]').text
        assert self.driver.title == 'Logimax Technology | Admin'
        print(f'Estimation items : {Estimation_item}')
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Estimation_Locators().Metals).click()
        sleep(5)
        metals = self.driver.find_element(by=By.XPATH,value=locators.Estimation_Locators().text_box)
        metals.send_keys(data.Estimation_Data().Metals)
        metals.send_keys(Keys.RETURN) 
        assert self.driver.title == 'Logimax Technology | Admin'
        print(f'Metal Name : {data.Estimation_Data().Metals}')
        sleep(23)
        self.driver.find_element(by=By.XPATH,value=locators.Estimation_Locators().Metals_Type).click()
        sleep(5)
        Metals_Type = self.driver.find_element(by=By.XPATH,value=locators.Estimation_Locators().text_box)
        Metals_Type.send_keys(data.Estimation_Data().metals_Type)
        Metals_Type.send_keys(Keys.RETURN) 
        assert self.driver.title == 'Logimax Technology | Admin'
        print(f'Metals Type : {data.Estimation_Data().metals_Type}')
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Estimation_Locators().Category).click()
        sleep(5)
        Category = self.driver.find_element(by=By.XPATH,value=locators.Estimation_Locators().text_box)
        Category.send_keys(data.Estimation_Data().Category)
        Category.send_keys(Keys.RETURN) 
        sleep(5)
        self.driver.find_element(by=By.NAME,value=locators.Estimation_Locators().purity_metal).send_keys(data.Estimation_Data().purity_value)
        assert self.driver.title == 'Logimax Technology | Admin'
        print(f'purity metal : {data.Estimation_Data().purity_value}')
        sleep(5)
        self.driver.find_element(by=By.NAME,value=locators.Estimation_Locators().metal_G_wt).send_keys(data.Estimation_Data().Gross_wt_value)
        assert self.driver.title == 'Logimax Technology | Admin'
        print(f'Metals Gross Weight : {data.Estimation_Data().Gross_wt_value}')
        sleep(5)
        self.driver.find_element(by=By.NAME,value=locators.Estimation_Locators().metal_D_wt).send_keys(data.Estimation_Data().Dust_wt)
        assert self.driver.title == 'Logimax Technology | Admin'
        print(f'Metals Dust Weight : {data.Estimation_Data().Dust_wt}')
        sleep(5)
        self.driver.find_element(by=By.NAME,value=locators.Estimation_Locators().metal_wastage_percentage).send_keys(data.Estimation_Data().non_wastage_per)
        assert self.driver.title == 'Logimax Technology | Admin'
        print(f'Metals wastage percentage : {data.Estimation_Data().non_wastage_per}')
        sleep(20)

        self.driver.find_element(by=By.NAME,value=locators.Estimation_Locators().Remark).send_keys(data.Estimation_Data().remarks)   
        assert self.driver.title == 'Logimax Technology | Admin'
        print(f'Remark : {data.Estimation_Data().remarks}')
        sleep(8)
        
        self.driver.find_element(by=By.ID,value=locators.Estimation_Locators().save_print).click()
        assert self.driver.title == 'Logimax Technology | Admin'
        print("Estimation completed successfully")
        
        sleep(15)
        self.driver.switch_to.window(self.driver.window_handles[0])
        sleep(8)
        
        self.driver.find_element(by=By.ID,value=locators.Estimation_Locators().Order_Branch).click()
        sleep(5)
        branch = self.driver.find_element(by=By.XPATH,value=locators.Estimation_Locators().text_box)
        branch.send_keys(data.Estimation_Data().Branch)
        branch.send_keys(Keys.RETURN) 
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Estimation_Locators().order_search).send_keys(data.Estimation_Data().name)
        sleep(5)
        EST_no = (self.driver.find_element(by=By.XPATH,value=locators.Estimation_Locators().estimation_no).text)
        sleep(8)
        
        self.driver.find_element(by=By.XPATH,value=locators.Bill_locators().side_bar).click()
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Bill_locators().Billing).click()
        Clickable_option = self.driver.find_element(by=By.XPATH,value=locators.Bill_locators().Billing).text
        assert self.driver.title == 'Logimax Technology | Admin'
        print(f'Clickable option : {Clickable_option}')
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Bill_locators().Bill).click()
        sleep(5)
        Branch = Select (self.driver.find_element(by=By.ID,value=locators.Bill_locators().Branch))
        Branch.select_by_value('1')
        selected_option = Branch.first_selected_option
        selected_text = selected_option.text
        assert self.driver.title == 'Logimax Technology | Admin'
        print('Cost Centre name : {a}'.format(a = selected_text))
        sleep(5)
        self.driver.find_element(by=By.ID,value=locators.Bill_locators().Sales_Employee).click()
        sleep(5)
        employee = self.driver.find_element(by=By.XPATH,value=locators.Bill_locators().text_box)
        employee.send_keys('111-Logimax Developer')
        employee.send_keys(Keys.RETURN) 
        assert self.driver.title == 'Logimax Technology | Admin'
        print('billing Sales Employee name  : {a}'.format( a='111-Logimax Developer'))
        sleep(5)
        self.driver.find_element(by=By.ID,value=locators.Bill_locators().Order_advance).click()
        Sale_button = self.driver.find_element(By.XPATH, '(//*[@class="custom-label"])[5]').text
        assert self.driver.title == 'Logimax Technology | Admin'
        print('Billing to : {a}'.format( a= Sale_button))
        
        sleep(5)
        self.driver.find_element(by=By.ID,value=locators.Bill_locators().Esti).send_keys(EST_no)    
        assert self.driver.title == 'Logimax Technology | Admin'
        print('Estimation Number:',EST_no)
        sleep(5)
        self.driver.find_element(by=By.ID,value=locators.Bill_locators().search).click()
        sleep(5)
       
        self.driver.find_element(by=By.ID,value=locators.Bill_locators().Order_no).send_keys(order_no)    
        assert self.driver.title == 'Logimax Technology | Admin'
        print('Customer Order Number:',order_no)
        sleep(5)
        self.driver.find_element(by=By.ID,value=locators.Bill_locators().search_order_no).click()
        sleep(8)
        alert_messages = self.driver.find_elements(By.XPATH,"//div[contains(@class, 'alert-danger')]")

# Loop through the warning messages and close them
        for alert_message in alert_messages:
    # Find the close button within each warning message
           close_button = alert_message.find_element(By.XPATH,".//button[@class='close']")
    # Click the close button to dismiss the warning message
           close_button.click()
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Bill_locators().pop_close).click()
        sleep(5)
        self.driver.find_element(by=By.ID,value=locators.Bill_locators().Total_summary).click()
        sleep(5)
        self.driver.find_element(by=By.ID,value=locators.Bill_locators().Make_payment).click()
        sleep(5)
        self.driver.find_element(by=By.ID,value=locators.Bill_locators().billing_save).click()
        #bill = self.driver.find_element(by=By.ID,value=locators.Bill_locators().billing_save).text
        assert self.driver.title == 'Logimax Technology | Admin'
        print("Billing : Order Advance Option Run Successfully")
        
        sleep(15)
        self.driver.switch_to.window(self.driver.window_handles[0])
        sleep(8)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().side_bar).click()
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Estimation_Locators().estimation).click()
        Select_option = self.driver.find_element(by=By.XPATH,value=locators.Estimation_Locators().estimation).text
        assert self.driver.title == 'Logimax Technology | Admin'
        print(f'Clickable Name : {Select_option}')
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Estimation_Locators().Add_Estimation).click()
        sleep(8)
        self.driver.find_element(by=By.ID,value=locators.Estimation_Locators().Order_Branch).click()
        sleep(5)
        branch = self.driver.find_element(by=By.XPATH,value=locators.Estimation_Locators().text_box)
        branch.send_keys(data.Estimation_Data().Branch)
        branch.send_keys(Keys.RETURN) 
        assert self.driver.title == 'Logimax Technology | Admin'
        print(f'Branch Name : {data.Estimation_Data().Branch}')
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Estimation_Locators().Sales_Employee).click()
        sleep(5)
        employee = self.driver.find_element(by=By.XPATH,value=locators.Estimation_Locators().text_box)
        employee.send_keys(data.Estimation_Data().Employee_name)
        employee.send_keys(Keys.RETURN) 
        assert self.driver.title == 'Logimax Technology | Admin'
        print(f'Employee Name : {data.Estimation_Data().Employee_name}')
        sleep(5)
        customer = self.driver.find_element(by=By.ID,value=locators.Estimation_Locators().Customer)
        sleep(10)
        customer.send_keys(data.Estimation_Data().name)
        sleep(5)
        customer.send_keys(Keys.BACK_SPACE)
        sleep(10)
        se_ver = self.driver.find_elements(By.XPATH, "//ul[@id='ui-id-1']//li")
        #print('Total',len(se_ver))
        customer_name = (data.Estimation_Data().customer_name)
        for element in se_ver:
            if element.text == customer_name:
                element.click()
                break
        assert self.driver.title == 'Logimax Technology | Admin'
        print(f'Customer Name : {customer_name}')     
             
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Estimation_Locators().Close).click()    
        sleep(5)
        self.driver.find_element(by=By.ID,value=locators.Estimation_Locators().Tag).click()
        Estimation_item = self.driver.find_element(By.XPATH,'//label[text()="Tag "]').text
        assert self.driver.title == 'Logimax Technology | Admin'
        print(f'Estimation items : {Estimation_item}')
        sleep(5)
        self.driver.find_element(by=By.ID,value=locators.Estimation_Locators().Order_no_search).send_keys(order_no)
        sleep(5)
        self.driver.find_element(by=By.ID,value=locators.Estimation_Locators().Customer_order_search).click()
        sleep(5)
        Sale_Amount=[]
        Total_Amount = (self.driver.find_element(by=By.XPATH,value=locators.Estimation_Locators().Total_Sale_Amount)).text
        Sale_Amount.append(Total_Amount)
        Total_Sale_Amount = float(Sale_Amount[0])
        #print(Total_Sale_Amount)
        
        sleep(8)
        Paid_Amount = []
        Total_purchase = (self.driver.find_element(by=By.XPATH,value=locators.Estimation_Locators().Total_Advance_Paid_Amount)).text
        Paid_Amount.append(Total_purchase)
        Total_Purchase_Amount= float(Paid_Amount[0])
       # print(Total_Purchase_Amount)
        
        balance = Total_Purchase_Amount - Total_Sale_Amount
        balance_Amount = abs(round(balance))
        #print(balance_Amount)
        sleep(5)
        self.driver.find_element(by=By.ID,value=locators.Estimation_Locators().save_print).click()
        assert self.driver.title == 'Logimax Technology | Admin'
        print("Estimation completed successfully")
        
        sleep(10)
        self.driver.switch_to.window(self.driver.window_handles[0])
        sleep(5)
        
        self.driver.find_element(by=By.ID,value=locators.Estimation_Locators().Order_Branch).click()
        sleep(5)
        branch = self.driver.find_element(by=By.XPATH,value=locators.Estimation_Locators().text_box)
        branch.send_keys(data.Estimation_Data().Branch)
        branch.send_keys(Keys.RETURN) 
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Estimation_Locators().order_search).send_keys(data.Estimation_Data().name)
        sleep(5)
        est_order_no = (self.driver.find_element(by=By.XPATH,value=locators.Estimation_Locators().estimation_no).text)
        sleep(8)
        self.driver.find_element(by=By.XPATH,value=locators.Bill_locators().side_bar).click()
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Bill_locators().Billing).click()
        Clickable_option = self.driver.find_element(by=By.XPATH,value=locators.Bill_locators().Billing).text
        assert self.driver.title == 'Logimax Technology | Admin'
        print(f'Clickable option : {Clickable_option}')
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Bill_locators().Bill).click()
        sleep(5)
        Branch = Select (self.driver.find_element(by=By.ID,value=locators.Bill_locators().Branch))
        Branch.select_by_value('1')
        selected_option = Branch.first_selected_option
        selected_text = selected_option.text
        assert self.driver.title == 'Logimax Technology | Admin'
        print('Cost Centre name : {a}'.format(a = selected_text))
        sleep(5)
        self.driver.find_element(by=By.ID,value=locators.Bill_locators().Sales_Employee).click()
        sleep(5)
        employee = self.driver.find_element(by=By.XPATH,value=locators.Bill_locators().text_box)
        employee.send_keys('111-Logimax Developer')
        employee.send_keys(Keys.RETURN) 
        assert self.driver.title == 'Logimax Technology | Admin'
        print('billing Sales Employee name  : {a}'.format( a='111-Logimax Developer'))
        sleep(18)
        self.driver.find_element(by=By.ID,value=locators.Bill_locators().order_delivery).click()
        Sale_button = self.driver.find_element(By.XPATH, '(//*[@class="custom-label"])[8]').text
        assert self.driver.title == 'Logimax Technology | Admin'
        print('Billing to : {a}'.format( a= Sale_button))
        sleep(5)    
        self.driver.find_element(by=By.ID,value=locators.Bill_locators().Esti).send_keys(est_order_no)    
        assert self.driver.title == 'Logimax Technology | Admin'
        print('Estimation Number:',est_order_no)
        sleep(5)
        self.driver.find_element(by=By.ID,value=locators.Bill_locators().search).click()
        sleep(20)
        alert_messages = self.driver.find_elements(By.XPATH,"//div[contains(@class, 'alert-danger')]")
        sleep(20)
        for alert_message in alert_messages:
            close_button = alert_message.find_element(By.XPATH,".//button[@class='close']")
            close_button.click()
        sleep(8)
        self.driver.find_element(by=By.XPATH,value=locators.Bill_locators().pop_close).click()
        sleep(5)
        self.driver.find_element(by=By.ID,value=locators.Bill_locators().Total_summary).click()
        sleep(5)
        self.driver.find_element(by=By.ID,value=locators.Bill_locators().Tcs).clear()
        sleep(5)
        self.driver.find_element(by=By.ID,value=locators.Bill_locators().Tcs).send_keys('0')
        sleep(5)
        self.driver.find_element(by=By.ID,value=locators.Bill_locators().Make_payment).click()
        sleep(5)
        '''
        sleep(5)
        self.driver.find_element(by=By.ID,value=locators.Bill_locators().PAN_No).send_keys(data.Bill_Data().PAN)
        assert self.driver.title == 'Logimax Technology | Admin'
        print('PAN Number: {a}'.format(a = data.Bill_Data().PAN))
        sleep(5)
        self.driver.find_element(by=By.ID,value=locators.Bill_locators().Adhaar_no).send_keys(data.Bill_Data().Adhaar)
        assert self.driver.title == 'Logimax Technology | Admin'
        print('Adhaar Number: {a}'.format(a = data.Bill_Data().Adhaar))
        sleep(5)
        self.driver.find_element(by=By.ID,value=locators.Bill_locators().Driving_lic_No).send_keys(data.Bill_Data().Driving)
        assert self.driver.title == 'Logimax Technology | Admin'
        print('drivng license Number: {a}'.format(a = data.Bill_Data().Driving))
        sleep(5)
        self.driver.find_element(by=By.ID,value=locators.Bill_locators().Passport_no).send_keys(data.Bill_Data().Passport)  
        assert self.driver.title == 'Logimax Technology | Admin'
        print('Passport Number: {a}'.format( a = data.Bill_Data().Passport))
        sleep(5)'''
        sleep(10)
        
        if 97870.60 == 135353:
            self.driver.find_element(by=By.ID,value=locators.Bill_locators().billing_save).click()
            #bill = self.driver.find_element(by=By.ID,value=locators.Bill_locators().billing_save).text220129.02
            assert self.driver.title == 'Logimax Technology | Admin'
            print("Billing : Order delivery successfully completed")
            
        elif  97870.60 < 135353: 
            self.driver.find_element(by=By.ID,value=locators.Bill_locators().keep_it_as).click()
            checkbox_name = self.driver.find_element(By.XPATH,'//label[@for="advance_yes"]').text
            assert self.driver.title == 'Logimax Technology | Admin'
            print(f'keep it as : {checkbox_name}')
            sleep(5)
            self.driver.find_element(by=By.ID,value=locators.Bill_locators().advance_amount).clear()
            sleep(2)
            self.driver.find_element(by=By.ID,value=locators.Bill_locators().advance_amount).send_keys(balance_Amount)
            assert self.driver.title == 'Logimax Technology | Admin'
            print(f'Advance_Amount :',balance_Amount)
            sleep(5)
            self.driver.find_element(by=By.ID,value=locators.Bill_locators().billing_save).click()
            #bill = self.driver.find_element(by=By.ID,value=locators.Bill_locators().billing_save).text
            assert self.driver.title == 'Logimax Technology | Admin'
            print("Billing : Order delivery successfully completed")

            
        elif  97870.60 > 135353: 
            self.driver.find_element(by=By.ID,value=locators.Bill_locators().net_banking).click()
            sleep(5)
            net_banking = Select(self.driver.find_element(by=By.NAME,value=locators.Bill_locators().net_banking_type))
            net_banking.select_by_value('2')
            selected_option = net_banking.first_selected_option
            selected_text = selected_option.text
            assert self.driver.title == 'Logimax Technology | Admin'
            print('Net Bank type : {a}'.format(a = selected_text))
            sleep(5)
            net_bank = Select(self.driver.find_element(by=By.NAME,value=locators.Bill_locators().net_bank))
            net_bank.select_by_value('6')
            selected_option = net_bank.first_selected_option
            selected_text = selected_option.text
            assert self.driver.title == 'Logimax Technology | Admin'
            print('Net Bank Name : {a}'.format(a = selected_text))
            sleep(5)
            self.driver.find_element(by=By.NAME,value=locators.Bill_locators().payment_date).send_keys(data.Bill_Data().pay_date)
            assert self.driver.title == 'Logimax Technology | Admin'
            print('Payment Date : {a}'.format(a = data.Bill_Data().pay_date))
            sleep(5)
            self.driver.find_element(by=By.NAME,value=locators.Bill_locators().Referral_no).send_keys(data.Bill_Data().ref_no)
            assert self.driver.title == 'Logimax Technology | Admin'
            print('Referral Number: {a}'.format(a = data.Bill_Data().ref_no))
            sleep(5)
            self.driver.find_element(by=By.NAME,value=locators.Bill_locators().net_banking_amount).send_keys(balance_Amount)
            assert self.driver.title == 'Logimax Technology | Admin'
            print('Net Banking Amount : ',balance_Amount)
            sleep(5)                
            self.driver.find_element(by=By.ID,value=locators.Bill_locators().net_bank_page_save).click()
            sleep(5)
            self.driver.find_element(by=By.ID,value=locators.Bill_locators().billing_save).click()
            #bill = self.driver.find_element(by=By.ID,value=locators.Logi_Locators().billing_save).text
            assert self.driver.title == 'Logimax Technology | Admin'
            print("Billing : Order delivery successfully completed")
            
        else:
            print('Amount not meet')    
            
            
                
            
                
                
        