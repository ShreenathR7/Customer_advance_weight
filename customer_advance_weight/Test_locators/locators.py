# locators.py - File where all The HTML Locators are Kept
class Logi_Locators:
    username_inputBox = 'username'

    password_inputBox = 'password'
     
    signButton ='(//*[@id="submit_login"])'
    
    side_bar = '(//*[@role="button"])'
    
    customer_order = "//span[text()='Customer Orders']"
    
    creat_order  = '(//span[text()="Create Order"]//preceding-sibling::i[@class="fa fa-circle-o"])[1]'
    
    Add_order ="add_Order"
    
    Customer = "cus_name"
    
    Order_Branch = "select2-branch_select-container"
    
    text_box = '(//*[@role="textbox"])'
    
    Sales_Employee = 'select2-issue_employee-container'
                     
    balance_type = "metal_bal_type"
    
    tag_order = "tag_order"
    
    order_rate="order_rate"
    
    New_tag_scan = 'est_tag_scan'
    
    Tag_search = 'tag_search'
    
    Gross_weight = "weight_1"
    
    size = '(//*[@role="presentation"])[16]'
    
    Peace = "qty_1"
    
    Wast = "o_item[1][wast_percent]"
    
    Mc_type = '(//*[@role="presentation"])[16]'
    
    Mc_value = "o_item[1][mc]"
    
    other_charge = '(//*[@class="btn btn-success"])[4]'
    
    Charge_name="est_stones_item[id_charge][]"
    
    value = "est_stones_item[value_charge][]"
    
    Save_charge = "update_charge_details"
    
    description = '(//a[@class="btn btn-default btn-sm"])[2]'
    
    item_description = "description"
    
    Add_description  = '(//*[@class="btn btn-success add_order_desc"])'
    
    Due_days= '(//*[@class="form-control due_date"])'
    
    save_page = "create_order"
    
    date_range = 'rpt_payment_date'
    
    From_date ="daterangepicker_start"
    
    To_date = 'daterangepicker_end'
    
    apply  = "//button[text()='Apply']"
    
    Search = "cus_order_search"
    
    order_search = '//input[@type="search"]'
        
    Order_number = '//table[@id="order_list"]//tbody//tr//td[2]'
    
    
    
    
class Estimation_Locators:
    username_inputBox = 'username'

    password_inputBox = 'password'
     
    signButton ='(//*[@id="submit_login"])'
    
    side_bar = '//a[@role="button"]'
    
    retail_catalog = '(//*[@class="fa fa-angle-left pull-right"])[3]'
   
    estimation = "//span[text()='Estimation']"
    
    Add_Estimation  = "//span[text()='Add Estimation ']"
    
    Order_Branch = "select2-branch_select-container"
    
    
    text_box = '(//*[@role="textbox"])'
    
    Sales_Employee = '(//*[@role="presentation"])[4]'
    
    Customer = 'est_cus_name'
    
    Close = '(//*[@class="btn btn-warning"])[10]'
    
    tag_checkbox = "select_tag_details"
    
    Tag = 'select_tag_details'

    old_metal = "select_oldmatel_details"
    
    Metals = '(//span[@title="- Select Metal-"])'
    
    Metals_Type = "//span[text()='Type']"
    
    Category =  "(//span[text()='Category'])[2]"
    
    purity_metal = 'est_oldmatel[purity][]'
    
    metal_G_wt = 'est_oldmatel[gwt][]'
    
    metal_D_wt = 'est_oldmatel[dwt][]'
    
    metal_wastage_percentage = 'est_oldmatel[wastage][]'
    
    Remark = 'est_oldmatel[old_metal_remarks][]'
    
    Total_Sale_Amount = '//table[@id="total_summary_details"]//tbody//tr[5]//td[4]'
    
    Total_Advance_Paid_Amount = '//table[@id="total_summary_details"]//tbody//tr[7]//td[4]'
    
    save_print = "est_print"
    
    Branch = 'id_branch'
    
    text_box = '(//*[@role="textbox"])'
    
    date_range_estimation = "account-dt-btn"
    
    From_date ="daterangepicker_start"
    
    To_date = 'daterangepicker_end'
    
    apply  = "//button[text()='Apply']"
    
    order_search = '//input[@type="search"]'

    estimation_no = '//table[@id="estimation_list"]//tbody//tr//td[1]'
    
    
    ####################################################################
    
    Order_no_search = "est_order"
    
    Customer_order_search = "order_search"
    
    

class Bill_locators:    
    
    side_bar = '//a[@role="button"]'
    
    Billing = "//span[text()='Billing']"
    
    Bill  = "//span[text()='New Bill']"
    
    Branch = 'id_branch'
    
    text_box = '(//*[@role="textbox"])'
    
    Sales_Employee = 'select2-emp_select-container'
   
    Order_advance = 'bill_type_order_advance'
    
    Esti = 'filter_est_no'
    
    search = 'search_est_no'
    
    Order_no = 'filter_order_no'
    
    search_order_no = 'search_order_no'
    
    Alret = "//button[@class='close']"
    
    pop_close = '(//button[@class="btn btn-warning"])[15]'
    
    Total_summary = 'tab_tot_summary'
    
    Make_payment = 'tab_make_pay'
    
    Tcs = "tcs_percent"
    
    billing_save = 'pay_submit'  
    
    order_delivery = "bill_type_order_del"
    
    keep_it_as = "advance_yes"
    
    advance_amount = "advance_amount"
    
    net_banking = 'net_bank_modal'
    
    net_banking_type = 'nb_details[nb_type][]'
    
    net_bank = 'nb_details[id_bank][]'
    
    payment_date = 'nb_details[nb_date][]'
    
    Referral_no = 'nb_details[ref_no][]'
    
    net_banking_amount = 'nb_details[amount][]'
    
    net_bank_page_save = 'add_newnb'
    
    
         
    
        