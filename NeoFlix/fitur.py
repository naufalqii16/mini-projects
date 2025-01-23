from tabulate import tabulate
class User:

    def __init__(self, username, current_plan, duration_plan, referral_code):
        self.username = username
        self.current_plan = current_plan
        self.duration_plan = duration_plan
        self.referral_code = referral_code

    def __str__(self):
        return self.username

    def get_user_plan(self):
        if self.current_plan is None:
            print('You dont have any plan yet')
            return
        else:
            print(f'Your Current Plan: {self.current_plan}')
            print(f'Plan Duration: {self.duration_plan} months')
            plan_now_index = plan_type.index(self.current_plan)
            print('Plan Benefit: ')
            header = [self.current_plan, "Services"]
            table = []
            for i in range(8):
                row = []
                for j in [plan_now_index,3]:
                    row.append(plan_services[j][i])
                table.append(row)

            print(tabulate(table, header))

    def get_plan(self, index):
        headers = ['Basic', 'Standard', 'Premium', 'Services']
        table = []  
        for i in range(8): 
            row = []
            for j in range(4):
                row.append(plan_services[j][i]) 
            table.append(row)

        if index != 4:
            row = []
            for k in range(index+1):
                availability_plan[k] = False

            for m in availability_plan:
                if m:
                    row.append("AVAILABLE")
                else:
                    row.append("NOT AVAILABLE")
            table.append(row)
        print(tabulate(table, headers))

    def get_price(self, num):
        return plan_services[num][7]
    
    def get_all_referral_code(self, users):
        return [self.referral_code for i in users]

    def buy_plan(self, users):
        if self.current_plan != None:
            print('This menu is only for new user. You should pick "Upgrade plan" at the menu')
        else:
            self.get_plan(4)
            print('---------------------')
            while True:
                plan_choosed = input('Choose the type of plan you want to purchase (e.g., Standard): ')
                plan_choosed = plan_choosed.title()
                if plan_choosed not in plan_type:
                    print('Invalid plan. Please enter a valid option from the available option.')
                    print('---------------------')
                else:
                    break
            price = self.get_price(plan_type.index(plan_choosed))
            if self.referral_code in self.get_all_referral_code(users):
                price -= 0.04*price
            print(f'Total payment: {price}')
            self.current_plan = plan_choosed
            self.duration_plan = 0
            print('Transaction Completed')

    def upgrade_plan(self):
        if self.current_plan == None:
            print('You dont have any plan yet')
            print('Please choose "Buy plan" at the menu')
            return
        else:
            print(f'Your Current Plan: {self.current_plan}')
            print('Available plan to purchase: ')
            plan_now_index = plan_type.index(self.current_plan)

            if plan_now_index == 2:
                print("There are no other plan to purchase")
                return
            else:
                self.get_plan(plan_now_index)
                while True:
                    print('---------------------')
                    plan_choosed = input('Choose the type of plan you want to purchase (e.g., Standard): ')
                    plan_choosed = plan_choosed.title()
                    if plan_choosed not in plan_type:
                        print('Invalid plan. Please enter a valid option from the available option.')
                        print('---------------------')
                    elif plan_choosed == self.current_plan:
                        print('You already have this plan')
                    elif availability_plan[plan_type.index(plan_choosed)] == False:
                        print('Plan is not available')
                    else:
                        break
                        
                price = self.get_price(plan_type.index(plan_choosed))
                if self.duration_plan > 12:
                    price -= 0.05*price
                
                print(f'Total payment: {price}')
                self.current_plan = plan_choosed
                self.duration_plan = 0
                print('Transaction Completed')

plan_type = ['Basic', 'Standard', 'Premium']
availability_plan = [True, True, True]
plan_services = [['yes', 'yes', 'yes', 'no', 'no', '1', '3rd party movie only', 120000],
                [ 'yes', 'yes', 'yes', 'yes', 'no', '2', 'basic plan content \n+ sports (F1, Football, Basketball)', 160000],
                ['yes', 'yes', 'yes', 'yes', 'yes', '4', 'basic plan + standard plan \n+ NeoFlix original series or movie', 200000],
                ['can_stream', 'can_download', 'has_sd', 'has_hd', 'has_uhd', 'num_of_devices', 'content', 'price']]